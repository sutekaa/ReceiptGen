{\rtf1\ansi\ansicpg1250\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import smtplib\
from email.mime.multipart import MIMEMultipart\
from email.mime.text import MIMEText\
from email.mime.base import MIMEBase\
from email import encoders\
import os\
\
def send_email(subject, body, recipient_email, attachment_path):\
    msg = MIMEMultipart()\
    msg['From'] = os.getenv('EMAIL_ADDRESS')\
    msg['To'] = recipient_email\
    msg['Subject'] = subject\
\
    msg.attach(MIMEText(body, 'plain'))\
\
    if attachment_path:\
        attach_file = open(attachment_path, "rb")\
        part = MIMEBase('application', 'octet-stream')\
        part.set_payload(attach_file.read())\
        encoders.encode_base64(part)\
        part.add_header('Content-Disposition', 'attachment; filename= "receipt.png"')\
        msg.attach(part)\
\
    try:\
        server = smtplib.SMTP('smtp.gmail.com', 587)\
        server.starttls()\
        server.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))\
        text = msg.as_string()\
        server.sendmail(os.getenv('EMAIL_ADDRESS'), recipient_email, text)\
        server.quit()\
    except Exception as e:\
        print(f"Error sending email: \{e\}")\
}