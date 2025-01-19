## Question
Here are API endpoints for a blog website.

## Solution 
From the source code, we know that each post is associated with a user (the author), and that this user has a password, and the post containing the flag has a `published:false` status.
![image](https://github.com/user-attachments/assets/c7a5063d-cce9-45e7-b068-158857e9e3d7)

This code snippet was the interesting part.
```javascript
let query = req.query;
query.published = true;
let posts = await prisma.post.findMany({where: query});

res.json({success: true, posts})
```

We do need the credentials from any of the 4 users with their passwords to view all the posts.
Using this [solver script](https://github.com/Rishblol/CTF-Writeups/blob/main/UofTCTF'25/uploads/prismatic-blogs/solve/solve.py), we can retrieve all the posts and get the flag.\
`flag:uoftctf{u51n6_0rm5_d035_n07_m34n_1nj3c710n5_c4n7_h4pp3n}`


