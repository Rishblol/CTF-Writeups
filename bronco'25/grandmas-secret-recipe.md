## Question
Grandma has been baking her world-famous cookies for decades, but she’s always kept her secret recipe locked away. Nobody—not even her most trusted kitchen helpers—knows the full list of ingredients.
She insists it’s all about "the perfect balance of love and a pinch of mystery", but deep down, you know there’s more to it. Rumors say only Grandma herself is allowed to see the recipe, hidden somewhere in her kitchen.
But, you were hired by Grandpa, who divorced her because she refused to share the recipe. Can you figure out the true secret behind her legendary cookies?

## Solution
Here we've been given a website having login, logout and Grandma's pantry. Clicking on login, we have logged in as "Kitchen Helper".
![image](https://github.com/user-attachments/assets/421113e8-8e52-4daf-a34e-5a1d6c2d5913)

We look into our cookies and we see that we've been given a checksum and a role. The checksum here is the md5 sum of the value "Kitchen Helper".
![image](https://github.com/user-attachments/assets/dd9902a1-bb5f-4fc0-b6ff-1b1f47f462fc)

Our aim is to access Grandma's pantry by changing the cookie values.\
Changing the role to `grandma` and checksum value as `a5d19cdd5fd1a8f664c0ee2b5e293167` and reloading the page, we get out flag.
![image](https://github.com/user-attachments/assets/50cbc33b-7a69-4c15-a3ba-9460f577731f)

flag: `bronco{grandma-makes-b3tter-cookies-than-girl-scouts-and-i-w1ll-fight-you-over-th@t-fact}`

