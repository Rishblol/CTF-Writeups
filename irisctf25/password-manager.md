## Question
It looks like skat finally remembered to use his password manager! One small problem though, he forgot his password to the password manager!

## Solution
Looking at the source code, we see two suspicious code snippets
![image](https://github.com/user-attachments/assets/48fcb5cf-525d-4913-bbee-7432dbda9a85)
![image](https://github.com/user-attachments/assets/cee15142-2966-4bd1-9956-ecf1c1b8d209)

We have to try and get into users.json to try and figure the credentials. Going into BurpSuite we change the required path to get into `/users.json` -
![image](https://github.com/user-attachments/assets/43a875be-6ece-46c0-bb57-952e6af068f7)

Logging in with these credentials we get to the `passwords` page:
![image](https://github.com/user-attachments/assets/13e33cd7-7023-4659-a254-5092e8583659)

`flag: irisctf{l00k5_l1k3_w3_h4v3_70_t34ch_sk47_h0w_70_r3m3mb3r_s7uff}`

