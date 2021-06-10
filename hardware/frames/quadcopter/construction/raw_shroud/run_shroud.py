import numpy as np
import matplotlib.pyplot as plt
from spline import Spline



cnpts = [
    [40+27,10],
    [41+27,10],
    [43+27,28],
    [43+27,30+5],
    [40+27,29+5],
    [38+27,26+5],
    [38+27,10],
    [40+27,10],
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
