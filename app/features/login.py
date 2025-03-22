from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.database.db import sign_in

class LoginPage(QWidget):
    def __init__(self, on_login_success, on_go_to_signup, on_go_to_forgot_password):
        super().__init__()
        self.on_login_success = on_login_success
        self.on_go_to_signup = on_go_to_signup
        self.on_go_to_forgot_password = on_go_to_forgot_password
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Login")
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

        # Login button
        login_button = QPushButton("Login", self)
        login_button.setStyleSheet("""
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
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        # Forgot password link
        forgot_password_link = QLabel("<a href='#'>Forgot Password?</a>")
        forgot_password_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        forgot_password_link.setStyleSheet("color: #2a82da; font-size: 14px;")
        forgot_password_link.linkActivated.connect(self.on_go_to_forgot_password)
        layout.addWidget(forgot_password_link)

        # Sign-up link
        signup_link = QLabel("<a href='#'>Don't have an account? Sign Up</a>")
        signup_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        signup_link.setStyleSheet("color: #2a82da; font-size: 14px;")
        signup_link.linkActivated.connect(self.on_go_to_signup)
        layout.addWidget(signup_link)

        self.setLayout(layout)

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email and password:
            response = sign_in(email, password)
            if response:
                self.on_login_success()
            else:
                QMessageBox.warning(self, "Error", "Invalid email or password")