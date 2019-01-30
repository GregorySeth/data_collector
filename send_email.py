from email.mime.text import MIMEText
import smtplib

try:
    from password import *
except ImportError:
    pass

def send_email(email, sex, name, height, weight, age, average_height, average_weight, average_age, count):

    to_email = email

    subject = "Human data"
    message = "Hey there <strong>%s</strong>, your height is <strong>%s</strong>, your weight is <strong>%s</strong>, and you're <strong>%s</strong> years old. <br> The average values are: <strong>%s</strong> for height, <strong>%s</strong> for weight, and <strong>%s</strong> for age. And that was calculated out of <strong>%s</strong> people.<br> Thank you for your help!" %(name, height, weight, age, average_height, average_weight, average_age, count)

    msg = MIMEText(message, 'html')
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
