import numpy as np
import pandas as pd

G = 9.8


class Projectile():

    def __init__(self, v0, theta):

        self.v0 = v0
        theta = np.radians(theta)
        self.ct = np.cos(theta)
        self.st = np.sin(theta)
        self.tof = None
        self.h = None
        self.toh = None

    def pos(self, t):

        x = self.v0*t*self.ct
        y = self.v0*t*self.st - 0.5*G*t**2

        return (x, y)

    def vel(self, t):

        x = self.v0*t*self.ct
        y = self.v0*t*self.st - G*t

        return (x, y)

    def accel(self, t):

        return (0, -G)

    def timeOfFlight(self):

        if self.tof is None:
            self.tof = 2*self.v0*self.st/G

        return self.tof

    def height(self):

        if self.h is None:
            self.h = (self.v0**2*self.st**2)/(2*G)
            self.toh = self.v0*self.st/G

        return (self.h, self.toh)


def generate_data(runs):

    for run in range(1, runs+1):
        vel = np.random.uniform(1, 10000)
        angle = np.random.uniform(1, 90)
        p = Projectile(vel, angle)

        time = np.arange(0, p.timeOfFlight(), 0.1)
        pos = map(p.pos, time)
        pos = pd.DataFrame(pos, columns=['x', 'y'])
        vel = map(p.vel, time)
        vel = pd.DataFrame(vel, columns=['dx', 'dy'])

        time = pd.DataFrame(time, columns=['time'])
        df = pd.concat([time, pos, vel], axis=1)
        df['accel'] = -G

        df.to_csv('mc%03d.csv.gz' % run, index=False, compression='gzip')
