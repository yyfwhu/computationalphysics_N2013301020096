'''
program SIMPLE_pendulum 
Author: Yao Yifei   Last Modify:20160520
'''
#to sove the oscillatory motivation
#with Euler and Euler-cromer method
from pylab import *
import numpy as np


class Euler(object):
    def __init__(self, theta0 = 10, omg0 = 0, t0 = 0, g = 9.8, l = 9.8/(4*(np.pi)**2), dt = 0.02, et = 7. ):
        self.theta, self.omg, self.t = [theta0], [omg0], [t0]
        self.l, self.g, self.dt, self.et, self.n = l, g, dt, et, int(et / dt)
        self.E = [0.5*((self.l * omg0)**2 + self.g * self.l*(theta0)**2)]
    def update(self):
        for i in range(self.n):
            self.t.append(self.t[-1] + self.dt)
            self.omg.append(self.omg[-1] - (self.g / self.l) * self.theta[-1] * self.dt)
            self.theta.append(self.theta[-1] + self.omg[-2] * self.dt)
            self.E.append(0.5*((self.l * self.omg[-1])**2 + self.g * self.l*(self.theta[-1])**2))
    def pl_theta(self, pic):
        pic.plot(self.t, self.theta,'g--', label = 'Euler Method')
    def pl_E(self, pic):
        pic.plot(self.t, self.E,'g--', label = 'Euler Method')

class Euler_cromer(Euler):
    def update(self):
        for i in range(self.n):
            self.t.append(self.t[-1] + self.dt)
            self.omg.append(self.omg[-1] - (self.g / self.l) * self.theta[-1] * self.dt)
            self.theta.append(self.theta[-1] + self.omg[-1] * self.dt)
            self.E.append(0.5*((self.l * self.omg[-1])**2 + self.g * self.l*(self.theta[-1])**2))
    def pl_theta(self, pic):
        pic.plot( self.theta, self.omg,'r--', label = 'Euler-cromer Method')
    def pl_E(self, pic):
        pic.plot(self.t, self.E,'r--', label = 'Euler-cromer Method')
pic_1 = subplot(121)
pic_2 = subplot(122)
s = Euler()
s.update()
s.pl_theta(pic_1)
s.pl_E(pic_2)

s = Euler_cromer()
s.update()
s.pl_theta(pic_1)
s.pl_E(pic_2)
pic_1.set_xlabel('time/(t)')
pic_1.set_ylabel('angel/(rad)')
pic_1.legend(loc = 'best')
pic_2.set_xlabel('time/(t)')
pic_2.set_ylabel('energy/(J)')
pic_2.legend(loc = 'best')

plt.show()


        