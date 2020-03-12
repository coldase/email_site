import smtplib
from email.message import EmailMessage

email = EmailMessage()

#username, password, receiver, subject, message 
def send_email(usr, pwd, to, sub, msg):
	email["from"] = usr
	email["to"] = to
	email["subject"] = sub
	
	email.set_content(msg)

        #host by mail.com, wokrs only with those emails
	with smtplib.SMTP(host="smtp.mail.com", port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(usr, pwd)
		smtp.send_message(email)
