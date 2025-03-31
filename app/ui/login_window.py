from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel,
                             QLineEdit, QPushButton, QStackedWidget, QFrame,
                             QHBoxLayout)
from PyQt6.QtGui import (QPixmap, QFont, QColor, QPalette, QBrush,
                         QIcon, QPainter, QLinearGradient)
from PyQt6.QtCore import (Qt, QPropertyAnimation, QPoint, QSize)
from app.core.auth import login, signup, forgot_password
from app.core.utils import FadeAnimation, SlideAnimation, load_stylesheet
import os


class LoginWindow(QMainWindow):
    def __init__(self, on_login_success=None):
        super().__init__()
        self.on_login_success = on_login_success
        self.dark_mode = True
        self.setup_ui()
        self.setup_animations()
        self.setup_icons()

    def setup_ui(self):
        self.setWindowTitle("Productivity Hub - Auth")
        self.setFixedSize(1000, 700)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(main_layout)

        # Left side (branding)
        self.setup_branding_side(main_layout)

        # Right side (forms)
        self.setup_forms_side(main_layout)

        # Theme toggle
        self.setup_theme_toggle()

    def setup_branding_side(self, parent_layout):
        branding_frame = QFrame()
        branding_frame.setObjectName("brandingFrame")
        branding_layout = QVBoxLayout()

        # Logo
        logo = QLabel("Productivity Hub")
        logo.setObjectName("brandLogo")
        logo.setFont(QFont("Arial", 24, QFont.Weight.Bold))

        # Tagline
        tagline = QLabel("Your all-in-one productivity solution")
        tagline.setObjectName("brandTagline")
        tagline.setFont(QFont("Arial", 14))

        branding_layout.addStretch()
        branding_layout.addWidget(logo, alignment=Qt.AlignmentFlag.AlignCenter)
        branding_layout.addWidget(tagline, alignment=Qt.AlignmentFlag.AlignCenter)
        branding_layout.addStretch()

        branding_frame.setLayout(branding_layout)
        parent_layout.addWidget(branding_frame, stretch=1)

    def setup_forms_side(self, parent_layout):
        forms_frame = QFrame()
        forms_frame.setObjectName("formsFrame")

        # Stacked widgets for forms
        self.stack = QStackedWidget()
        self.setup_login_form()
        self.setup_signup_form()
        self.setup_forgot_form()

        forms_layout = QVBoxLayout()
        forms_layout.addWidget(self.stack)
        forms_frame.setLayout(forms_layout)
        parent_layout.addWidget(forms_frame, stretch=1)

        # Apply CSS
        self.update_styles()

    def setup_login_form(self):
        form = QFrame()
        form.setObjectName("authForm")
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)

        # Title
        title = QLabel("Welcome Back")
        title.setObjectName("formTitle")

        # Email field
        email_layout = QHBoxLayout()
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email address")
        self.email_input.setObjectName("authInput")
        self.email_icon = QLabel()
        email_layout.addWidget(self.email_icon)
        email_layout.addWidget(self.email_input)

        # Password field
        password_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("authInput")
        self.password_icon = QLabel()
        password_layout.addWidget(self.password_icon)
        password_layout.addWidget(self.password_input)

        # Login button
        login_btn = QPushButton("Login")
        login_btn.setObjectName("primaryButton")
        login_btn.clicked.connect(self.handle_login)

        # Links
        links_layout = QHBoxLayout()
        signup_link = QPushButton("Create account")
        signup_link.setObjectName("textButton")
        signup_link.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        forgot_link = QPushButton("Forgot password?")
        forgot_link.setObjectName("textButton")
        forgot_link.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        links_layout.addWidget(signup_link)
        links_layout.addWidget(forgot_link)

        # Add to layout
        layout.addWidget(title)
        layout.addLayout(email_layout)
        layout.addLayout(password_layout)
        layout.addWidget(login_btn)
        layout.addLayout(links_layout)
        form.setLayout(layout)
        self.stack.addWidget(form)

    def setup_signup_form(self):
        form = QFrame()
        form.setObjectName("authForm")
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)

        # Title
        title = QLabel("Create Account")
        title.setObjectName("formTitle")

        # Name field
        name_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full name")
        self.name_input.setObjectName("authInput")
        self.name_icon = QLabel()
        name_layout.addWidget(self.name_icon)
        name_layout.addWidget(self.name_input)

        # Email field
        email_layout = QHBoxLayout()
        self.signup_email_input = QLineEdit()
        self.signup_email_input.setPlaceholderText("Email address")
        self.signup_email_input.setObjectName("authInput")
        self.signup_email_icon = QLabel()
        email_layout.addWidget(self.signup_email_icon)
        email_layout.addWidget(self.signup_email_input)

        # Password field
        password_layout = QHBoxLayout()
        self.signup_password_input = QLineEdit()
        self.signup_password_input.setPlaceholderText("Password")
        self.signup_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_password_input.setObjectName("authInput")
        self.signup_password_icon = QLabel()
        password_layout.addWidget(self.signup_password_icon)
        password_layout.addWidget(self.signup_password_input)

        # Confirm Password field
        confirm_layout = QHBoxLayout()
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setObjectName("authInput")
        self.confirm_password_icon = QLabel()
        confirm_layout.addWidget(self.confirm_password_icon)
        confirm_layout.addWidget(self.confirm_password_input)

        # Signup button
        signup_btn = QPushButton("Create Account")
        signup_btn.setObjectName("primaryButton")
        signup_btn.clicked.connect(self.handle_signup)

        # Links
        links_layout = QHBoxLayout()
        login_link = QPushButton("Already have an account? Login")
        login_link.setObjectName("textButton")
        login_link.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        links_layout.addWidget(login_link)

        # Add to layout
        layout.addWidget(title)
        layout.addLayout(name_layout)
        layout.addLayout(email_layout)
        layout.addLayout(password_layout)
        layout.addLayout(confirm_layout)
        layout.addWidget(signup_btn)
        layout.addLayout(links_layout)
        form.setLayout(layout)
        self.stack.addWidget(form)

        # Set icons
        user_icon = os.path.join("app", "ui", "assets", "icons", "user.svg")
        if os.path.exists(user_icon):
            self.name_icon.setPixmap(QPixmap(user_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))
        if hasattr(self, 'signup_email_icon'):
            email_icon = os.path.join("app", "ui", "assets", "icons", "mail.svg")
            if os.path.exists(email_icon):
                self.signup_email_icon.setPixmap(QPixmap(email_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))
        if hasattr(self, 'signup_password_icon'):
            lock_icon = os.path.join("app", "ui", "assets", "icons", "lock.svg")
            if os.path.exists(lock_icon):
                self.signup_password_icon.setPixmap(
                    QPixmap(lock_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))
                self.confirm_password_icon.setPixmap(
                    QPixmap(lock_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))

    def setup_forgot_form(self):
        form = QFrame()
        form.setObjectName("authForm")
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)

        # Title
        title = QLabel("Reset Password")
        title.setObjectName("formTitle")

        # Instructions
        instructions = QLabel("Enter your email to receive a password reset link")
        instructions.setObjectName("formSubtitle")
        instructions.setWordWrap(True)

        # Email field
        email_layout = QHBoxLayout()
        self.forgot_email_input = QLineEdit()
        self.forgot_email_input.setPlaceholderText("Email address")
        self.forgot_email_input.setObjectName("authInput")
        self.forgot_email_icon = QLabel()
        email_layout.addWidget(self.forgot_email_icon)
        email_layout.addWidget(self.forgot_email_input)

        # Submit button
        submit_btn = QPushButton("Send Reset Link")
        submit_btn.setObjectName("primaryButton")
        submit_btn.clicked.connect(self.handle_forgot_password)

        # Links
        links_layout = QHBoxLayout()
        login_link = QPushButton("Remember your password? Login")
        login_link.setObjectName("textButton")
        login_link.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        links_layout.addWidget(login_link)

        # Add to layout
        layout.addWidget(title)
        layout.addWidget(instructions)
        layout.addLayout(email_layout)
        layout.addWidget(submit_btn)
        layout.addLayout(links_layout)
        form.setLayout(layout)
        self.stack.addWidget(form)

        # Set icon
        email_icon = os.path.join("app", "ui", "assets", "icons", "mail.svg")
        if os.path.exists(email_icon):
            self.forgot_email_icon.setPixmap(QPixmap(email_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))

    def handle_signup(self):
        name = self.name_input.text()
        email = self.signup_email_input.text()
        password = self.signup_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if password != confirm_password:
            self.show_error("Passwords don't match!")
            return

        if signup(email, password):
            self.show_success("Account created successfully!")
            self.stack.setCurrentIndex(0)  # Return to login

    def handle_forgot_password(self):
        email = self.forgot_email_input.text()
        if forgot_password(email):
            self.show_success("Password reset link sent to your email")
            self.stack.setCurrentIndex(0)  # Return to login

    def show_error(self, message):
        error_label = QLabel(message)
        error_label.setObjectName("errorMessage")
        # Add to layout temporarily
        # In production, you'd want a more sophisticated notification system

    def show_success(self, message):
        success_label = QLabel(message)
        success_label.setObjectName("successMessage")
        # Add to layout temporarily

    def setup_icons(self):
        # Set icons for input fields
        icon_path = os.path.join("app", "ui", "assets", "icons")

        # Email icon
        email_icon = os.path.join(icon_path, "mail.svg")
        if os.path.exists(email_icon):
            self.email_icon.setPixmap(QPixmap(email_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))

        # Password icon
        password_icon = os.path.join(icon_path, "lock.svg")
        if os.path.exists(password_icon):
            self.password_icon.setPixmap(QPixmap(password_icon).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio))

    def setup_theme_toggle(self):
        self.theme_toggle = QPushButton()
        self.theme_toggle.setObjectName("themeToggle")
        self.theme_toggle.setFixedSize(40, 40)
        self.theme_toggle.clicked.connect(self.toggle_theme)

        # Position toggle
        self.theme_toggle.move(self.width() - 50, 20)
        self.update_theme_icon()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.update_styles()
        self.update_theme_icon()

    def update_theme_icon(self):
        icon = "moon.svg" if self.dark_mode else "sun.svg"
        icon_path = os.path.join("app", "ui", "assets", "icons", icon)
        if os.path.exists(icon_path):
            self.theme_toggle.setIcon(QIcon(icon_path))
            self.theme_toggle.setIconSize(QSize(20, 20))

    def update_styles(self):
        css_path = os.path.join("app", "ui", "styles", "login.css")
        base_style = load_stylesheet(css_path)

        # Add theme variant
        theme_suffix = "dark" if self.dark_mode else "light"
        theme_style = f"""
            #brandingFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 {'#1a1a2e' if self.dark_mode else '#f5f7fa'}, 
                    stop:1 {'#16213e' if self.dark_mode else '#c3cfe2'});
            }}
            #formsFrame {{
                background: {'#121212' if self.dark_mode else '#ffffff'};
            }}
        """
        self.setStyleSheet(base_style + theme_style)

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        if login(email, password):
            self.fade_out()
            if self.on_login_success:
                self.on_login_success()

    def fade_out(self):
        animation = FadeAnimation.fade_out(self)
        animation.finished.connect(self.close)

    def setup_animations(self):
        # Animate form entry
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            widget.setGraphicsEffect(None)
            anim = SlideAnimation.slide_from_right(widget, 800)
            anim.start()