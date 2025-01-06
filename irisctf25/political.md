## Question
My new enterprise policy ensures you will remain flag-free.

## Solution 
Here they've given a site to redeem a random generated token, and a bot to connect to via `Netcat`.

Looking at the source code, we see that we have to give it a a url starting with `https://political-web.chal.irisc.tf/`.

The URL submitted must not contain certain patterns found in the `policy.json` file.
```json
{
	"URLBlocklist": ["*/giveflag", "*?token=*"]
}
```

Hence, the payload we give the bot is: `https://political-web.chal.irisc.tf/giv%65flag?tok%65n=a21c924f2255f66f1cc60a5bc72f55f6 `. This bypasses the conditions as JavaScript does not normalize any type of encoding and thus interprets /giv%65flag differently from /giveflag. The same goes for /?token=. As such, the policy isn't triggered.
Now, we go the /redeem part of the website to get thet flag.
![image](https://github.com/user-attachments/assets/fcb856cb-7678-4b25-a730-6910c514b2bd)

`flag:irisctf{flag_blocked_by_admin}`
