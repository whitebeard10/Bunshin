import sys
from PyQt6.QtWidgets import QApplication
from app.ui.login_window import LoginWindow
from app.ui.landing_page import LandingPage


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = None
        self.landing_page = None
        self.show_login()

    def show_login(self):
        if self.landing_page:
            self.landing_page.close()
        self.login_window = LoginWindow(on_login_success=self.show_landing)
        self.login_window.show()

    def show_landing(self):
        if self.login_window:
            self.login_window.close()
        self.landing_page = LandingPage(on_logout=self.show_login)
        self.landing_page.show()

    def run(self):
        sys.exit(self.app.exec())


if __name__ == "__main__":
    # Configure high DPI scaling
    from PyQt6.QtCore import Qt
    from PyQt6.QtGui import QGuiApplication

    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    # Create and run application
    application = Application()
    application.run()