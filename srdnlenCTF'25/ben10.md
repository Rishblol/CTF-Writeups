## Question 
Ben Tennyson's Omnitrix holds a mysterious and powerful form called Materia Grigia — a creature that only those with the sharpest minds can access. It's hidden deep within the system, waiting for someone clever enough to unlock it. Only the smartest can access what’s truly hidden. Can you outsmart the system and reveal the flag?

## Solution
So we've been given a site having a register, login and a home page containing all the transformations present in the omnitrix.\
![image](https://github.com/user-attachments/assets/29ec37ab-053d-43ba-be10-5de88de93b7f)

After creating the account and logging in, we are redirected to this page.\
![image](https://github.com/user-attachments/assets/3e1f6df9-7a24-4699-92c6-9767736fd005)

Looking at the [source code](https://github.com/Rishblol/CTF-Writeups/blob/main/srdnlenCTF'25/files/ben10/app.py), we can see this ```app.secret_key = 'your_secret_key'``` which creates an unsigned flask cookie.

Our aim to access ben10, which we aren't allowed to access because of lack of permissions.
![image](https://github.com/user-attachments/assets/bfe17c52-7874-4ae4-bc46-dc30b21b4413)

Unsigning (Brute Forcing Secret Keys) via this [program](https://github.com/Paradoxis/Flask-Unsign), we can write `flask-unsign --sign --cookie "{'username': 'admin'}" --secret 'your_secret_key'` and change the site cookie to get the flag.\
![image](https://github.com/user-attachments/assets/4b8ddaf4-4d00-492f-9896-a1d0661d2201)

`flag: srdnlen{b3n_l0v3s_br0k3n_4cc355_c0ntr0l_vulns}`


