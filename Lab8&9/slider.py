#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PyQt5 import QtCore


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks=1000):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.setLayout(layout)

        # A slider
        self.slider = QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(low * ticks, high * ticks)
        self.slider.setValue(low*ticks)
        self.slider.valueChanged.connect(lambda : self.lb2.setText(str(self.value()/ticks)))

        # A label
        self.lb = QLabel('%s: ' % name)
        v = self.value()/ticks
        self.lb2 = QLabel('%.3f' % v)

        # Add things to the layout
        layout.addWidget(self.lb)
        layout.addWidget(self.lb2)
        layout.addWidget(self.slider)

    def value(self):
        return self.slider.value()


if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('foo', 0.001, 0.01)

    slider.show()

    app.exec_()

