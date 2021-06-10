
difference(){
  import("DriveWheel.stl", convexity=9);
  translate([0,0,-6])cylinder(r=4.55,h=28,$fn=40);
  translate([0,-20,2.5])rotate([-90,0,0])cylinder(r=1.7,h=40, $fn=32);
}

difference(){
  translate([0,0,0])cylinder(r=7,h=19,$fn=40);
  translate([0,0,-6])cylinder(r=4.6,h=28,$fn=40);
  translate([0,-20,2.5])rotate([-90,0,0])cylinder(r=1.7,h=40, $fn=32);
}   

