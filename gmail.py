import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_gmail(bname,name,phone):
    gmail_username = 'test@gmail.com'
    gmail_password = 'testPAss'

    recipient_email = 'recipient_email@gmail.com'

    subject = f'Book {bname} ordered'
    body = f'book {bname} was ordered by {name}, phone no.{phone}, operation : issue'
    message = MIMEMultipart()
    message['From'] = gmail_username
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_username, gmail_password)

    try:
        server.sendmail(gmail_username, recipient_email, message.as_string())
        #print("Email sent successfully!")
    except Exception as e:
        print(f"Failed please try again later: {str(e)}")
    finally:
        server.quit()
