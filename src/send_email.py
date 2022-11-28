import smtplib
import sys

SENDER_EMAIL = 'ruben.g1293@gmail.com'
SENDER_PASSWORD = 'ulkkbsslokbkmwqs'

def send_email(receiver_email, subject, body):
    message= 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

if __name__ == '__main__':
    send_email(sys.argv[1], sys.argv[2], sys.argv[3])