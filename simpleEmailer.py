import smtplib
from email.mime.text import MIMEText

class SimpleEmailer:
	def __init__(self, smtp_user, smtp_pass):
		self.smtp_user = smtp_user
		self.smtp_pass = smtp_pass
	
	def send(self, msg, subject, fromEmail, toEmail):
		m = MIMEText(msg)
		m['Subject'] = subject
		m['To'] = toEmail
		m['From'] = fromEmail
		
		s = smtplib.SMTP('smtp.sendgrid.net')
		s.login(self.smtp_user, self.smtp_pass)
		s.send_message(m)
		s.quit()
		
if __name__ == "__main__":
	import sys
	if len(sys.argv) == 3:
		se = SimpleEmailer(sys.argv[1],sys.argv[2])
		se.send("Hello World, this is an email!", "Hello World", "pi@reboot.com.au", "james.wassink@gmail.com")
	else:
		print("Wrong number of arguments - usage is \"simpleEmailer.py <smtp_user> <smtp_pass>\"")
