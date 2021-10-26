import smtplib

import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

DEAL_PRICE = float(629.00)
from_email = "priyasmtptest@gmail.com"
password = "as1234.,"
to_email = "aplisipriya1998@gmail.com"
account_sid = "ACf87db75e19e511ef0f7cc90d7e635167"
auth_token = "f2bd30ddda1b3034a2a184451b6564c9"
FROM_NUM = "+18456225337"

BASE_URL = "https://www.amazon.in/Mattress-Protector%C2%AE-Waterproof-Protector-Skirting/dp/B085975N1Y/ref=sr_1_4" \
           "?dchild=1&keywords=wakefit%2Bmattresses%2Bprotector&qid=1635248279&qsid=261-8672915-7435315&sprefix" \
           "=wakefit%2B%2Caps%2C760&sr=8-4&sres=B083JB58P6%2CB085975N1Y%2CB0859B7DY5%2CB08R8XS8R8%2CB01A57IV58" \
           "%2CB07KPF324W%2CB076FX3NQ4%2CB07PXLWY3Q%2CB0822WJWGS%2CB06XHLH8VM%2CB08RG759N3%2CB08P6XGBTK%2CB07WC5FVS7" \
           "%2CB01GV0IDA6%2CB0924NVNYB%2CB099WQRYPP&srpt=MATTRESS_COVER&th=1 "
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    # "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "User-Agent": "Defined"
}


response = requests.get(BASE_URL, headers=headers)
amazon_res = response.text
# print(amazon_res)
soup = BeautifulSoup(amazon_res, "html.parser")
product_title = soup.find(name="span", id="productTitle").get_text()

price_tag = soup.find(name="span", id="priceblock_dealprice")
price = float(price_tag.getText().split("₹")[1])

if price <= DEAL_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject:Amazon Price Alert\n\n{product_title.strip()} is now {price}.\n{BASE_URL}"
        )

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"\nAmazon Price Alert\n\n{product_title.strip()} is now {price}.\n{BASE_URL}",
        from_=FROM_NUM,
        to="+918940400485"
    )

    print(message.status)