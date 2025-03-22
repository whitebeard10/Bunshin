import sys
from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QPixmap, QColor
from app.gui.main_window import MainWindow

def apply_dark_theme(app):
    # Set dark palette
    dark_palette = app.palette()
    dark_palette.setColor(dark_palette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(dark_palette.ColorRole.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(dark_palette.ColorRole.Base, QColor(35, 35, 35))
    dark_palette.setColor(dark_palette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(dark_palette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    dark_palette.setColor(dark_palette.ColorRole.ToolTipText, QColor(255, 255, 255))
    dark_palette.setColor(dark_palette.ColorRole.Text, QColor(255, 255, 255))
    dark_palette.setColor(dark_palette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(dark_palette.ColorRole.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(dark_palette.ColorRole.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(dark_palette.ColorRole.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(dark_palette.ColorRole.HighlightedText, QColor(255, 255, 255))
    app.setPalette(dark_palette)

    # Set style sheet for additional styling
    app.setStyleSheet("""
        QToolTip {
            color: #ffffff;
            background-color: #2a82da;
            border: 1px solid white;
        }
        QPushButton {
            background-color: #2a82da;
            color: white;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #1c5a9b;
        }
        QLineEdit {
            background-color: #353535;
            color: white;
            border: 1px solid #555;
            border-radius: 3px;
            padding: 5px;
        }
        QTableWidget {
            background-color: #353535;
            color: white;
            gridline-color: #555;
        }
        QHeaderView::section {
            background-color: #2a82da;
            color: white;
            padding: 5px;
        }
    """)

def main():
    app = QApplication(sys.argv)

    # Show splash screen
    splash_pix = QPixmap("../resources/splash-screen.svg")
    splash = QSplashScreen(splash_pix)
    splash.show()

    # Simulate loading
    app.processEvents()

    # Apply dark theme
    apply_dark_theme(app)

    # Main window
    window = MainWindow()
    window.show()

    # Close splash screen
    splash.finish(window)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()