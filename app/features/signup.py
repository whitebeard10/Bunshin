from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.database.db import sign_up

class SignUpPage(QWidget):
    def __init__(self, on_signup_success, on_go_to_login):
        super().__init__()
        self.on_signup_success = on_signup_success
        self.on_go_to_login = on_go_to_login
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Sign Up")
        title.setFont(QFont("Arial", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.email_input)

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.password_input)

        # Sign-up button
        signup_button = QPushButton("Sign Up", self)
        signup_button.setStyleSheet("""
            QPushButton {
                background-color: #2a82da;
                color: white;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1c5a9b;
            }
        """)
        signup_button.clicked.connect(self.handle_signup)
        layout.addWidget(signup_button)

        # Sign-in link
        signin_link = QLabel("<a href='#'>Already have an account? Sign In</a>")
        signin_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        signin_link.setStyleSheet("color: #2a82da; font-size: 14px;")
        signin_link.linkActivated.connect(self.on_go_to_login)
        layout.addWidget(signin_link)

        self.setLayout(layout)

    def handle_signup(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email and password:
            response = sign_up(email, password)
            if response:
                QMessageBox.information(self, "Success", "Account created successfully! Please sign in.")
                self.on_signup_success()
            else:
                QMessageBox.warning(self, "Error", "Failed to create account")