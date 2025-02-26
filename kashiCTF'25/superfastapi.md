## Question
Made my verty first API!
However I have to still integrate it with a frontend so can't do much at this point lol.

## Solution
Clicking on the challenge instance, we've been greeted with a site like this.
![image](https://github.com/user-attachments/assets/51135880-2b9d-4a98-b778-187d67535194)

Since it's using a `FastAPI`, it'll have a /docs endpoint, so we write that and we're shown this interface.
![image](https://github.com/user-attachments/assets/8729b9ee-70f0-4aec-bbae-10af59976dcf)

There are many endpoints given, so let's make a new user.
![image](https://github.com/user-attachments/assets/97d18758-93b6-4307-ae57-29c9e95c2af9)

Now, we'll go to the `get/{username}` endpoint and see the details.
![image](https://github.com/user-attachments/assets/0db9644a-dce0-40a9-acaa-2accedc5651c)

Here we see that our role is "guest". Our aim is to change the role to "admin" and get the flag.
So we go to `update/{username}` endpoint and change our role to `admin`
![image](https://github.com/user-attachments/assets/5d6f4d81-5d22-48f6-afd5-367bb5b80d90)

Now we go to `flag/{username}` endpoint and we'll get the flag!

flag: `KashiCTF{m455_4551gnm3n7_ftw_wR88yBTTQ}`




