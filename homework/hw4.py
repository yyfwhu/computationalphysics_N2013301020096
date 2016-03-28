#import pylab
from pylab import *
#define the empty list
v = []
t = []
dt = 0.1
v.append(0.)
t.append(0)
et = 10
#do the "for" circle
for i in range(int(et/dt)):
	vn = v[i] + (10-v[i]) * dt
	v.append(vn)
	t.append(dt*(i+1))
	print v[i]

#plot the picture
plot(v, color='blue', linewidth = 2.0,linestyle='-')

show()	





