from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
import sympy as sp

class Criticalpoint(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("critical points ploter")

        self.layout = QVBoxLayout()

        self.func_input = QLineEdit()
        self.func_input.setPlaceholderText("enter your function")
        self.layout.addWidget(self.func_input)

        self.button = QPushButton("plot critical poiints")
        self.layout.addWidget(self.button)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)
        self.button.clicked.connect(self.plot)

    def plot(self):
        func_text = self.func_input.text()
        x = sp.Symbol("x")
        f = sp.sympify(func_text)

        f_prime = sp.diff(f, x)
        critical_x = sp.solve(f_prime, x)

        f_np = sp.lambdify(x, f, "numpy")
        x_value = np.linspace(-10, 10, 400)
        y_value = f_np(x_value)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x_value, y_value, label="Function")

        for cx in critical_x:
            try:
                cx_val = float(cx)
                cy_val = f_np(cx_val)
                ax.plot(cx_val, cy_val, 'ro')
                ax.text(cx_val, cy_val, f"({cx_val:.2f}, {cy_val:.2f})", fontsize=9)
            except:
                continue

        ax.set_title("function with critical points")
        ax.legend()
        self.canvas.draw()

app = QApplication([])
window = Criticalpoint()
window.show()
app.exec()