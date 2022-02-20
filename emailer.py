import smtplib
import sys
from email.message import EmailMessage
from email.utils import make_msgid

#Sends an email with the attached image
#argv[1] - email sender name
#argv[2] - email sender address
#argv[2] - email recipient address

sender_address = "bbrainzproject@gmail.com"
recipient_address = str(sys.argv[3]) #+ ", " + str(sys.argv[2])
attachment_name = str(sys.argv[1]) + "'s Schedule"


msg = EmailMessage()
msg['To'] = recipient_address
msg['From'] = sender_address
msg['Subject'] = "Schedule"

attachment_cid = make_msgid()

msg.set_content("""\
<!DOCTYPE html>
<html>
  <h1>%s</h1>
  <body>
    <img src='cid:%s' alt="Schedule">
  </body>
</html>
""" % (attachment_name, attachment_cid[1:-1]), 'html')

with open('schedule.jpg', 'rb') as img:
  msg.add_related(
    img.read(), 'image', 'jpeg', cid=attachment_cid)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(sender_address, 'sktelxvlvclhfblx')

  smtp.send_message(msg)