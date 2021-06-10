import("raw_cone.stl");

difference(){
  union(){
    translate([0,0,-20])cylinder(r=8,h=20, $fn=30);
    translate([-41,-4,-2])cube([82,8,2]);
    rotate([0,0,90])
    translate([-41,-4,-2])cube([82,8,2]);
  }
  
  translate([0,0,-25])cylinder(r=6,h=55, $fn=30);
}


