import smtplib
import os
from email.mime.multipart import MIMEMultipart
import sys
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

def send_email(From = 'your_gmail@gmail.com',To = 'xxx@xxx.com',passward = 'xxx',
               Subject = 'subject', text = None,attachment= None):
    '''
    attachment is a list of path
    '''
    
    outer = MIMEMultipart()
    outer['Subject'] = Subject
    outer['To'] = To
    outer['From'] = From
    if text is not None:
        outer.attach(MIMEText(text, 'plain')) # or 'html'

    if attachment is not None:
        for file in attachment:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise
    composed = outer.as_string()
    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com')
        s.ehlo()
        s.login(From, passward)
        s.sendmail(From, To, composed)
        s.close()
        print("Email sent!")
        # with smtplib.SMTP_SSL('smtp.gmail.com') as s:
            # s.ehlo()
            # # s.starttls()
            # s.ehlo()
            # s.login(From, passward)
            # s.sendmail(From, To, composed)
            # s.close()
            # print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


