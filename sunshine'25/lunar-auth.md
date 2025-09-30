## Description
Infiltrate the LunarAuth admin panel and gain access to the super secret FLAG artifact !

## Solution
Upon clicking the site link we reach this page.
<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/3afd2ded-6dc0-4e83-85b5-788265c463a1" />

Given that they've mentioned `Robot Protocol` we can go and explore `/robots.txt` and we see a `disallow: /admin` in the page.

Going there we reach the admin page-
<img width="1899" height="874" alt="image" src="https://github.com/user-attachments/assets/e7b3a03a-faf0-4754-8404-7c1cf21c9950" />

Inspecting the page we see this text-
```js
 /*
    To reduce load on our servers from the recent space DDOS-ers we have lowered login attempts by using Base64 encoded encryption
    ("encryption" 💀) on the client side.
    
    TODO: implement proper encryption.
    */
    const real_username = atob("YWxpbXVoYW1tYWRzZWN1cmVk");
    const real_passwd   = atob("UzNjdXI0X1BAJCR3MFJEIQ==");
```

this is base64 text and converting it we get the credentials and once logging in we obtain the flag `sun{cl1ent_s1d3_auth_1s_N3V3R_a_g00d_1d3A_983765367890393232}`

