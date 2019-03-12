#!/usr/bin/env python

from scipy.integrate import odeint
from numpy import arange


# Simulated mass-spring-damper system, using the ode solver from scipy
class MassSpringDamper :
    def __init__(self, m, k, c, time, ts) :
        self.m = m
        self.k = k
        self.c = c
        self.t = time
        self.ts = ts

    def simulate(self, x, x_dot) :
        initial_state = [x, x_dot]
        times = arange(0.0, self.t, self.ts)  # Set the simulation timesteps

        # Do the simulation
        state = odeint(lambda s, t : self.equation(s, t), initial_state, times)

        # Return the states (as [x, x_dot]) and the simulation timesteps
        return state, times

    # This function takes the current state [x, x_dot] and returns the
    # next velocity and acceleration [x_dot and x_do t_dot].  The
    # function is used by the scipy ode solver.
    def equation(self, state, t) :
        # unpack the state vector
        x = state[0]
        x_dot = state[1]

        # compute acceleration xdd
        x_dot_dot = -self.k / self.m * x - self.c / self.m * x_dot

        return [x_dot, x_dot_dot]


if __name__ == '__main__' :
    smd = MassSpringDamper(m=10, k=10, c=0, time=20, ts=0.01)
    state, t = smd.simulate(-1, 0.01)

    for s in state :
        print(s[0])
