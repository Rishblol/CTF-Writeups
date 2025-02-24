## Question
If you're tired of fast and good-looking editors, try this.
Now with extra crispiness!

## Solution
Here we've been given a website which looks like this.
![image](https://github.com/user-attachments/assets/3db433f7-25ef-4d08-a0e1-1ee39c356ac6)

With their source code, there's a `app.py`:
```python
import ast
import traceback
from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/check")
def check():
    try:
        ast.parse(**request.json)
        return {"status": True, "error": None}
    except Exception:
        return {"status": False, "error": traceback.format_exc()}
        
if __name__ == '__main__':
    app.run(debug=True)
```

and `secret.py`:
```python
def main():
    print("Here's the flag: ")
    print(FLAG) 
    
FLAG = "TRX{fake_flag_for_testing}"

main()
```

From the code, we can figure out that it's a `ast.parse` vulnerability. Using repeater in BurpSuite we write incorrect code and a `filename: secret.py`

![image](https://github.com/user-attachments/assets/a8e3a93b-3fae-4d4a-8db2-a374a30b98e4)

Here we can see that it's printing the second line of the code after the error. This is the vulnerability where it'll give the error of that respective line and would print that exact line of the filename given.
So we have to try and trigger the `main()` function, and so we write the payload and voila! we get the flag.
![image](https://github.com/user-attachments/assets/96005b15-5498-4f02-9ad0-9e2552e27e50)

flag:`TRX{4ll_y0u_h4v3_t0_d0_1s_l00k_4t_th3_s0urc3_c0d3}`

