## Question
Try to log in as a KevinM user

## Solution
We've been given with a site which looks like this.
![image](https://github.com/user-attachments/assets/390d2d09-a60f-483b-84c5-1e27605a95e3)

The site has endpoints at `index.html`, `upload.html` which doesn't work and a `/scripts.html` where in the source code it shows this:
![image](https://github.com/user-attachments/assets/09245d25-d934-4ddd-959d-f06aded5af3a)

Translating 检查一下, it says check it out and `bG9jYWxob3N0OjMwMDAvZG93bmxvYWQ/ZmlsZW5hbWU9c2VjcmV0` when base64 decoded shows `localhost:3000/download?filename=secret`

We then proceed to do that, and it gives a .txt file which has a HUGE amount of base64 text which has been encoded multiple times.
We write a script to decode the text and we get: `username: 'KevinM' & password: ^32i6;xqOFYkqg$l=wq^8-?jO^SIpT`

We have the credentials to login, but we don't see any endpoint to login, so we go towards the `/login` endpoint
![image](https://github.com/user-attachments/assets/cc00aa8d-18a8-4d5b-a464-922db10a69f2)

and enter our credentials and we get the flag.
![image](https://github.com/user-attachments/assets/40d8bfd9-093c-4b9e-ba4d-5f264ef78279)

flag: `CTF{L0g1n_M4st3r_2025}` 


