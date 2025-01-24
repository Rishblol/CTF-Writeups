## Question
Sometimes, seemingly harmless configuration files can do more than they appear. Can you uncover a hidden flaw and turn it to your advantage?

## Solution 
Here we've been given a site with a base64 encoding as its endpoint and that is the message being displayed in the content.
![image](https://github.com/user-attachments/assets/a6c23973-6718-493b-9193-ad8e693dc737)

Reading this [challenge](https://trevorsaudi.medium.com/yaml-2-json-hackpack-ctf-7de28ef0ecff), I figured that something is possible of the sort.

So we wrote `yaml: !!python/object/apply:os.system ["id"]` and converted it to base64.
![image](https://github.com/user-attachments/assets/e814368f-9414-42dd-9537-0f5cc6a998c2)

This gave an error and aftering altering for some time, using this command: `yaml: !!python/object/apply:os.listdir []` and we get the flag.
![image](https://github.com/user-attachments/assets/6cdba07d-dd00-4ae4-9963-d290dfae66bd)

`flag: KCTF{d38787fb0741bd0efdad8ed01f037740}`

