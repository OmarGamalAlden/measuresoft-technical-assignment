from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRectF


class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(600, 400)

        self.bgColor = QColor(Qt.GlobalColor.white)

        self.start = None
        self.end = None

        self.shape = "line"
        self.color = QColor(Qt.GlobalColor.black)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start = event.position()
            self.end = None
            self.update()

    def mouseMoveEvent(self, event):
        if self.start:
            self.end = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.end = event.position()
            self.update()

    # draw current shape based on mouse start/end points
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.bgColor)

        if not self.start or not self.end:
            return

        painter.setPen(self.color)

        x1 = self.start.x()
        y1 = self.start.y()
        x2 = self.end.x()
        y2 = self.end.y()

        if self.shape == "line":
            painter.drawLine(self.start, self.end)
            return

        rect = QRectF(
            min(x1, x2),
            min(y1, y2),
            abs(x2 - x1),
            abs(y2 - y1)
        )

        if self.shape == "rect":
            painter.drawRect(rect)
        elif self.shape == "ellipse":
            painter.drawEllipse(rect)

    def setShape(self, shape):
        self.shape = shape

    def setColor(self, color):
        self.color = color
        self.update()

    def clear(self):
        self.start = None
        self.end = None
        self.update()
