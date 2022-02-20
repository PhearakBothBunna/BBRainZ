import smtplib
import sys
import imghdr
from email.message import EmailMessage
from email.utils import make_msgid

#Sends an email with the attached image
#argv[1] - student name
#argv[2] - student ID
#argv[3] - student address
#argv[4] - advisor address

FILE_NAME = 'schedule.jpg'

sender_address = "bbrainzproject@gmail.com"
recipient_address = str(sys.argv[4]) + ", " + str(sys.argv[3])
attachment_name = str(sys.argv[1]) + "'s Schedule"
student_id = str(sys.argv[2])

msg = EmailMessage()
msg['To'] = recipient_address
msg['From'] = sender_address
msg['Subject'] = "Schedule"

attachment_cid = make_msgid()

msg.set_content("""\
<!DOCTYPE html>
<html>
  <h1>%s</h1>
  <h2>%s</h2>
  <body>
    <img src='cid:%s' alt="Schedule">
  </body>
</html>
""" % (attachment_name, student_id, attachment_cid[1:-1]), 'html')

with open(FILE_NAME, 'rb') as img:
  file_data = img.read()
  file_type = imghdr.what(img.name)

  msg.add_related(
    file_data, 'image', file_type, cid=attachment_cid)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(sender_address, 'sktelxvlvclhfblx')

  smtp.send_message(msg)