import smtplib
import datetime as dt
import random

my_email = "onetime26832@gmail.com"
my_password = "yrykkrzfjjayywhu"
RECIPIENT = "danydacoder@gmail.com"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.ehlo()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                to_addrs=RECIPIENT,
                msg=f"Subject:Saturday motivational quote\n\n" + quote)
            
        print('Email sent!')
    except Exception as e:
        print(e)
        print("unsuccessful")