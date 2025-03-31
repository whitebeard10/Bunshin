from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton,
                             QHBoxLayout, QFrame, QSizePolicy, QScrollArea)
from PyQt6.QtGui import QFont, QColor, QLinearGradient, QBrush, QPalette, QPixmap
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve


class LandingPage(QWidget):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        self.setup_ui()
        self.setup_animations()

    def setup_ui(self):
        # Main layout with scroll area for responsiveness
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Container widget for scroll area
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Layout for container
        container_layout = QVBoxLayout()
        container_layout.setContentsMargins(20, 20, 20, 20)
        container_layout.setSpacing(30)

        # Header Section
        self.setup_header(container_layout)

        # Hero Section
        self.setup_hero_section(container_layout)

        # Features Section
        self.setup_features_section(container_layout)

        # Footer
        self.setup_footer(container_layout)

        container.setLayout(container_layout)
        scroll.setWidget(container)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

        # Set background
        self.set_background()

    def set_background(self):
        # Use gradient background that scales with window
        palette = self.palette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(30, 30, 30))
        gradient.setColorAt(1, QColor(50, 50, 50))
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

    def setup_header(self, layout):
        header = QFrame()
        header.setObjectName("header")
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        # Logo
        logo = QLabel("Productivity Hub")
        logo.setObjectName("logo")
        logo.setFont(QFont("Arial", 20, QFont.Weight.Bold))

        # Spacer
        header_layout.addWidget(logo)
        header_layout.addStretch()

        # Logout button
        logout_btn = QPushButton("Logout")
        logout_btn.setObjectName("logoutButton")
        logout_btn.clicked.connect(self.on_logout)
        header_layout.addWidget(logout_btn)

        header.setLayout(header_layout)
        layout.addWidget(header)

    def setup_hero_section(self, layout):
        hero_frame = QFrame()
        hero_frame.setObjectName("heroFrame")
        hero_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        hero_frame.setMinimumHeight(300)

        hero_layout = QVBoxLayout()
        hero_layout.setContentsMargins(40, 40, 40, 40)

        # Title
        title = QLabel("Welcome to Your Productivity Hub")
        title.setObjectName("heroTitle")
        title.setFont(QFont("Arial", 32, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setWordWrap(True)

        # Subtitle
        subtitle = QLabel("Everything you need in one place")
        subtitle.setObjectName("heroSubtitle")
        subtitle.setFont(QFont("Arial", 18))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hero_layout.addStretch()
        hero_layout.addWidget(title)
        hero_layout.addWidget(subtitle)
        hero_layout.addStretch()

        hero_frame.setLayout(hero_layout)
        layout.addWidget(hero_frame)

    def setup_features_section(self, layout):
        features_frame = QFrame()
        features_frame.setObjectName("featuresFrame")
        features_layout = QVBoxLayout()
        features_layout.setContentsMargins(40, 20, 40, 40)

        # Title
        title = QLabel("Features")
        title.setObjectName("sectionTitle")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Features grid
        grid_layout = QHBoxLayout()
        grid_layout.setSpacing(30)

        features = [
            ("Password Manager", "Securely store all your passwords"),
            ("Task Organizer", "Manage your to-do lists with reminders"),
            ("Idea Board", "Capture and organize your creative ideas"),
            ("Finance Tracker", "Monitor your expenses and budgets")
        ]

        for feature in features:
            card = self.create_feature_card(*feature)
            grid_layout.addWidget(card)

        features_layout.addWidget(title)
        features_layout.addLayout(grid_layout)
        features_frame.setLayout(features_layout)
        layout.addWidget(features_frame)

    def create_feature_card(self, title, description):
        card = QFrame()
        card.setObjectName("featureCard")
        card.setMinimumHeight(200)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel(title)
        title_label.setObjectName("featureTitle")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Description
        desc_label = QLabel(description)
        desc_label.setObjectName("featureDesc")
        desc_label.setFont(QFont("Arial", 14))
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addStretch()

        card.setLayout(layout)
        return card

    def setup_footer(self, layout):
        footer = QFrame()
        footer.setObjectName("footer")
        footer.setFixedHeight(80)

        footer_layout = QHBoxLayout()
        footer_layout.setContentsMargins(20, 20, 20, 20)

        # Copyright
        copyright = QLabel("© 2023 Productivity Hub. All rights reserved.")
        copyright.setObjectName("copyright")

        footer_layout.addWidget(copyright, alignment=Qt.AlignmentFlag.AlignLeft)
        footer_layout.addStretch()

        footer.setLayout(footer_layout)
        layout.addWidget(footer)

    def setup_animations(self):
        # Can add animations for elements if needed
        pass

    def resizeEvent(self, event):
        # Handle responsive behavior
        super().resizeEvent(event)
        self.set_background()