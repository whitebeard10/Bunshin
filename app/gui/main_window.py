from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from app.features.login import LoginPage
from app.features.signup import SignUpPage
from app.features.forgot_password import ForgotPasswordPage
from app.features.password_manager import PasswordManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Desktop App")
        self.setGeometry(100, 100, 800, 600)

        # Stacked widget to switch between pages
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Login page
        self.login_page = LoginPage(
            on_login_success=self.show_password_manager,
            on_go_to_signup=self.show_signup,
            on_go_to_forgot_password=self.show_forgot_password
        )
        self.stacked_widget.addWidget(self.login_page)

        # Sign-up page
        self.signup_page = SignUpPage(
            on_signup_success=self.show_login,
            on_go_to_login=self.show_login
        )
        self.stacked_widget.addWidget(self.signup_page)

        # Forgot password page
        self.forgot_password_page = ForgotPasswordPage(
            on_go_to_login=self.show_login
        )
        self.stacked_widget.addWidget(self.forgot_password_page)

        # Password manager page
        self.password_manager = PasswordManager()
        self.stacked_widget.addWidget(self.password_manager)

        # Show login page by default
        self.stacked_widget.setCurrentWidget(self.login_page)

    def show_login(self):
        self.stacked_widget.setCurrentWidget(self.login_page)

    def show_signup(self):
        self.stacked_widget.setCurrentWidget(self.signup_page)

    def show_forgot_password(self):
        self.stacked_widget.setCurrentWidget(self.forgot_password_page)

    def show_password_manager(self):
        self.stacked_widget.setCurrentWidget(self.password_manager)