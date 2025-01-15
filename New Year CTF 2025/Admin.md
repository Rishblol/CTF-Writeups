## Question
Can you log in as admin?

## Solution
They had given a site having username and password field.\
Basic WAF injection, you can bypass by writing `username: admin' || '1'='1` and enter any random password, you get the flag.
![Screenshot 2025-01-14 122056](https://github.com/user-attachments/assets/b707c129-1cd7-4004-b421-36aeaec7bdd0)

`flag: grodno{th3r3_1s_n0_w4f_f0r_hum4n_stup1d1ty}`
