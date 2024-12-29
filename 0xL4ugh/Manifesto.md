![image](https://github.com/user-attachments/assets/6ad7f62c-b629-419a-9a74-c5730775bd32)## Question 
This is an easy challenge, except... it's written in Clojure. Can you find your way through all of these parentheses and come out victorious?

## Solution
So this is a website written in clojure, with the source code given [here](). 
It has three pages, `Home`, `Login`, and `Gists`, which is our main priority.
![image](https://github.com/user-attachments/assets/52248036-87c6-4674-b72c-2efbdb361415)

Looking at the source code we can login as admin by just `http://localhost:4000/?username=admin`, and we get to gists.
![image](https://github.com/user-attachments/assets/cc7d4a7e-1379-45e6-af62-8078d86f552f)

From here, it's just LFI via shell, insert `#=(slurp "/proc/self/environ")` in the textbox to get the flag.
![image](https://github.com/user-attachments/assets/81e620ce-477b-4d7e-aba3-8ee4b71089d4)

flag: `0xL4ugh{w5Rwzs2XntZaqnorcYFbJDnfieSjovhv}`

