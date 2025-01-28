## Question
My startup is launching the next big patient portal, using the hottest new tech! Check it out with our guest account: Demo:TUCTF. We're still in beta, but it's so secure we already have users! Note: This challenge requires no bruteforcing or intense scanning of the application.

## Solution
We've been given a website having a login page with either "doctor" or "patient" role.
![image](https://github.com/user-attachments/assets/dec1ff81-c1e4-41bc-b27d-801c9afbc9d6)

Logging in with the given credentials, we're taken to the patient page.
![image](https://github.com/user-attachments/assets/b7123d92-a0e9-4025-80fb-0c923ad2b661)

Loading the site on Burp Suite, we see the it displays the info based on a GraphQL query.
![image](https://github.com/user-attachments/assets/769317f6-1e04-48ae-9427-64bc7d81982d)

Sending this to repeater and writing `"query":"{ __schema { types { name fields { name type { name } } } } }"` we get all the classes.
![image](https://github.com/user-attachments/assets/c708ad0b-c525-486a-b236-e5dd4a315c4c)

Sending `"query":"{ userData { doctor { id name department password } } }"` to repeater, we get the doctor credentials.
![image](https://github.com/user-attachments/assets/3ccc6357-dafd-4845-9378-f7d5e079097a)

Decoding the password in [CrackStation](https://crackstation.net/) we get the password as `madjac`.

Logging in as `username: Ivy`, `password: madjac` and `role: Doctor`, we enter and get the flag.
![image](https://github.com/user-attachments/assets/8eed4998-7985-4f48-beb1-f6ab4d401aac)

`flag: TUCTF{w3_7h1nk_1n_6r4ph5}`
