import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QComboBox,
    QColorDialog,
    QVBoxLayout,
    QHBoxLayout
)

from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Draw App")
        self.resize(900, 600)

        self.canvas = Canvas()

        self.shapeBox = QComboBox()
        self.shapeBox.addItem("Line", "line")
        self.shapeBox.addItem("Rectangle", "rect")
        self.shapeBox.addItem("Ellipse", "ellipse")
        self.shapeBox.currentIndexChanged.connect(self.changeShape)

        self.colorBtn = QPushButton("Color")
        self.colorBtn.clicked.connect(self.pickColor)

        self.clearBtn = QPushButton("Clear")
        self.clearBtn.clicked.connect(self.canvas.clear)

        # top controls inputs (shape, color, clear)
        topLayout = QHBoxLayout()
        topLayout.addWidget(self.shapeBox)
        topLayout.addWidget(self.colorBtn)
        topLayout.addWidget(self.clearBtn)
        topLayout.addStretch()

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

    def changeShape(self):
        shape = self.shapeBox.currentData()
        self.canvas.setShape(shape)

    def pickColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.setColor(color)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
