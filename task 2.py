import sys
import numpy as np
import sympy as sp
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class DerivativePlotter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function and Derivative Plotter")
        self.layout = QVBoxLayout()
        self.input = QLineEdit()
        self.input.setText("x**2")
        self.button = QPushButton("Plot")
        self.button.clicked.connect(self.plot)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self):
        expr_text = self.input.text()
        x_sym = sp.symbols('x')
        try:
            f_sym = sp.sympify(expr_text)
            f_prime = sp.diff(f_sym, x_sym)
            f_lamb = sp.lambdify(x_sym, f_sym, "numpy")
            fprime_lamb = sp.lambdify(x_sym, f_prime, "numpy")
            x = np.linspace(-10, 10, 400)
            y = f_lamb(x)
            yprime = fprime_lamb(x)
        except Exception:
            x = np.linspace(-10, 10, 400)
            y = np.zeros_like(x)
            yprime = np.zeros_like(x)

        self.figure.clear()
        ax = self.figure.add_subplot()
        ax.plot(x, y, label="f(x)")
        ax.plot(x, yprime, label="f'(x)")
        ax.legend()
        ax.set_title(f"Function and Derivative: {expr_text}")
        self.canvas.draw()

app = QApplication(sys.argv)
window = DerivativePlotter()
window.show()
app.exec()