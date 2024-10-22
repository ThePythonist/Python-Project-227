import smtplib, ssl
from credentials import password
import random


def generate_password():
    password = ""
    for i in range(6):
        password += str(random.randint(0, 9))
    return password


def main():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "awrash.sn@gmail.com"  # Enter your address
    receiver_email = "yasnaghavami18@gmail.com"  # Enter receiver address

    code = generate_password()

    message = f"""
    Your verification code is {code}
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    if input(f"Enter verification code sent to {receiver_email} : ") == code:
        print("Successfully logged in")
    else:
        print("Verification code is incorrect. Try again")
        main()


main()
