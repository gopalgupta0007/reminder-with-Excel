import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
status_code, response=server.ehlo()
print(f"these is ehlo >>>>> {status_code} and {response}")
status_codetls, responsetls=server.starttls()
print(f"these is starttls >>>>> {status_codetls} and {responsetls}")
subject="sending email using python"
body="this is mail are sending through python smtp"
message = "Subject : {}\n\n{}".format(subject, body)
try:
    status_codel, responsel=server.login('guptagopal18082003@gmail.com', 'bwmczqycwmydrddq')
    print("Login successful")
    print(f"these is login >>>>>  {status_codel} and {responsel}")
    server.sendmail('guptagopal18082003@gmail.com', ['vg870779@gmail.com', 'vg660856@gmail.com'], message)
    print("mail sended")
except smtplib.SMTPAuthenticationError as e:
    print(f"Login failed: {e}")
finally:
    server.quit()