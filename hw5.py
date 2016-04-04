#import pylab
from pylab import *
#define the empty list
Na = []
Nb = []
t = []
dt = 0.2
tau = 1
Na.append(200.)
Nb.append(0.)
t.append(0)
et = 5
#do the "for" circle
for i in range(int(et/dt)):
	Nan = Na[i] + (Nb[i]-Na[i]) * dt
	Nbn = Nb[i] + (Na[i]-Nb[i]) * dt
	Na.append(Nan)
	Nb.append(Nbn)
	t.append(dt*(i+1))
	print Nb[i]
	#print Na[i],and Nb[i]
#plot the picture
xlabel('Time',fontsize=20)
ylabel('Numble of Nuclei',fontsize=20)
title('Decay of Two Nuclei',fontsize=25)

plot(Na,'p--',Nb,'p--')

show()