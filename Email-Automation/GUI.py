import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import smtplib, ssl
from credentials import password
import random


def generate_password():
    password = ""
    for i in range(6):
        password += str(random.randint(0, 9))
    return password


class EmailVerificationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Email Verification')
        self.setGeometry(100, 100, 400, 200)

        self.email_label = QLabel('Enter your email address:')
        self.email_input = QLineEdit()
        self.send_button = QPushButton('Send Verification Code')
        self.code_label = QLabel('Enter verification code:')
        self.code_input = QLineEdit()
        self.verify_button = QPushButton('Verify Email')

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.code_label)
        layout.addWidget(self.code_input)
        layout.addWidget(self.verify_button)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_verification_code)
        self.verify_button.clicked.connect(self.verify_email)

        self.code = generate_password()

    def send_verification_code(self):
        email_address = self.email_input.text()
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "awrash.sn@gmail.com"  # Enter your address
        receiver_email = self.email_input  # Enter receiver address

        message = f"""
        Your verification code is {self.code}
        """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print(f"Sent code to {receiver_email}")

    def verify_email(self):
        verification_code = self.code_input.text()
        if verification_code == self.code:
            print("Verification Completed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailVerificationUI()
    window.show()
    sys.exit(app.exec_())
