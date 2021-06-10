import numpy as np
import matplotlib.pyplot as plt
from spline import Spline



cnpts = [
    [23,0],
    [30,15],
    [40,25],
    [45,25],
    [25,0],
]




spline = Spline(cnpts, name="Shroud")
spline.generate()
spline.plot(mirror=True)




filename = 'shroud.scad'

spline.rotateExtrude(filename)

with open(filename, 'a') as f1:

    f1.write("difference(){\n")
    f1.write("  union(){\n")
    f1.write("    hull(){\n")
    f1.write("      translate([-4,65,10])cube([8,25,3]);\n")
    f1.write("      translate([-25/2,65,10])cube([25,3,20]);\n")
    f1.write("    }\n")
    f1.write("    rotate([0,-90,0])Shroud();\n")
    f1.write("  }\n")
    f1.write("  translate([0,65+10,-10])cylinder(r=1.5,h=50,$fn=20);\n")
    f1.write("  translate([0,65+20,-10])cylinder(r=1.5,h=50,$fn=20);\n")
    f1.write("  translate([0,65+10,14])cylinder(r=3,h=50,$fn=20);\n")
    f1.write("  translate([0,65+20,14])cylinder(r=3,h=50,$fn=20);\n")
    f1.write("\n}")
