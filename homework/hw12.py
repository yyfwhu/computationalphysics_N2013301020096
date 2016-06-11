'''
This program is aim to caculate the two planet driven by the gravity
author Yao Yifei
'''

#print 'ok'
from pylab import *
import mpl_toolkits.mplot3d



x_1 = []
y_1 = []
z_1 = []

x_2 = []
y_2 = []
z_2 = []
#print 'ok'
class solar:
    def __init__(self, q = 0., et = 50,  m_1 = 4*pi , m_2 = 2*pi, pos_1 =array([1.,1.,0.]), pos_2 = array([3.,1.,0.]), v_1 = array([0.,1.,0.]), v_2 = array([0.,0.,0.]), dt = .0001 ):
        self.m_1 = m_1
        self.m_2 = m_2
        self.q = q
        self.n = int(et / dt)
        self.dt = dt
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.v_1 = v_1
        self.v_2 = v_2

        self.x_1 = []
        self.y_1 = []
        self.z_1 = []

        self.x_2 = []
        self.y_2 = []
        self.z_2 = []
    def update(self):
        print self.n
        for i in range(self.n):



            self.F_1 = self.m_1 * self.m_2 * (self.pos_2 - self.pos_1)/(inner(self.pos_1-self.pos_2, self.pos_1 - self.pos_2) ** ((3. + self.q) / 2.))
            self.F_2 = self.m_1 * self.m_2 * (self.pos_1 - self.pos_2)/(inner(self.pos_1-self.pos_2, self.pos_1 - self.pos_2) ** ((3. + self.q) / 2.))
            self.a_1 = self.F_1/self.m_1
            self.a_2 = self.F_2/self.m_2
            self.v_1 +=self.a_1 * self.dt
            self.v_2 +=self.a_2 * self.dt
            self.pos_1 +=self.v_1 * self.dt
            self.pos_2 +=0

            self.x_1.append(self.pos_1[0])
            self.y_1.append(self.pos_1[1])
            self.z_1.append(self.pos_1[2])

            self.x_2.append(self.pos_2[0])
            self.y_2.append(self.pos_2[1])
            self.z_2.append(self.pos_2[2])          
    def plot(self,pic):
        pic.plot(self.x_1,self.y_1,'g-',label = 'planet $M_1$')
        pic.plot(self.x_2,self.y_2,'r.',label = 'planet $M_2$')
        pic.set_xlabel('x',size =20 )
        pic.set_ylabel('y',size =20 )
        pic.set_title(' Two planet system ',size = 25)
        pic.text(2.8,-0.25,'q=' + str(self.q),size = 20)

pic_1 = subplot(2,2,1)
s = solar(.0) 
s.update()
s.plot(pic_1)
legend(loc = 'best')

pic_1 = subplot(2,2,2)
s = solar(.1) 
s.update()
s.plot(pic_1)
legend(loc = 'best')

pic_1 = subplot(2,2,3)
s = solar(.5) 
s.update()
s.plot(pic_1)
legend(loc = 'best')

pic_1 = subplot(2,2,4)
s = solar(1.) 
s.update()
s.plot(pic_1)
legend(loc = 'best')

show()












 