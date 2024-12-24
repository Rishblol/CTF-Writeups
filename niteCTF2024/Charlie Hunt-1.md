## Question
Charlie secured his website after an attack on his website. Do you think you can find something?

## Solution 
So there was a website with only chocolate products and a star-review system along with it. Going in BurpSuite we see the following:
![image](https://github.com/user-attachments/assets/7ef53a26-9479-4284-af65-2666bc07b3b6)

Changing the Api version v2 to v1 and the non-numeric value to the stars it will throw the error.
![image](https://github.com/user-attachments/assets/a3911150-d5fc-4fe5-9583-04a5f41093cf)

When sending a payload of {{7*7}} it returns 49, signifying a SSTI. Thus we create a payload to try and read the flag.
![image](https://github.com/user-attachments/assets/09ae61f8-c806-48d7-b8a5-8223dbe7cf63)

```flag: nite{3rror5_can_b3_u53ful_s0m3t1m35}```




