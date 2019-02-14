from msd import MassSpringDamper
import matplotlib.pyplot as plt


def damper():
    smd = MassSpringDamper(m=1.0, k=106.53587366415807, c=1.0115579455349972)
    state, t = smd.simulate(-1, 0)
    displacement = []

    for s in state:
        displacement.append(s[0])

    plt.plot(t, displacement, 'r-')
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.title('the displacement of the mass over time')
    plt.show()


if __name__ == "__main__":
    damper()