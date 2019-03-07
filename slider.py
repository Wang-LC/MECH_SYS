#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout,QLCDNumber
from PyQt5 import QtCore


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks=1000):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.setLayout(layout)

        # A slider
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.slider.valueChanged.connect(lambda: self.value(ticks))
        self.slider.setRange(low*ticks, high*ticks)

        # A label
        self.lb = QLabel('%s: ' % name)
        self.lb2 = QLabel('0.000', self)

        # Add things to the layout
        layout.addWidget(self.lb)
        layout.addWidget(self.lb2)
        layout.addWidget(self.slider)

    def value(self, ticks):
        return self.lb2.setText(str(self.slider.value()/ticks))


if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('foo', 0, 10)

    slider.show()

    app.exec_()

