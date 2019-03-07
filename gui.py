#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLCDNumber, QSlider
from slider import SliderDisplay


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Spring-Mass-Damper Playground')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)
        # self.resize(1000, 800)

        # main layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # layout
        layout1 = QVBoxLayout()
        widget.setLayout(layout1)
        layout2 = QVBoxLayout()
        widget.setLayout(layout2)

        # label
        label = QLabel('System parameters')
        label2 = QLabel('Simulation parameters')

        # sliders
        mass_slider = SliderDisplay('Mass', 0, 10)
        spring_slider = SliderDisplay('Spring', 0, 10)
        damper_slider = SliderDisplay('Damper', 0, 10)
        time_slider = SliderDisplay('Time(s)', 0, 100)

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # You probably want to add in other interface elements here

        # Add things to the layout
        layout.addStretch()
        layout.addWidget(label)
        layout1.addWidget(mass_slider)
        layout1.addWidget(spring_slider)
        layout1.addWidget(damper_slider)
        layout.addLayout(layout1)
        layout.addWidget(quit_button)

        # Add other widgets to the layout here.  Possibly other layouts.


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

