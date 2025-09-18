import smtplib
email=input("Enter your email: ")
recever_email=input("Enter recever email: ")
subject=input("Enter subject: ")
message=input("Enter message: ")
text=f"Subject: {subject}\n\n{message}"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,"szdp ypnq ifpm qrch")
server.sendmail(email,recever_email,text)
print("Email sent successfully")