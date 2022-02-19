import smtplib
import imghdr
import sys
from email.message import EmailMessage

#Sends an email with the attached image
#argv[1] - email sender name
#argv[2] - email recipient address

sender_address = "bbrainzproject@gmail.com"
recipient_adress = str(sys.argv[2])
attachment_name = str(sys.argv[1]) + "'s Schedule"


msg = EmailMessage()
msg['Subject'] = "Schedule"
msg['From'] = sender_address
msg['To'] = recipient_adress
msg.set_content("Here is " + attachment_name)

with open('schedule.jpg', 'rb') as pic:
  file_data = pic.read()
  file_type = imghdr.what(pic.name)

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=attachment_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(sender_address, 'sktelxvlvclhfblx')

  smtp.send_message(msg)