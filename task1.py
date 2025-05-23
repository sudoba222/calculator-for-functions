import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
 
class calculator1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("plot your function ")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input = QLineEdit()
        self.input.setPlaceholderText("enter  your  function ")
        self.layout.addWidget(self.input)

        self.button = QPushButton("plot function")
        self.button.clicked.connect(self.plot)
        self.layout.addWidget(self.button)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def plot(self):
        expr = self.input.text()
        x = np.linspace(-10, 10, 400)
        names = {"x": x, "np": np}
        try:
            y = eval(expr, {"__builtins__": {}}, names)
            self.ax.clear()
            self.ax.plot(x, y, label=expr)
            self.ax.legend()
            self.ax.grid(True)
            self.canvas.draw()
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = calculator1()
    window.show()
    sys.exit(app.exec())
