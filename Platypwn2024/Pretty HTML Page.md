## Question
I made a pretty HTML page. It can even give you a flag if you write “flag”! But for security reasons, as soon as you write “flag”, your input will get redacted. Sorry for that :)

## Solution 
So this is a problem based on a PHP bug as discovered in CVE-2024-21726 we were supposed to exploit the inconsistent behaviour of PHP's multibyte string methods.
The comparison of the input string and `"flag"` is done with PHP's `mb_strpos` and `mb_substr`. Up to PHP 8.2, those methods count characters in a string differently as soon as there are broken UTF-8 characters present.
![image](https://github.com/user-attachments/assets/32190477-aa48-4183-ae31-ec39e36b5234)

So using this [python script]() we can input and get the flag as follows:
![image](https://github.com/user-attachments/assets/ee5b59fe-a714-4094-9ab6-5c631e449581)

flag: ```PP{c0Unt1n6_ch42AC73r5-15_h4rD::ce56eUL_49s6}```

