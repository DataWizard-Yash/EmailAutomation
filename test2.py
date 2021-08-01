import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #Required to check settings of Gmail,
server.login("yashbhatt289@gmail.com", "why@$#99")

server.sendmail("yashbhatt289@gmail.com",
                "yash.bhatt103501@marwadiuniversity.ac.in",
                "Hey! This is just automation testing.")

server.quit()