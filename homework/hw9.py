'''
program SIMPLE_pendulum 
Author: Yao Yifei   Last Modify:20160520
'''
#to sove the oscillatory motivation
#with Euler and Euler-cromer method
from pylab import *
import math


class Cromer:
    def __init__(self,et = 400, theta0 = 1, omg0 = 0, t0 = 0, F = 1.2, q = 0.5, omgd = 2.0/3., g = 9.8, l = 9.8, dt = 0.01  ):
        self.theta, self.omg, self.t = [theta0], [omg0], [t0]
        self.l = l
        self.g = g
        self.dt = dt 
        self.omgd = omgd 
        self.q = q
        self.F = F 
        self.et = et
        self.n = int(et / dt)
        self.E = [0.5*((self.l * omg0)**2 + self.g * self.l*(theta0)**2)]
    def update(self):
        for i in range(self.n):
            if self.theta[-1] > pi:
                self.theta[-1] += -2 * pi
            elif self.theta[-1] < -pi:
                self.theta[-1] += 2 * pi
            
            self.t.append(self.t[-1] + self.dt)
            self.omg.append(self.omg[-1] - ( (self.g / self.l) * sin(self.theta[-1]) + self.q * self.omg[-1] - self.F * sin(self.omgd * self.t[-1]) ) * self.dt)
            self.theta.append(self.theta[-1] + self.omg[-1] * self.dt)
            self.E.append(0.5*((self.l * self.omg[-1])**2 + self.g * self.l*(self.theta[-1])**2))
    def pl_theta(self, pic):
        pic.plot(self.theta, self.omg,'o') # label = 'Euler_Cromer method' )



pic_1 = subplot(221)
pic_2 = subplot(222)
pic_3 = subplot(223)
pic_4 = subplot(224)

s = Cromer(50)
s.update()
s.pl_theta(pic_1)

s = Cromer(100)
s.update()
s.pl_theta(pic_2)

s = Cromer(500)
s.update()
s.pl_theta(pic_3)

s = Cromer(1000)
s.update()
s.pl_theta(pic_4)



pic_1.annotate('q = 1.0',
         xy=(0.9, 13.7), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#pic_1.set_title('period=' , size = 25)
pic_1.set_xlabel('Angle/(rad)')
pic_1.set_ylabel('$\omega$/(rad/s)')
pic_1.legend(loc = 'best')
pic_1.text(2,2,'n=50')
#pic_2.set_title('period', size = 25)
pic_2.set_xlabel('Angle/(rad)')
pic_2.set_ylabel('$\omega$/(rad/s)')
pic_2.legend(loc = 'best')
pic_2.text(2,2,'n=100')
#pic_3.set_title('period', size = 25)
pic_3.set_xlabel('Angle/(rad)')
pic_3.set_ylabel('$\omega$/(rad/s)')
pic_3.legend(loc = 'best')
pic_3.text(2,2,'n=500')
#pic_4.set_title('period', size = 25)
pic_4.set_xlabel('Angle/(rad)')
pic_4.set_ylabel('$\omega$/(rad/s)')
pic_4.legend(loc = 'best')
pic_4.text(2,2,'n=1000')

#pic_1.text(2, 11, 'damped pendulum',  size = 20)
#pic_1.text(2, 10.5, '$\Omega_D=2.0,F=0.2,q=0$',size = 20)
plt.show()


        
