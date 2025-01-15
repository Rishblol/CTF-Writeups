## Question
I found an internal tool of the store that creates a barcode for the product. Maybe there is a flag there?

## Solution
In this site, there's a create barcode option and view product via sending the barcode.

When generating a barcode, the application returned a reference to the file location in the HTML source-
![image](https://github.com/user-attachments/assets/75e2148f-8bdb-478c-9848-344d4013791c)

The filenames follow a predictable numeric sequence (<number>.png). This suggested it might be possible to access earlier barcodes by substituting the number in the path.
By replacing 6325.png with 1.png, the first barcode generated was accessed-
![image](https://github.com/user-attachments/assets/722f3647-160c-419a-bfd3-ff8b7f1b1e64)

The `1.png` file was downloaded and uploaded back into the web application using the designated input field. Upon submission, the application validated it and returned the flag.
![image](https://github.com/user-attachments/assets/92eef3c7-e068-425b-a32c-e1bcb279ce70)

`flag:grodno{7eb13bfd35b2f61de9edb6064e40bfa5}`
