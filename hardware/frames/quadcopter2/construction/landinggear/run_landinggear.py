import numpy as np
import os
import matplotlib.pyplot as plt
from spline import Spline



cnpts = [
    [0,0],
    [25,0],
    [35,0],
    [45,-5],
    [55,-25],
    
    [53.5,-25],
    [45,-10], 
    [35,-3],
    [0,-3],

]




spline = Spline(cnpts, name="LandingGear")
spline.generate()
spline.plot(mirror=False, plot=False)

plt.axis("equal")
plt.show()
filename = 'landingGear.scad'

spline.linearExtrude(filename, z=15)

with open(filename, 'a') as f1:
    f1.write("LandingGear();\n")
