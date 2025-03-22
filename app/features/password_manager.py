from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout
from app.database.db import add_password, get_passwords

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Input fields with labels
        form_layout = QFormLayout()
        self.website_input = QLineEdit(self)
        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        form_layout.addRow("Website:", self.website_input)
        form_layout.addRow("Username:", self.username_input)
        form_layout.addRow("Password:", self.password_input)

        # Add button
        add_button = QPushButton("Add Password", self)
        add_button.clicked.connect(self.add_password)

        # Table to display passwords
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Website", "Username", "Password"])
        self.load_passwords()

        # Add widgets to layout
        layout.addLayout(form_layout)
        layout.addWidget(add_button)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_password(self):
        website = self.website_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if website and username and password:
            add_password(website, username, password)
            self.load_passwords()

    def load_passwords(self):
        passwords = get_passwords()
        self.table.setRowCount(len(passwords))
        for i, row in enumerate(passwords):
            self.table.setItem(i, 0, QTableWidgetItem(row["website"]))
            self.table.setItem(i, 1, QTableWidgetItem(row["username"]))
            self.table.setItem(i, 2, QTableWidgetItem(row["password"]))