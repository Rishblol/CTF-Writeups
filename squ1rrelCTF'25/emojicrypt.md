## Question
Passwords can be more secure. We’re taking the first step.

## Solution
Going to the website, we see a page like this-
![image](https://github.com/user-attachments/assets/136867d2-693a-4ed9-83dc-1e2014030b16)

and looking at the source code-
```python
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    username = request.form.get('username')

    if not email or not username:
        return "Missing email or username", 400
    salt = generate_salt()
    random_password = ''.join(random.choice(NUMBERS) for _ in range(32))
    password_hash = bcrypt.hashpw((salt + random_password).encode("utf-8"), bcrypt.gensalt()).decode('utf-8')

    # TODO: email the password to the user. oopsies!
```

We see that we aren't given the password to us.

Seeing the code, it's mainly made for flag query and since they're using bcrpyt, the maximum password length is 72.

Looking at the logic for password generation-
```python
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return "Missing username or password", 400
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT salt, password_hash FROM users WHERE username = ?", (username,))
    data = cursor.fetchone()
    if data is None:
        return redirect(url_for('index', incorrect='true'))
    
    salt, hash = data
    
    if salt and hash and bcrypt.checkpw((salt + password).encode("utf-8"), hash.encode("utf-8")):
        return os.environ.get("FLAG")
    else:
        return redirect(url_for('index', incorrect='true'))
```
and-
```python
emojis = ["🍔", "🎁", "🍁", "😄", "🎵", "🍒", "🍖", "🌱", "🍀", "🌰", "🍎", "🌈"]
letters = "aa"

result = ''.join([emoji + letters for emoji in emojis])
byte_string = result.encode('utf-8')
print(byte_string)
```
with the emoji list (12 emojis) which they use to generate the salt plus 22 "a" characters, which comes up with a total of 70 characters, we need to bruteforce the last 2 digits to login.

We then write a script to find numbers between 0-99 to login, we then obtain the flag: `squ1rrel{turns_out_the_emojis_werent_that_useful_after_all}`
