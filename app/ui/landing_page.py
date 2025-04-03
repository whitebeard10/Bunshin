from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QPushButton,
                             QHBoxLayout, QFrame, QSizePolicy, QGridLayout,
                             QScrollArea, QStackedLayout)
from PyQt6.QtGui import (QFont, QColor, QLinearGradient, QBrush,
                         QPalette, QPixmap, QPainter, QFontMetrics)
from PyQt6.QtCore import (Qt, QPropertyAnimation, QEasingCurve,
                          QParallelAnimationGroup, QSequentialAnimationGroup,
                          QPoint, QTimer, QSize, QRect)


class LandingPage(QWidget):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        self.min_width = 320  # Minimum width for mobile screens

        # Set an initial size
        self.setMinimumSize(800, 600)

        self.setup_ui()
        self.setup_animations()

        # Connect resize event to handle responsiveness
        self.resizeEvent = self.on_resize

    def setup_ui(self):
        # Create a scroll area to handle small screens
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Create container widget for scroll area
        self.container = QWidget()
        self.scroll_area.setWidget(self.container)

        # Main layout with spacing and margins
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Container layout with more generous spacing
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(20, 30, 20, 30)  # Reduced margins
        self.container_layout.setSpacing(50)  # More space between sections

        # Set main layout
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        # Apply modern gradient background
        self.set_gradient_background()

        # Header with logo and navigation
        self.setup_header(self.container_layout)

        # Hero section with animated welcome
        self.setup_hero_section(self.container_layout)

        # Features section with interactive cards
        self.setup_features_section(self.container_layout)

        # Call-to-action section
        self.setup_cta_section(self.container_layout)

        # Footer with links and copyright
        self.setup_footer(self.container_layout)

    def set_gradient_background(self):
        # Modern gradient from dark blue to purple
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(15, 32, 65))  # Dark blue
        gradient.setColorAt(1, QColor(65, 15, 65))  # Purple

        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)
        self.container.setPalette(palette)

    def setup_header(self, layout):
        self.header = QFrame()
        self.header_layout = QHBoxLayout(self.header)
        self.header_layout.setContentsMargins(10, 10, 10, 10)  # More padding

        # Logo with adaptive sizing
        self.logo = QLabel("Productivity Hub")
        self.logo.setFont(QFont("Arial", 18, QFont.Weight.Bold))  # Smaller initial font
        self.logo.setStyleSheet("color: white;")
        self.logo.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.logo.setMinimumWidth(150)

        # Navigation buttons in a layout for responsiveness
        self.nav_layout = QHBoxLayout()
        self.nav_layout.setSpacing(15)  # More space between buttons
        self.nav_buttons = []
        nav_texts = ["Features", "Pricing", "About", "Contact"]

        for btn_text in nav_texts:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                QPushButton {
                    color: white;
                    background: transparent;
                    border: none;
                    padding: 10px 15px;  /* More padding */
                    font-size: 14px;
                }
                QPushButton:hover {
                    color: #2a82da;
                }
            """)
            self.nav_buttons.append(btn)
            self.nav_layout.addWidget(btn)

        # Menu button for mobile (initially hidden)
        self.menu_btn = QPushButton("☰")
        self.menu_btn.setStyleSheet("""
            QPushButton {
                color: white;
                background: transparent;
                border: none;
                font-size: 28px;  /* Larger hamburger icon */
                padding: 8px;
            }
            QPushButton:hover {
                color: #2a82da;
            }
        """)
        self.menu_btn.setVisible(False)
        self.menu_btn.clicked.connect(self.toggle_mobile_menu)

        self.header_layout.addWidget(self.logo)
        self.header_layout.addStretch()
        self.header_layout.addLayout(self.nav_layout)
        self.header_layout.addWidget(self.menu_btn)

        # Add header to main layout with fixed height
        self.header.setFixedHeight(70)  # Fixed height for header
        layout.addWidget(self.header)

        # Mobile menu with better styling
        self.mobile_menu = QFrame()
        self.mobile_menu.setStyleSheet("""
            QFrame {
                background-color: rgba(15, 32, 65, 0.95);
                border-radius: 10px;
                margin: 0px 10px;
            }
        """)
        self.mobile_menu.setVisible(False)
        self.mobile_menu.setFixedHeight(200)  # Fixed height for menu

        mobile_menu_layout = QVBoxLayout(self.mobile_menu)
        mobile_menu_layout.setSpacing(5)

        for btn_text in nav_texts:
            btn = QPushButton(btn_text)
            btn.setStyleSheet("""
                QPushButton {
                    color: white;
                    background: transparent;
                    border: none;
                    padding: 12px;
                    font-size: 16px;
                    text-align: center;
                }
                QPushButton:hover {
                    color: #2a82da;
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 5px;
                }
            """)
            mobile_menu_layout.addWidget(btn)

        layout.addWidget(self.mobile_menu)

    def toggle_mobile_menu(self):
        self.mobile_menu.setVisible(not self.mobile_menu.isVisible())

    def setup_hero_section(self, layout):
        hero_frame = QFrame()
        hero_layout = QVBoxLayout(hero_frame)
        hero_layout.setContentsMargins(15, 30, 15, 30)  # More padding
        hero_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hero_layout.setSpacing(25)  # More spacing

        # Main title with animation
        self.hero_title = QLabel("Your Personal Productivity Hub")
        self.hero_title.setFont(QFont("Arial", 32, QFont.Weight.Bold))  # Slightly smaller
        self.hero_title.setStyleSheet("color: white;")
        self.hero_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hero_title.setWordWrap(True)
        self.hero_title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        # Enforce minimum height for title
        self.hero_title.setMinimumHeight(80)

        # Subtitle
        self.hero_subtitle = QLabel("Everything you need to stay organized and productive")
        self.hero_subtitle.setFont(QFont("Arial", 16))  # Slightly smaller
        self.hero_subtitle.setStyleSheet("color: rgba(255, 255, 255, 0.8);")  # More visible
        self.hero_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hero_subtitle.setWordWrap(True)
        self.hero_subtitle.setMinimumHeight(50)  # Ensure subtitle has enough space

        # Get Started button
        self.get_started_btn = QPushButton("Explore Features")
        self.get_started_btn.setStyleSheet("""
            QPushButton {
                background-color: #2a82da;
                color: white;
                padding: 12px 25px;
                font-size: 16px;
                border-radius: 25px;
                min-width: 180px;
            }
            QPushButton:hover {
                background-color: #1a6bb0;
            }
        """)
        self.get_started_btn.setFixedSize(200, 50)  # Fixed size button for consistency

        # Add widgets to layout with proper alignment
        hero_layout.addWidget(self.hero_title)
        hero_layout.addWidget(self.hero_subtitle)
        hero_layout.addWidget(self.get_started_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # Set a minimum height for the hero section
        hero_frame.setMinimumHeight(250)
        layout.addWidget(hero_frame)

    def setup_features_section(self, layout):
        features_frame = QFrame()
        self.features_layout = QVBoxLayout(features_frame)
        self.features_layout.setContentsMargins(15, 20, 15, 20)
        self.features_layout.setSpacing(30)

        # Section title
        section_title = QLabel("Key Features")
        section_title.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        section_title.setStyleSheet("color: white;")
        section_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        section_title.setMinimumHeight(40)

        # Features grid with better spacing
        self.features_grid = QGridLayout()
        self.features_grid.setHorizontalSpacing(20)  # More horizontal space
        self.features_grid.setVerticalSpacing(20)  # More vertical space

        self.features = [
            ("Password Manager", "Secure vault for all your credentials", "#FF6B6B"),
            ("Task Organizer", "Smart to-do lists with reminders", "#4ECDC4"),
            ("Idea Board", "Capture and organize creative ideas", "#FFBE0B"),
            ("Finance Tracker", "Manage budgets and expenses", "#9D4EDD")
        ]

        # Create feature cards
        self.feature_cards = []
        for title, desc, color in self.features:
            card = self.create_feature_card(title, desc, color)
            self.feature_cards.append(card)

        self.features_layout.addWidget(section_title)
        self.features_layout.addLayout(self.features_grid)

        # Ensure the section has enough height
        features_frame.setMinimumHeight(300)
        layout.addWidget(features_frame)

    def create_feature_card(self, title, description, color):
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                border-left: 5px solid {color};
            }}
        """)
        card.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        card.setMinimumSize(200, 180)  # Minimum card size

        # Create card layout with better margins
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(15, 15, 15, 15)
        card_layout.setSpacing(12)

        # Icon placeholder with better positioning
        icon = QLabel("•")
        icon.setStyleSheet(f"color: {color}; font-size: 30px;")
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon.setFixedHeight(30)  # Fixed height for icon

        # Feature title with fixed height
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setFixedHeight(30)  # Fixed height for title

        # Feature description
        desc_label = QLabel(description)
        desc_label.setFont(QFont("Arial", 12))
        desc_label.setStyleSheet("color: rgba(255, 255, 255, 0.8);")  # More visible
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc_label.setMinimumHeight(60)  # Ensure enough height for description

        card_layout.addWidget(icon)
        card_layout.addWidget(title_label)
        card_layout.addWidget(desc_label)
        card_layout.addStretch()  # Add stretch at the end to keep content at top

        # Add hover effect
        card.enterEvent = lambda e: self.animate_card(card, True)
        card.leaveEvent = lambda e: self.animate_card(card, False)

        return card

    def animate_card(self, card, hover):
        animation = QPropertyAnimation(card, b"geometry")
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.Type.OutQuad)

        rect = card.geometry()
        if hover:
            animation.setEndValue(rect.adjusted(-3, -3, 3, 3))  # Less movement
        else:
            animation.setEndValue(rect.adjusted(3, 3, -3, -3))  # Less movement

        animation.start()

    def setup_cta_section(self, layout):
        self.cta_frame = QFrame()
        self.cta_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 30px; /* Reduced padding */
            }
        """)
        self.cta_frame.setMinimumHeight(200)  # Minimum height

        cta_layout = QVBoxLayout(self.cta_frame)
        cta_layout.setContentsMargins(20, 20, 20, 20)  # More consistent padding
        cta_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cta_layout.setSpacing(20)

        self.cta_title = QLabel("Ready to boost your productivity?")
        self.cta_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))  # Slightly smaller
        self.cta_title.setStyleSheet("color: white;")
        self.cta_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cta_title.setWordWrap(True)
        self.cta_title.setMinimumHeight(80)  # Minimum height

        self.cta_text = QLabel("Join thousands of users who transformed their workflow")
        self.cta_text.setFont(QFont("Arial", 11))  # Slightly smaller
        self.cta_text.setStyleSheet("color: rgba(255, 255, 255, 0.8);")  # More visible
        self.cta_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cta_text.setWordWrap(True)
        self.cta_text.setMinimumHeight(80)  # Minimum height

        self.cta_btn = QPushButton("Get Started Now")
        self.cta_btn.setStyleSheet("""
            QPushButton {
                background-color: #2a82da;
                color: white;
                padding: 12px 25px;
                font-size: 16px;
                border-radius: 25px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #1a6bb0;
            }
        """)
        self.cta_btn.setFixedSize(220, 50)  # Fixed size for consistency

        cta_layout.addWidget(self.cta_title)
        cta_layout.addWidget(self.cta_text)
        cta_layout.addWidget(self.cta_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.cta_frame)

    def setup_footer(self, layout):
        self.footer = QFrame()
        self.footer.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 0.2);
                padding: 20px;
            }
        """)
        self.footer.setMinimumHeight(150)  # Minimum height

        footer_layout = QVBoxLayout(self.footer)
        footer_layout.setContentsMargins(10, 15, 10, 15)
        footer_layout.setSpacing(15)

        # Links container with better layout
        self.links_container = QFrame()
        self.links_container.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.links_layout = QHBoxLayout(self.links_container)
        self.links_layout.setContentsMargins(0, 0, 0, 0)
        self.links_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.links_layout.setSpacing(8)  # More space between links

        self.link_buttons = []
        links = ["About", "Features", "Pricing", "Contact", "Privacy", "Terms"]
        for link in links:
            btn = QPushButton(link)
            btn.setStyleSheet("""
                QPushButton {
                    color: rgba(255, 255, 255, 0.7);
                    background: transparent;
                    border: none;
                    padding: 8px 12px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    color: white;
                }
            """)
            btn.setFixedHeight(40)  # Fixed height for buttons
            self.link_buttons.append(btn)
            self.links_layout.addWidget(btn)

        # Copyright with fixed height
        self.copyright = QLabel("© 2025 Productivity Hub. All rights reserved.")
        self.copyright.setStyleSheet("color: rgba(255, 255, 255, 0.5);")
        self.copyright.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.copyright.setWordWrap(True)
        self.copyright.setFixedHeight(20)

        # Logout button with fixed size
        self.logout_btn = QPushButton("Logout")
        self.logout_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                padding: 8px 20px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        self.logout_btn.setFixedSize(100, 40)  # Fixed size
        self.logout_btn.clicked.connect(self.on_logout)

        footer_layout.addWidget(self.links_container)
        footer_layout.addWidget(self.copyright)
        footer_layout.addWidget(self.logout_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.footer)

    def setup_animations(self):
        # Title animation
        self.title_anim = QPropertyAnimation(self.hero_title, b"pos")
        self.title_anim.setDuration(1000)
        self.title_anim.setStartValue(self.hero_title.pos() + QPoint(0, -30))  # Less movement
        self.title_anim.setEndValue(self.hero_title.pos())
        self.title_anim.setEasingCurve(QEasingCurve.Type.OutBack)

        # Subtitle animation
        self.subtitle_anim = QPropertyAnimation(self.hero_subtitle, b"opacity")
        self.subtitle_anim.setDuration(1500)
        self.subtitle_anim.setStartValue(0)
        self.subtitle_anim.setEndValue(1)

        # Group animations
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.title_anim)
        self.anim_group.addAnimation(self.subtitle_anim)

        # Start animations after a short delay
        QTimer.singleShot(300, self.anim_group.start)

    def on_resize(self, event):
        width = self.width()

        # Update the gradient
        self.set_gradient_background()

        # Responsive header adjustments
        if width < 768:
            # Mobile view
            self.logo.setFont(QFont("Arial", 16, QFont.Weight.Bold))
            for btn in self.nav_buttons:
                btn.setVisible(False)
            self.menu_btn.setVisible(True)
        else:
            # Desktop view
            self.logo.setFont(QFont("Arial", 18, QFont.Weight.Bold))
            for btn in self.nav_buttons:
                btn.setVisible(True)
            self.menu_btn.setVisible(False)
            self.mobile_menu.setVisible(False)

        # Responsive hero section
        if width < 500:
            # Very small screens
            self.hero_title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
            self.hero_subtitle.setFont(QFont("Arial", 12))
            self.get_started_btn.setFixedSize(160, 45)
            self.get_started_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2a82da;
                    color: white;
                    padding: 8px 15px;
                    font-size: 14px;
                    border-radius: 20px;
                }
                QPushButton:hover {
                    background-color: #1a6bb0;
                }
            """)
        elif width < 768:
            # Medium small screens
            self.hero_title.setFont(QFont("Arial", 26, QFont.Weight.Bold))
            self.hero_subtitle.setFont(QFont("Arial", 14))
            self.get_started_btn.setFixedSize(180, 50)
            self.get_started_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2a82da;
                    color: white;
                    padding: 10px 20px;
                    font-size: 15px;
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: #1a6bb0;
                }
            """)
        else:
            # Large screens
            self.hero_title.setFont(QFont("Arial", 32, QFont.Weight.Bold))
            self.hero_subtitle.setFont(QFont("Arial", 16))
            self.get_started_btn.setFixedSize(200, 50)
            self.get_started_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2a82da;
                    color: white;
                    padding: 12px 25px;
                    font-size: 16px;
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: #1a6bb0;
                }
            """)

        # Responsive feature cards layout
        self.adjust_feature_cards(width)

        # Responsive CTA section
        if width < 500:
            # Very small screens
            self.cta_title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
            self.cta_text.setFont(QFont("Arial", 12))
            self.cta_btn.setFixedSize(160, 45)
            self.cta_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2a82da;
                    color: white;
                    padding: 8px 15px;
                    font-size: 14px;
                    border-radius: 20px;
                }
                QPushButton:hover {
                    background-color: #1a6bb0;
                }
            """)
            self.cta_frame.setStyleSheet("""
                QFrame {
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 15px;
                    padding: 15px;
                }
            """)
        elif width < 768:
            # Medium small screens
            self.cta_title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
            self.cta_text.setFont(QFont("Arial", 13))
            self.cta_btn.setFixedSize(180, 50)
            self.cta_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2a82da;
                    color: white;
                    padding: 10px 20px;
                    font-size: 15px;
                    border-radius: 20px;
                }
                QPushButton:hover {
                    background-color: #1a6bb0;
                }
            """)
            self.cta_frame.setStyleSheet("""
                QFrame {
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 15px;
                    padding: 20px;
                }
            """)
        else:
            # Large screens
            self.cta_title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
            self.cta_text.setFont(QFont("Arial", 14))
            self.cta_btn.setFixedSize(220, 50)
            self.cta_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2a82da;
                    color: white;
                    padding: 12px 25px;
                    font-size: 16px;
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: #1a6bb0;
                }
            """)
            self.cta_frame.setStyleSheet("""
                QFrame {
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 15px;
                    padding: 30px;
                }
            """)

        # Responsive footer
        if width < 600:
            # Stack links vertically in small screens
            self.adjust_footer_links(True)
        else:
            # Arrange links horizontally in large screens
            self.adjust_footer_links(False)

        super().resizeEvent(event)

    def adjust_feature_cards(self, width):
        # Clear current grid items
        while self.features_grid.count():
            item = self.features_grid.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        # Determine grid layout based on width
        if width < 500:
            # Single column for very small screens
            for i, card in enumerate(self.feature_cards):
                self.features_grid.addWidget(card, i, 0)
                # Set fixed height for cards in small screens
                card.setFixedHeight(180)
        elif width < 800:
            # Two columns for medium screens
            for i, card in enumerate(self.feature_cards):
                row = i // 2
                col = i % 2
                self.features_grid.addWidget(card, row, col)
                card.setFixedHeight(180)
        else:
            # Four columns for large screens
            for i, card in enumerate(self.feature_cards):
                self.features_grid.addWidget(card, 0, i)
                # Allow cards to expand in height on large screens
                card.setMinimumHeight(200)

    def adjust_footer_links(self, vertical):
        # Remove all widgets from links layout
        while self.links_layout.count():
            item = self.links_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        if vertical:
            # Create a vertical layout for small screens
            self.links_layout.setDirection(QHBoxLayout.Direction.TopToBottom)
            for btn in self.link_buttons:
                self.links_layout.addWidget(btn)
                btn.setFixedHeight(35)  # Smaller buttons in mobile view
        else:
            # Create a horizontal layout for larger screens
            self.links_layout.setDirection(QHBoxLayout.Direction.LeftToRight)
            for btn in self.link_buttons:
                self.links_layout.addWidget(btn)
                btn.setFixedHeight(40)  # Standard size buttons

    def paintEvent(self, event):
        # Add some decorative elements
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw some circles in the background - scaled for responsive design
        width = self.width()
        height = self.height()

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(255, 255, 255, 10))

        # Scale decorative elements based on screen size
        circle1_size = min(width, height) * 0.25  # Smaller circles
        circle2_size = min(width, height) * 0.35

        painter.drawEllipse(int(width * 0.1), int(height * 0.1), int(circle1_size), int(circle1_size))
        painter.drawEllipse(int(width - circle2_size - width * 0.1), int(height - circle2_size - height * 0.1),
                            int(circle2_size), int(circle2_size))