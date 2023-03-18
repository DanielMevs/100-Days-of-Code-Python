import smtplib
my_email = "onetime26832@gmail.com"
my_password = "yrykkrzfjjayywhu"
RECIPIENT = "danydacoder@gmail.com"


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="danydacoder@gmail.com", msg="Hello")
# connection.close()
quote = "You are awesome"


try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.ehlo()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
            to_addrs=RECIPIENT,
            msg="Subject:Motivational quote\n\n" + quote)
        
    print('Email sent!')
except Exception as e:
    print(e)