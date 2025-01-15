## Question
Can you get the flag without having anything?

## Solution
They've given a site with a textbox, and to give the flag to a specific user.\
Go to Networks tab and reload the site, you get a message saying `To get a list of users, you need to send a GET request to /api/users.\nAlso, don't forget to set a cookie with the name \"role\" and the value \"admin\`.

Doing that we get `[{"name":"Alice"},{"name":"Bob"},{"name":"Charlie"},{"name":"Eve"},{"name":"FlagUser"}]` and upon entering FlagUser we get the flag.\
![image](https://github.com/user-attachments/assets/50881674-3249-43ec-8e48-13ef19a3c16c)

`flag:grodno{api_of_a_healthy_person?}`

