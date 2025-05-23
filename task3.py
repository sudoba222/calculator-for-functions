from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
import sympy as sp
from scipy.integrate import quad

class AreaCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Area Under the Curve")
        self.layout = QVBoxLayout()

        self.func_input = QLineEdit()
        self.func_input.setPlaceholderText("Enter your function")
        self.layout.addWidget(self.func_input)

        self.a_input = QLineEdit()
        self.a_input.setPlaceholderText("Enter lower limit a")
        self.layout.addWidget(self.a_input)

        self.b_input = QLineEdit()
        self.b_input.setPlaceholderText("Enter upper limit b")
        self.layout.addWidget(self.b_input)

        self.button = QPushButton("Plot Area")
        self.layout.addWidget(self.button)

        self.area_label = QLabel("")
        self.layout.addWidget(self.area_label)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.layout.addWidget(self.canvas)

        self.button.clicked.connect(self.plot_area)
        self.setLayout(self.layout)

    def plot_area(self):
        func = self.func_input.text()
        a1 = self.a_input.text()
        b1 = self.b_input.text()

        a = float(a1)
        b = float(b1)

        x = sp.Symbol("x")
        f = sp.sympify(func)
        f_np = sp.lambdify(x, f, "numpy")

        area, _ = quad(f_np, a, b)

        x_values = np.linspace(-20, 20, 400)
        y_values = f_np(x_values)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x_values, y_values)
        ax.fill_between(x_values, y_values, where=(x_values >= a) & (x_values <= b), color="lightgreen")
        ax.set_title(f"Area from {a} to {b}: {area:.4f}")

        self.canvas.draw()
        self.area_label.setText(f"Area under the curve: {area:.4f}")

app = QApplication([])
window = AreaCalculator()
window.show()
app.exec()