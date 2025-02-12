## Question
Just click the flag :)

## Solution 
Here we've been given a website which looks like this
![image](https://github.com/user-attachments/assets/b5fe46b7-3387-4c50-b548-42792634323f)

The source code was given in `main.js` -
```javascript
const $ = q => document.querySelector(q);
const $a = q => document.querySelectorAll(q);

const boxes = $a('.box');
let flagbox = boxes[Math.floor(Math.random() * boxes.length)];

for (const box of boxes) {
  if (box === flagbox) {
    box.onclick = () => {
      let enc = `"\\u000e\\u0003\\u0001\\u0016\\u0004\\u0019\\u0015V\\u0011=\\u000bU=\\u000e\\u0017\\u0001\\t=R\\u0010=\\u0011\\t\\u000bSS\\u001f"`;
      for (let i = 0; i < enc.length; ++i) {
        try {
          enc = JSON.parse(enc);
        } catch (e) { }
      }
      let rw = [];
      for (const e of enc) {
        rw['\x70us\x68'](e['\x63har\x43ode\x41t'](0) ^ 0x62);
      }
      const x = rw['\x6dap'](x => String['\x66rom\x43har\x43ode'](x));
      alert(`Congrats ${x['\x6aoin']('')}`);
    };
    flagbox = null;
  } else {
    box.onclick = () => alert('no flag here');
  }
};
```

The JavaScript code reveals that the flag is hidden within one of the buttons and will be displayed if the correct button is clicked. However, the flag string is encrypted using an XOR operation with the value 0x62.

Writing this solve script-
```python
enc_str = "\u000e\u0003\u0001\u0016\u0004\u0019\u0015V\u0011=\u000bU=\u000e\u0017\u0001\t=R\u0010=\u0011\t\u000bSS\u001f"

# Perform XOR with 0x62 to decrypt
decrypted_chars = [chr(ord(c) ^ 0x62) for c in enc_str]
flag = "".join(decrypted_chars)

print(flag)
```
We get the flag: `lactf{w4s_i7_luck_0r_ski11}`
