# newotp.py
import random
import smtplib
from email.message import EmailMessage


def generate_otp(length=6):
    """
    Generate a random OTP of the specified length.
    :param length: Length of the OTP (default is 6).
    :return: A string containing the OTP.
    """
    if length <= 0:
        raise ValueError("OTP length must be a positive integer.")
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def send_otp_email(otp, from_mail, app_password, to_mail):
    """
    Send an OTP email to the specified recipient.
    :param otp: The OTP to send.
    :param from_mail: Sender's email address.
    :param app_password: The sender's app password.
    :param to_mail: Recipient's email address.
    :return: True if the email is sent successfully, False otherwise.
    """
    try:
        # Setup SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_mail, app_password)

        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = "OTP Verification"
        msg['From'] = from_mail
        msg['To'] = to_mail
        msg.set_content(f"Your OTP is: {otp}")

        # Send the email
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
