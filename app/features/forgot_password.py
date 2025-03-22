from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.database.db import reset_password

class ForgotPasswordPage(QWidget):
    def __init__(self, on_go_to_login):
        super().__init__()
        self.on_go_to_login = on_go_to_login
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Forgot Password")
        title.setFont(QFont("Arial", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.email_input)

        # Reset button
        reset_button = QPushButton("Reset Password", self)
        reset_button.setStyleSheet("""
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
        reset_button.clicked.connect(self.handle_reset)
        layout.addWidget(reset_button)

        # Sign-in link
        signin_link = QLabel("<a href='#'>Back to Sign In</a>")
        signin_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        signin_link.setStyleSheet("color: #2a82da; font-size: 14px;")
        signin_link.linkActivated.connect(self.on_go_to_login)
        layout.addWidget(signin_link)

        self.setLayout(layout)

    def handle_reset(self):
        email = self.email_input.text()
        if email:
            response = reset_password(email)
            if response:
                QMessageBox.information(self, "Success", "Password reset email sent!")
            else:
                QMessageBox.warning(self, "Error", "Failed to send reset email")