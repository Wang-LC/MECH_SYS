#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QGroupBox, QHBoxLayout
from slider import SliderDisplay
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from msd import MassSpringDamper
import math


def pprint(m, s, d, t, ts):
    print('Mass: %s' % m)
    print('Spring: %s' % s)
    print('Damper: %s' % d)
    print('Time(s): %s' % t)
    print('Time Step: %s' % ts)
    print('-'*30)


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.TimeBox = QGroupBox()
        self.SysBox = QGroupBox()
        self.BhBox = QGroupBox()
        self.setWindowTitle('Spring-Mass-Damper Playground')
        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)
        self.resize(1500, 1000)

        # create System Box
        sys_layout = QVBoxLayout()
        self.mass_slider = SliderDisplay('Mass', 0, 10)
        self.spring_slider = SliderDisplay('Spring', 0, 10)
        self.damper_slider = SliderDisplay('Damper', 0, 10)
        # add things to layout
        sys_layout.addWidget(self.mass_slider)
        sys_layout.addWidget(self.spring_slider)
        sys_layout.addWidget(self.damper_slider)
        self.SysBox.setLayout(sys_layout)

        # create behavior box
        BH_layout = QHBoxLayout()
        text_label = QLabel('Type:')
        self.type = QLabel('None')
        # add to layout
        BH_layout.addWidget(text_label)
        BH_layout.addWidget(self.type)
        BH_layout.addStretch(1)
        self.BhBox.setLayout(BH_layout)

        # creat Time Box
        layout = QVBoxLayout()
        self.time_slider = SliderDisplay('Time (s)', 0, 100)
        self.step_slider = SliderDisplay('Time step (s)', 0.001, 0.1)
        self.initial = SliderDisplay('Initial x', -10, 0)
        self.dx = SliderDisplay('Initial dx', 0, 0.1)
        # add things to layout
        layout.addWidget(self.time_slider)
        layout.addWidget(self.step_slider)
        layout.addWidget(self.initial)
        layout.addWidget(self.dx)
        self.TimeBox.setLayout(layout)

        # set title label
        label1 = QLabel('System parameters')
        label2 = QLabel('Simulation parameters')
        label3 = QLabel('System Behavior')

        # simulate button
        ss_button = QPushButton('Simulate\nSystem')
        ss_button.clicked.connect(
            lambda : pprint(self.mass_slider.value() / 1000, self.spring_slider.value() / 1000,
                            self.damper_slider.value() / 1000, self.time_slider.value() / 1000,
                            self.step_slider.value() / 1000)
        )
        ss_button.clicked.connect(self.draw)
        ss_button.clicked.connect(self.findType)

        # quit button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # The display for the graph
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

        # main layout
        mainLayout = QHBoxLayout()
        widget.setLayout(mainLayout)
        # left layout
        left_Layout = QVBoxLayout()
        # add things to left layout
        left_Layout.addWidget(label1)
        left_Layout.addWidget(self.SysBox)
        left_Layout.addStretch(1)
        left_Layout.addWidget(label3)
        left_Layout.addWidget(self.BhBox)
        left_Layout.addStretch(1)
        left_Layout.addWidget(label2)
        left_Layout.addWidget(self.TimeBox)
        left_Layout.addStretch(1)
        left_Layout.addWidget(ss_button)
        left_Layout.addStretch(6)
        left_Layout.addWidget(quit_button)
        left_Layout.addStretch(1)

        # set main layout
        mainLayout.addLayout(left_Layout, stretch=1)
        mainLayout.addWidget(self.display, stretch=2)
        widget.setLayout(mainLayout)

    def draw(self):
        try:
            self.figure.clear()
            k = self.spring_slider.value() / 1000
            m = self.mass_slider.value() / 1000
            c = self.damper_slider.value() / 1000
            time = self.time_slider.value() / 1000
            ts = self.step_slider.value() / 1000
            ini = self.initial.value() / 1000
            dx = self.dx.value() / 1000
            ax = self.figure.add_subplot(111)
            smd = MassSpringDamper(m, k, c, time, ts)
            # start point at (-1,0)
            state, t = smd.simulate(ini, dx)
            self.z = c / (2*math.sqrt(k*m))
            self.displacement = []

            for s in state :
                self.displacement.append(s[0])
            ax.plot(t, self.displacement, 'r-')
            ax.set_title('Spring-Mass-Damper System Behavior\n'
                         'k = %s, m = %s, c = %s, dt = %s' % (k, m, c, ts)
                         )
            ax.set_xlabel('Times(s)')
            ax.set_ylabel('Amplitude')
            self.display.draw()
        except:
            self.z = -1

    def findType(self):
        if self.z == 0:
            self.type.setText('Undamped')
        elif 0 <= self.z < 1:
            self.type.setText('Underdamped')
        elif self.z > 1:
            self.type.setText('Overdamped')
        elif self.z == 1:
            self.type.setText('Critically damped')
        else:
            self.type.setText('wrong parameters set up')


if __name__ == '__main__' :
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()
