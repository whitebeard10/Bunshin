from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QSize
from PyQt6.QtWidgets import QWidget, QGraphicsOpacityEffect, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class FadeAnimation:
    """Helper class for fade animations"""
    @staticmethod
    def fade_in(widget: QWidget, duration=500):
        """Fade in animation"""
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity", widget)
        anim.setDuration(duration)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        return anim

    @staticmethod
    def fade_out(widget: QWidget, duration=500):
        """Fade out animation"""
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity", widget)
        anim.setDuration(duration)
        anim.setStartValue(1)
        anim.setEndValue(0)
        anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        return anim

class SlideAnimation:
    """Helper class for slide animations"""
    @staticmethod
    def slide_from_left(widget: QWidget, duration=500, offset=100):
        """Slide from left animation"""
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(widget.x() - offset, widget.y()))
        anim.setEndValue(QPoint(widget.x(), widget.y()))
        anim.setEasingCurve(QEasingCurve.Type.OutBack)
        return anim

    @staticmethod
    def slide_from_right(widget: QWidget, duration=500, offset=100):
        """Slide from right animation"""
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(widget.x() + offset, widget.y()))
        anim.setEndValue(QPoint(widget.x(), widget.y()))
        anim.setEasingCurve(QEasingCurve.Type.OutBack)
        return anim

    @staticmethod
    def slide_from_top(widget: QWidget, duration=500, offset=100):
        """Slide from top animation"""
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(widget.x(), widget.y() - offset))
        anim.setEndValue(QPoint(widget.x(), widget.y()))
        anim.setEasingCurve(QEasingCurve.Type.OutBack)
        return anim

    @staticmethod
    def slide_from_bottom(widget: QWidget, duration=500, offset=100):
        """Slide from bottom animation"""
        anim = QPropertyAnimation(widget, b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPoint(widget.x(), widget.y() + offset))
        anim.setEndValue(QPoint(widget.x(), widget.y()))
        anim.setEasingCurve(QEasingCurve.Type.OutBack)
        return anim

def load_stylesheet(file_path: str) -> str:
    """Load CSS styles from file"""
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: Stylesheet not found at {file_path}")
        return ""
    except Exception as e:
        print(f"Error loading stylesheet: {str(e)}")
        return ""

def apply_drop_shadow(widget: QWidget, radius=10, offset=(2, 2), color=None):
    """Apply drop shadow effect to a widget"""
    shadow = QGraphicsDropShadowEffect(widget)
    shadow.setBlurRadius(radius)
    shadow.setOffset(*offset)
    if color is None:
        color = QColor(0, 0, 0, 80)
    shadow.setColor(color)
    widget.setGraphicsEffect(shadow)