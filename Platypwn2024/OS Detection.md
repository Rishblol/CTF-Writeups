## Question
A new service has been deployed that uses advanced algorithms to detect your Operating System. What an invasion of privacy! Can you pwn it?

## Solution
So this problem is basically a SSTI (Server Side Template Injection) problem where the website detects your os via your user-agent in the headers section. This being a flask app (from source code) we see the altering the user-agent header gives us different results.
![osdetect](https://github.com/user-attachments/assets/c998d4af-b141-4e84-8f52-0edd13f9bbc6)

so writing ```{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag/flag.txt').read()}} ``` in the user-agent header, you should get something like this:
![osdetectflag](https://github.com/user-attachments/assets/2fb6fe07-d93c-4b6f-860b-f6c67eab793e)



