'''
This program is aim to caculate the two planet driven by the gravity
author Yao Yifei
date 2016.6.10
'''
from pylab import *
import mpl_toolkits.mplot3d

x = []
y = []
z = []
Energy = []
time = []

class mov:
    def __init__(self,  E = array([5., 0., 0.]) , B = array([2.,0.,5]) ,g = array([0.,0.,0.]),


    pos = array([1.,0.,0.]), v = array([-7., 1., 0.]),

    q = 1.,  m = 2., dt = 0.0001, et = 10. ):

        self.q = q
        self.v = v
        self.E = E
        self.B = B
        self.g = g
        self.pos = pos

        self.m = m
        self.dt = dt
        self.n = int(et/dt)
        self.Energy = 0.5 * self.m * inner(self.v, self.v)
    def update(self):

        for i in range(self.n):
            self.F = self.q * (self.E + cross(self.v, self.B)) + self.m * self.g
            self.a = self.F / self.m
            self.v += self.a * self.dt
            self.pos += self.v  * self.dt
            x.append(self.pos[0])
            y.append(self.pos[1])
            z.append(self.pos[2])
            self.t = self.dt * self.n
            Energy.append(self.Energy)
            time.append(self.t)

    def pl(self, pic):
        pic.plot(x,y,z,'b-',label = 'q in magnetic filed')
        pic.set_xlabel('X/m', size = 20)
        pic.set_ylabel('Y/m', size = 20)
        pic.set_zlabel('Z/m',size = 20)
        pic.set_title('with magnetic filed',size = 25)
        #pic.text(1.4,0,'. B',size = 20)

    def plE(self,pic):
        pic.plot(Energy,time,'r-',label = 'Energy')
        pic.set_xlabel('time',size = 20)
        pic.set_ylabel('Energy',size = 20)
        pic.set_title('with magnetic and filed',size = 25)


pic1 = subplot(1,1,1,projection = '3d')

s = mov()
s.update()
s.pl(pic1)

#xlim(0,2)
#ylim(-1,1)
legend(loc = 'lower right')
#text(1000,-20,'n = 50000',size = 20)
#annotate("E",(30.,4.1),(20.,4.),size = 20,arrowprops=dict(arrowstyle="->"))

'''pic1 = subplot(1,2,2)
s = mov()
s.update()
s.plE(pic1)
legend(loc = 'best')
'''

show()




