#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QGroupBox, QHBoxLayout
from slider import SliderDisplay


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.TimeBox = QGroupBox()
        self.SysBox = QGroupBox()
        self.setWindowTitle('Spring-Mass-Damper Playground')
        self.createSysBox()
        self.createTimeBox()
        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)
        self.resize(500, 400)

        # set title label
        label1 = QLabel('System parameters')
        label2 = QLabel('Simulation parameters')

        # simulate button
        ss_button = QPushButton('Simulate\nSystem')

        # quit button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)
        # main layout
        mainLayout = QHBoxLayout()
        # sub layout
        subLayout = QVBoxLayout()
        # add things to layout
        subLayout.addWidget(label1)
        subLayout.addWidget(self.SysBox)
        subLayout.addWidget(label2)
        subLayout.addWidget(self.TimeBox)
        subLayout.addWidget(ss_button)
        subLayout.addWidget(quit_button)
        widget.setLayout(subLayout)
        mainLayout.addLayout(subLayout)
        widget.setLayout(mainLayout)

    def createSysBox(self):
        layout = QVBoxLayout()
        mass_slider = SliderDisplay('Mass', 0, 10)
        spring_slider = SliderDisplay('Spring', 0, 10)
        damper_slider = SliderDisplay('Damper', 0, 10)
        # add things to layout
        layout.addWidget(mass_slider)
        layout.addWidget(spring_slider)
        layout.addWidget(damper_slider)
        self.SysBox.setLayout(layout)

    def createTimeBox(self):
        layout = QVBoxLayout()
        time_slider = SliderDisplay('Time (s)', 0, 100)
        step_slider = SliderDisplay('Time step (s)', 0.001, 0.1)
        # add things to layout
        layout.addWidget(time_slider)
        layout.addWidget(step_slider)
        self.TimeBox.setLayout(layout)



if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

