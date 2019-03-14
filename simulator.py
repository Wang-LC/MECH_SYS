import subprocess


class Simulator:
    def __init__(self, instance):
        self.ins = instance

    def evaluate(self, path):
        with open('C:/Users/wlc-6/Downloads/waypoints', 'w') as f:
            for i in path:
                f.write(str(i).replace('(', '').replace(')', '').replace(',', '')+'\n')
        cmd = 'simulator waypoints %s' % (str(self.ins))
        p = subprocess.Popen(cmd, shell=True, cwd='C:/Users/wlc-6/Downloads')
        # cwd = 'file path'
        return p


if __name__ == '__main__':
    w = [(-10, -10), (0, 2), (10, 10)]
    s = Simulator(10)
    print(s.evaluate(w))