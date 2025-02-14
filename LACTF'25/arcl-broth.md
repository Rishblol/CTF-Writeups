## Question
I heard Arc'blroth was writing challenges for LA CTF. Wait, is it arc'blroth or arcl broth?

## Solution 
We've been given a website having a registration and login, where we can go and make "broths".
![image](https://github.com/user-attachments/assets/2e3e60cc-2c0c-4b5f-81b0-fead7d439bb4)

Our aim is to get admin access to get the flag, based on the source code via `Null Byte Injection`.
Trying to register as admin, we intercept the request and notice that it puts and extra backslash in the request.
![image](https://github.com/user-attachments/assets/c7bf818c-b71b-4a70-ae7a-92dc03b0848a)

Then we correct that payload to `username: admin\u0000hax` and `password: password`.
![image](https://github.com/user-attachments/assets/93c79d6f-990f-473e-84d8-84ada11b55d1)

Voila! We're in! Now, we replenish our arcs and brew our broth, which take 50 arcs and gives us the flag.
![image](https://github.com/user-attachments/assets/715fc42b-95f7-4ef0-871d-64533d3eba12)

![image](https://github.com/user-attachments/assets/0aad8773-248e-4d94-813e-31f8dbed50c8)

`flag: lactf{bulri3v3_it_0r_n0t_s3cur3_sqlit3_w4s_n0t_s3cur3}`




