from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from app.database.db import sign_up, sign_in

class AuthWidget(QWidget):
    def __init__(self, on_auth_success):
        super().__init__()
        self.on_auth_success = on_auth_success
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")
        layout.addWidget(self.email_input)

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Sign-in button
        sign_in_button = QPushButton("Sign In", self)
        sign_in_button.clicked.connect(self.handle_sign_in)
        layout.addWidget(sign_in_button)

        # Sign-up button
        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.clicked.connect(self.handle_sign_up)
        layout.addWidget(sign_up_button)

        # Status label
        self.status_label = QLabel(self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def handle_sign_in(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email and password:
            response = sign_in(email, password)
            if response:
                self.on_auth_success()
            else:
                QMessageBox.warning(self, "Error", "Invalid email or password")

    def handle_sign_up(self):
        email = self.email_input.text()
        password = self.password_input.text()

        if email and password:
            response = sign_up(email, password)
            if response:
                QMessageBox.information(self, "Success", "Account created successfully! Please sign in.")
            else:
                QMessageBox.warning(self, "Error", "Failed to create account")