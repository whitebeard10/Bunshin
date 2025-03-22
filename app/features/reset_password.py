from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.database.db import update_password

class ResetPasswordPage(QWidget):
    def __init__(self, on_password_updated):
        super().__init__()
        self.on_password_updated = on_password_updated
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Reset Password")
        title.setFont(QFont("Arial", 24))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # New password input
        self.new_password_input = QLineEdit(self)
        self.new_password_input.setPlaceholderText("New Password")
        self.new_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.new_password_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.new_password_input)

        # Confirm password input
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setStyleSheet("padding: 10px; font-size: 16px;")
        layout.addWidget(self.confirm_password_input)

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

        self.setLayout(layout)

    def handle_reset(self):
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if new_password and confirm_password:
            if new_password == confirm_password:
                response = update_password(new_password)
                if response:
                    QMessageBox.information(self, "Success", "Password updated successfully!")
                    self.on_password_updated()
                else:
                    QMessageBox.warning(self, "Error", "Failed to update password")
            else:
                QMessageBox.warning(self, "Error", "Passwords do not match")