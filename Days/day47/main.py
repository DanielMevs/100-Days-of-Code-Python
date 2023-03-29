import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B0B4PQDFCL/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
BUY_PRICE = 95
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)
price = soup.find(name="span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("<YOUR_EMAIL>", "<YOUR_PASSWORD>")
        connection.sendmail(
            from_addr="<YOUR_EMAIL>",
            to_addrs="<YOUR_EMAIL>",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )