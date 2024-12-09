## Question
After starting my studies, I wanted to play around with LaTeX. So I built a web-based editor! Unfortunately, people have tried hacking it, so I needed to blacklist some commands. But I’m sure it’s 100% secure now! :) I also made the app restart if it crashes, I just hope that people can’t abuse that for something. But hey, it’s just a restart, right? What could possibly go wrong?

## Solution
LaTeX is utterly broken, with a lot of vulnerabilities. 
![image](https://github.com/user-attachments/assets/488b2266-a297-4157-b249-752442884125)

Looking at this [python script]() given for the challenge, we can see that they've "blocked" certain commands from being used, but we can still by-pass this by writing ```\begin{inpu\iftrue t\fi}{"/flag/flag.txt"}``` which when clicking on the render button gives as follows:
![image](https://github.com/user-attachments/assets/931f5cb0-b356-492e-aa7d-f661ab77201c)

flag: ```PP{g3t-t3x3d::tz7jKqyP74f}```

