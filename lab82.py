import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pradeepselvaraj10t@gmail.com", "@**********")
 
msg = "50 times"
server.sendmail("pradeepselvaraj10t@gmail.com", "johnrohith1731999@gmail.com", msg)
server.quit()
print ("mail sent sucessfully")
