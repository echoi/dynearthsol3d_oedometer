#!/usr/bin/env python

from math import pi,sin, sqrt

K=200e6
mu=200e6
coh=1e6
phi=10*pi/180
psi=10.0*pi/180
ten=5.67e6
rho=1.0
vx=1e-5

e1=K+4.0*mu/3.0
e2=K-2.0*mu/3.0
sf=sin(phi)
nf=(1.0+sf)/(1.0-sf)
sp=sin(psi)
np=(1.0+sp)/(1.0-sp)
rl = (e1-e2*nf)/((e1+e2)*nf*np-2.0*e2*(nf+np)+2.0*e1)
step1 = 2.0*coh*sqrt(nf)/((e1-e2*nf)*vx)

fname="ydispl_Sxxa_psi%02d.dat" % (psi*180/pi)
fo=open(fname,"w")

Sxx = 0.0
for i in range(2001):
	if i > 0:
		#de = vx
		de = vx/(1-vx*i)
		if i < step1:
			Sxx = Sxx + e1*de
		else:
			Sxx = Sxx + de*(e1+2.0*rl*(e2*np-e1))
	if i%40==0:
		print >> fo, "%e %e" % (i*vx, Sxx)

fo.close()
		

