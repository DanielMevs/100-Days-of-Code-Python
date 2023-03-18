import smtplib
my_email = "onetime26832@gmail.com"
password = "yrykkrzfjjayywhu"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="danydacoder@gmail.com", msg="Hello")
connection.close()
