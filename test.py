import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


my_address = 'yashbhatt289@gmail.com' 
reciever_address = ['yash.bhatt103501@marwadiuniversity.ac.in', 'yashbhatt.dev@gmail.com']

#Email 
msg = MIMEMultipart()

msg['From'] = my_address
msg['To'] = " ,".join(reciever_address)
msg['subject'] = 'Checking Email Automation'

body = 'Hey There! Just checking my email automation!!!!!!'

msg.attach(MIMEText(body,'plain'))

#Sender's EMail Id and Password.

email = "yashbhatt289@gmail.com"
password = "why@$#99"

#Sending Email through SMTP.
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text = msg.as_string()
mail.sendmail(my_address,reciever_address,text)
mail.quit()











""""
server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #Required to check settings of Gmail,
server.login("yashbhatt289@gmail.com", "why@$#99")

server.sendmail("yashbhatt289@gmail.com",
                "yash.bhatt103501@marwadiuniversity.ac.in",
                "Hey! This is just automation testing.")

server.quit()
"""


