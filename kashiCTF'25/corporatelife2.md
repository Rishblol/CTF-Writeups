## Question
The disgruntled employee also stashed some company secrets deep within the database, can you find them out?

## Solution
Same endpoint we have to go to as the previous challenge, but the SQLi requires UNION injection to view the contents of another table.
![image](https://github.com/user-attachments/assets/cbaf9793-4b8d-4478-a79f-3798c4d6a003)

Using this query, we can figure out and inject the query to get the secret flag.
![image](https://github.com/user-attachments/assets/b52b8b82-f471-48bc-9642-54a6274e85e4)

Injecting `' OR 1=1 UNION SELECT request_id, secret_flag,null, null,null,null FROM flags --` we get parts and joining them to get the flag.
flag: `KashiCTF{b0r1ng_old_c0rp0_l1f3_am_1_r1gh7_FbU5cNXH}`



