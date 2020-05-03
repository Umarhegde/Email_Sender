import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Umar Hegde'
email['to'] = '<to email address >
email['subject'] = 'Email Subject'

email.set_content(html.substitute({'name': '-'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<your email address>', '<your password>')
    smtp.send_message(email)
    print('all good boss!')
