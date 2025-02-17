![image](https://github.com/user-attachments/assets/34e9c91a-ad89-4e66-9425-afb9488b88b5)## Question
I have this friend mary who has a lamb that only responds to a specific dial tone. Can you help mary find her lamb?

## Solution
Here we've been given a website which looks like this.
![image](https://github.com/user-attachments/assets/a05664cd-e894-42d0-8b44-a3b53a57a4e5)

This is just a simple dialpad where each number makes a sound note of the poem "Mary has a little lamb". The problem is the app resets after every 5-6 seconds, hence we can't write all the notes without it resetting.
We intercept the request in BurpSuite, and we see that it returns the website like `<site>/<numbers you've written>`.
![image](https://github.com/user-attachments/assets/5943aff8-3a91-4691-b9ca-5e2cbbf78f5f)

After bruteforcing for a long time, the final sequence `32123332223993212333322321` is what we have to send the request and we get the flag.
![image](https://github.com/user-attachments/assets/743015be-7094-4140-8c23-c1244b97179c)

flag: `bronco{W0ah_y0u_f0und_m4rys_1itt1e_1amb}`


