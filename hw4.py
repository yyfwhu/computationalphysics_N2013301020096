from pylab import *
v = []
t = []
dt = 0.1
v.append(0.)
t.append(0)
et = 10
for i in range(int(et/dt)):
	vn = v[i] + (10-v[i]) * dt
	v.append(vn)
	t.append(dt*(i+1))
	print v[i]

plot(v, color='blue', linewidth = 2.0,linestyle='-')

show()	





