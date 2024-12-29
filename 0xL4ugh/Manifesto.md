## Question 
This is an easy challenge, except... it's written in Clojure. Can you find your way through all of these parentheses and come out victorious?

## Solution 
This is a Clojure Web Application having `Home`,`Login` and `Gists`.
![image](https://github.com/user-attachments/assets/6d92b2b0-9d31-4458-80bc-186df03b32da)

Looking at the source code, we can get admin access by writing /?username=admin in front of the instance url and we're in!
![image](https://github.com/user-attachments/assets/4c7e26c0-04de-4594-8a96-48b12d29b143)

Going to the Gists page, this is a case of LFI via shell, and writing `#=(slurp "/proc/self/environ")` we get the flag.
![image](https://github.com/user-attachments/assets/1b5c1905-15aa-42f9-b637-666f1722bb21)
