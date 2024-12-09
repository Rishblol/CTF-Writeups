##Question
A new service has been deployed that uses advanced algorithms to detect your Operating System. What an invasion of privacy! Can you pwn it?

##Solution
So this problem is basically a SSTI (Server Side Template Injection) problem where the website detects your os via your user-agent in the headers section. This being a flask app (from source code) we see the altering the user-agent header gives us different results.

so writing ```{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag/flag.txt').read()}} ``` in the user-agent, you should get something like this:



