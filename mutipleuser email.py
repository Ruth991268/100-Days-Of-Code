import smtplib
email=input("Enter your email: ")
subject=input("Enter subject: ")
message=input("Enter message: ")
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,"")#Enter your app password here
more_user="yes"
while more_user=="yes":
    recever_email=input("Enter recever email: ")
   
    
    text=f"Subject: {subject}\n\n{message}"
    server.sendmail(email,recever_email,text)
    print("Email sent successfully")
    more_user=input("Do you want to send more email? Type 'yes' or 'no': ").lower()
if more_user == "no":
        print("👋 Exiting... Goodbye!")
       
server.quit()    