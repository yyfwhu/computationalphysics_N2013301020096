'''
program Lorenze model
Author: Yao Yifei   Last Modify:20160520
'''
import math 
from pylab import *
import mpl_toolkits.mplot3d
sig = 10
b = 8./3.
#print b

class lorenze:
    def __init__(self, r = 5,et = 0.01,  x = 1, y = 0, z = 0, dt = 0.01 ):
        self.x = [x]
        self.y = [y]
        self.z = [z]
        self.t = [0]
        self.r = r
        self.dt = dt
        self.et = et
        self.n = int(self.et / self.dt)
    def update(self):
        for i in range(self.n):
            self.t.append(self.t[-1] + self.dt)
            self.x.append(self.x[-1] + sig * (self.y[-1] -self.x[-1]) * self.dt)
            self.y.append(self.y[-1] + (-self.x[-1] * self.z[-1] + self.r * self.x[-1] - self.y[-1]) * self.dt)
            self.z.append(self.z[-1] + (self.x[-1] * self.y[-1] - b * self.z[-1]) * self.dt) 
        
    def plzt(self, pic):
        pic.plot(self.t, self.z, label = 'n=' + str(self.n))
        pic.legend(loc = 'best')

    def plzx(self, pic):
        pic.plot(self.x, self.z, '.', label ='r=' + str(self.r))
        pic.set_title('Z versus X')
        pic.legend(loc = 'best')
        pic.set_xlabel('X')
        pic.set_ylabel('Z')



    def plzx1(self, pic):
        pic.plot(self.x, self.z, '.', label = 'r=' + str(self.r))
        pic.set_title('Z versus X')
        pic.legend(loc = 'best')
        pic.set_xlabel('X')
        pic.set_ylabel('Z')
    
    def plzy(self, pic):
        pic.plot(self.y, self.z,label = 'r=' + str(self.r))
        pic.set_title('Z versus Y')
        pic.legend(loc = 'best')
        pic.set_xlabel('Y')
        pic.set_ylabel('Z')

    def plyx(self, pic):
        pic.plot(self.y, self.x, label = 'r=' + str(self.r))
        pic.set_title('Y versus X')
        pic.legend(loc = 'best')
        pic.set_xlabel('X')
        pic.set_ylabel('Y')

    def plxyz(self, pic):
        plot(self.y, self.x, self.z, ',', label = 'r=' + str(self.r))
        pic.set_title('X-Y-Z')
        pic.legend(loc = 'best')
        pic.set_xlabel('X')
        pic.set_ylabel('Y')
        pic.set_zlabel('Z')

pic1 = subplot(1,1,1,projection = '3d')
s = lorenze(29, 100)
s.update()
s.plxyz(pic1)

#pic1 = subplot(222)
#s = lorenze(29, 50)
#s.update()
#s.plzx(pic1)

#pic1 = subplot(224)
#s = lorenze(29, 50)
#s.update()
#s.plzy(pic1)

#pic1 = subplot(223)
#s = lorenze(29, 50)
#s.update()
#s.plyx(pic1)

#pic1 = subplot(221)
#s = lorenze(29, 50)
#s.update()
#s.plzx1(pic1)


show()

