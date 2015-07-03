import numpy as np

# Generate Pointy Star-Shape Thingy

a = 2
b = 3

dt = 1.0/5
t  = np.arange(0,1,dt)

z = np.array((a*np.exp(2j*np.pi*t), b*np.exp(2j*np.pi*t)))
w = z.T.reshape(10)

# SVG Template

H = 300
W = 300
data = "\n".join([ "\t%s %s"%(int(x.real), int(x.imag)) for x in w])

print """<?xml version="1.0" standalone="no"?>
<svg width="%s" height="%s" version="1.1" xmlns="http://www.w3.org/2000/svg">

  <polygon points="\n%s"       stroke="#E09823" fill="transparent" stroke-width="2"/>


</svg>""" %(H,W,data)
