
difference(){
  union(){
    import("IdlerWheel.stl", convexity=9);
    translate([0,0,0])cylinder(r=4.5,h=13,$fn=40);
  }
  translate([0,0,-6])cylinder(r=2,h=28,$fn=40);
}

