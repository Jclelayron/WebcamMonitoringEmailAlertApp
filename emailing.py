import smtplib
import imghdr
from email.message import EmailMessage
import os

password = os.getenv("PASSWORD")
email = os.getenv("USER")
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showerd up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email,password)
    gmail.sendmail(email, email, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email("images/20.png")

