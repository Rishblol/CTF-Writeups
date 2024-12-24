## Question
I created the world's most secure notes app, but might have uploaded and forgotten about some personal files. Whatever, even if they try to look for them they will go to the wrong place.

## Solution
While F12ing around the page, we see that the background image is referenced from /uploads.
![image](https://github.com/user-attachments/assets/bccec2ea-a7b1-4a16-824d-c0f3779ee925)

Going towards the upload section, we see a bunch of logs in it.
![image](https://github.com/user-attachments/assets/75317882-6120-4227-bf38-818b435a4d9f)

From these logs, we get the ```username: D3aDs0ck``` and ```password: bluM#_M@y_N3vr``` and we login to the website.
The Dockerfile contained JWT_SECRET_KEY & FDRP_JWT_SECRET_KEY.
![image](https://github.com/user-attachments/assets/d2b07605-e48f-4660-99a8-4f82d4f42878)

Now, decode and change the secret with JWT_SECRET_FILE and we get the flag.
![image](https://github.com/user-attachments/assets/fc587ecd-2c32-4764-b8a3-dda1c85b3dfd)

```flag: nite{7rY_XKcD_S3b_f0R_3xPl4nA7i0n}```




