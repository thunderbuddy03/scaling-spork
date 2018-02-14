import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pradeepselvaraj10t@gmail.com", "@selvaraj10t")
 
msg = "hey how are you"
server.sendmail("pradeepselvaraj10t@gmail.com", "nithind7026@gmail.com", msg)
server.quit()
