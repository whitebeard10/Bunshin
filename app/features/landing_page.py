from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt6.QtGui import QFont, QColor, QLinearGradient, QBrush, QPalette
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve

class LandingPage(QWidget):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        self.setup_ui()

    def setup_ui(self):
        # Set up the main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(30)
        self.setLayout(layout)

        # Apply a gradient background
        self.set_gradient_background()

        # Hero Section
        self.setup_hero_section(layout)

        # Features Section
        self.setup_features_section(layout)

        # Footer
        self.setup_footer(layout)

        # Logout button
        logout_button = QPushButton("Logout", self)
        logout_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4d4d;
                color: white;
                padding: 10px;
                font-size: 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        logout_button.clicked.connect(self.on_logout)
        layout.addWidget(logout_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def set_gradient_background(self):
        # Create a gradient background
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(30, 30, 30))  # Dark gray
        gradient.setColorAt(1, QColor(50, 50, 50))  # Lighter gray

        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

    def setup_hero_section(self, layout):
        # Hero Title
        hero_title = QLabel("Your Personal Productivity Hub")
        hero_title.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        hero_title.setStyleSheet("color: white;")
        hero_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hero_title)

        # Hero Subtitle
        hero_subtitle = QLabel("Manage passwords, tasks, and ideas in one place.")
        hero_subtitle.setFont(QFont("Arial", 18))
        hero_subtitle.setStyleSheet("color: #AAAAAA;")
        hero_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(hero_subtitle)

    def setup_features_section(self, layout):
        # Features Title
        features_title = QLabel("Features")
        features_title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        features_title.setStyleSheet("color: white;")
        features_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(features_title)

        # Features Cards
        features_layout = QHBoxLayout()
        features_layout.setSpacing(20)

        # Feature 1: Password Manager
        feature1 = self.create_feature_card("Password Manager", "Securely store and manage your passwords.")
        features_layout.addWidget(feature1)

        # Feature 2: To-Do List
        feature2 = self.create_feature_card("To-Do List", "Organize tasks with reminders and priorities.")
        features_layout.addWidget(feature2)

        # Feature 3: Idea Storage
        feature3 = self.create_feature_card("Idea Storage", "Save and revisit creative ideas with reminders.")
        features_layout.addWidget(feature3)

        layout.addLayout(features_layout)

    def create_feature_card(self, title, description):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #404040;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        card.setFixedSize(300, 200)

        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Feature Title
        feature_title = QLabel(title)
        feature_title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        feature_title.setStyleSheet("color: white;")
        card_layout.addWidget(feature_title)

        # Feature Description
        feature_description = QLabel(description)
        feature_description.setFont(QFont("Arial", 14))
        feature_description.setStyleSheet("color: #AAAAAA;")
        feature_description.setWordWrap(True)
        feature_description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.addWidget(feature_description)

        card.setLayout(card_layout)
        return card

    def setup_footer(self, layout):
        footer = QFrame()
        footer.setStyleSheet("background-color: #2a82da; padding: 20px;")

        footer_layout = QHBoxLayout()
        footer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Footer Links
        social_links = ["GitHub", "Twitter", "Privacy Policy", "Terms of Service"]
        for link in social_links:
            footer_link = QLabel(f"<a href='#' style='color: white; text-decoration: none;'>{link}</a>")
            footer_link.setFont(QFont("Arial", 12))
            footer_link.setOpenExternalLinks(True)
            footer_layout.addWidget(footer_link)

        footer.setLayout(footer_layout)
        layout.addWidget(footer)