#check all the iputs and change according to yours
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Attach the PNG file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path.split('/')[-1]}",
        )
        message.attach(part)

    # Connect to the SMTP server
    with smtplib.SMTP("mail.swechaap.org", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

# Read CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\kondu\\Desktop\\swecha\\QR CODE\\Bootcamp 2023.csv")

# Iterate over rows in the DataFrame
for index, row in df.iterrows():
    sender_email = "sendermail@example.com"
    sender_password = "password"
    receiver_email = row['Email Id']  #'Email','Name', 'Roll' in your CSV
    subject = "Certificate of Participation"
    body = f"Hello {row['NAME']},\n\nWe are happy to have you participating in the BootCamp2023. Your certificate of Participation has been given below attachment.\nThank you for participating in the BootCamp2023, hope you are interested in participating in upcoming events.\n\nFollow us on instagram page to get all updates on SLC Activities. Stay tuned...\n\nTelegram Channel:- https://telegram.me/+MH6E_zC0_MozYmVl?fbclid=PAAaZWXcVki7YUg014nxZNvC219XLyA1SNFmUVsjhVWAdns53cmobYTkc6egQ\n\nThank you and have a great day!\n\nWarm Regards,\nMVGR GLUG\nA Swecha AP Learning Centre"
    attachment_path = f"C:\\Users\\kondu\\Desktop\\swecha\\QR CODE\\BootCamp2023-Certificate\\{row['ROLLO']}.png"
    send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
    print(f"Sent for {row['ROLLO']}")