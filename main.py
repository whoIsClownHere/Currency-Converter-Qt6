import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy


EXCHANGE_RATES = {
    'RU': 1,
    'USD': 70,
    'ERO': 80,
    'TUR': 30
}


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Конвертор валют")

        self.main_layout = QHBoxLayout(self)
        self.input_layout = QVBoxLayout(self)
        self.output_layout = QVBoxLayout(self)

        self.input_value = QLineEdit(self)
        self.input_value.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.input_type = QComboBox(self)
        self.input_type.addItems(EXCHANGE_RATES.keys())
        self.input_type.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.convert_btn = QPushButton(self)
        self.convert_btn.setText("->")
        self.convert_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.convert_btn.clicked.connect(self.convert)

        self.output_value = QLineEdit(self)
        self.output_value.setEnabled(False)
        self.output_value.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.output_type = QComboBox(self)
        self.output_type.addItems(EXCHANGE_RATES.keys())
        self.output_type.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.input_layout.addWidget(self.input_value)
        self.input_layout.addWidget(self.input_type)

        self.output_layout.addWidget(self.output_value)
        self.output_layout.addWidget(self.output_type)

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addWidget(self.convert_btn)
        self.main_layout.addLayout(self.output_layout)

        self.setLayout(self.main_layout)

    def convert(self):
        input = float(self.input_value.text()) * EXCHANGE_RATES[self.input_type.currentText()]
        output = input / EXCHANGE_RATES[self.output_type.currentText()]
        self.output_value.setText(f"{output:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()

    sys.exit(app.exec())
