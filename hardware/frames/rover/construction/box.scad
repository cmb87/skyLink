difference(){
  translate([-73/2,-58/2,0])cube([73,58,34]);
  translate([-70/2,-53/2,2])cube([70,53,40.01]);
  for (i=[0:3]) {
    translate([-73/2+7+i*20,40,14])rotate([90,0,0])cylinder(r=1.5,h=80,$fn=30);
  }
  
  for (i=[0:3]) {
    translate([-73/2+7+i*20,40,29])rotate([90,0,0])cylinder(r=1,h=80,$fn=30);
  }
  
  for (k=[1,-1]) {
    for (i=[0:5]) {
      translate([-73/2+12+i*10,-k*(58/2-7),-20])cylinder(r=1.5,h=40,$fn=30);
    }
  }
  
  for (i=[-20,-10,0,10,20]) {
    translate([-40,i,29])rotate([0,90,0])cylinder(r=1,h=80,$fn=30);
  }
  
}

