## Question 
Click acorns. Buy squirrels. Profit.

## Solution 
Here in this site, we are given a login and register page, and after doing that we see a page like this.
![image](https://github.com/user-attachments/assets/f4307632-fda1-4c8d-b2d0-bb3d995479df)

As we can see, the amount to buy the flag is too huge, and would take a long time.

Looking at their source code they do be using mongoDB, which we can go about deserializing the amount from and int to NaN. 

The way I did it was I logged in as admin (creds were admin and admin) and it shows NaN acorns.
![image](https://github.com/user-attachments/assets/ea8b288c-fe6f-4edc-bf49-a439183e04f5)

And we click on buy flag and obtain: `squ1rrel{1nc0rr3ct_d3s3r1al1zat10n?_1n_MY_m0ng0?}`

