## Question
A simple login page can you get past it? And remember there are secrets you will have to figure out. After you find the flag remember that the format is TUCTF{(FLAG)} and the if the flag has spaces use _ instead when submitting.

## Solution
In this challenge, they've given a login page and we have to bypass that.
![image](https://github.com/user-attachments/assets/c92a43c5-db58-441c-991f-f0e086ba2f56)

It was basic sqli, writing `username: admin' OR '1'='1` we get access to the secret page.
![image](https://github.com/user-attachments/assets/c6153399-fbbb-49ec-b607-405138fdbb61)

Here these symbols are from `mistborn steel alphabet` and decoding the message we get the flag.

`flag: TUCTF{Allomancy_is_power}`

