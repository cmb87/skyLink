driveWheel = [0,15,0];
idlerWheel1 = [28,0,0];
idlerWheel2 = [75,0,0];
idlerWheel3 = [103,15,0];

wheeldiameter=30;
bodyWidth = 100;

nholes = 5;

module side(){
  difference(){
  union(){
    hull(){
      translate(driveWheel)cylinder(r=15,h=3,$fn=6);
      translate(idlerWheel1)cylinder(r=5,h=3,$fn=6);
      translate(idlerWheel2)cylinder(r=5,h=3,$fn=6);
      translate(idlerWheel3)cylinder(r=15,h=3,$fn=6);
    };
  
    translate([0, 0,0])translate(idlerWheel1)cylinder(r=5,h=6,$fn=30);
    translate([0, 0,0])translate(idlerWheel2)cylinder(r=5,h=6,$fn=30);
    translate([0, 0,0])translate(idlerWheel3)cylinder(r=5,h=6,$fn=30); 


    translate([105/2-20,16,0])cube([40,8,24]);
    translate([105/2-20,20,0])cylinder(r=4,h=24,$fn=20);
    translate([105/2+20,20,0])cylinder(r=4,h=24,$fn=20);

  }
  // Differences
  translate([0, 0 ,-5])translate(driveWheel)cylinder(r=1.5,h=15,$fn=30);
  translate([0, 0 ,6])translate(driveWheel)cylinder(r=2.5,h=15,$fn=30);
  translate([0,0,-0.01])translate(driveWheel)cylinder(r=3.5,h=2.2,$fn=6);

    
  translate([0, 0 ,-5])translate(idlerWheel1)cylinder(r=1.5,h=15,$fn=30);
  translate([0, 0 ,6])translate(idlerWheel1)cylinder(r=2.5,h=15,$fn=30);
  translate([0,0,-0.01])translate(idlerWheel1)cylinder(r=3.5,h=2.2,$fn=6);

  translate([0, 0 ,-5])translate(idlerWheel2)cylinder(r=1.5,h=15,$fn=30);
  translate([0, 0 ,6])translate(idlerWheel2)cylinder(r=2.5,h=15,$fn=30);
  translate([0,0,-0.01])translate(idlerWheel2)cylinder(r=3.5,h=2.2,$fn=6);
  
  translate([0, 0 ,-5])translate(idlerWheel3)cylinder(r=1.5,h=15,$fn=30);
  translate([0,0,-0.01])translate(idlerWheel3)cylinder(r=3.5,h=2.2,$fn=6);
  translate([0, 0 ,6])translate(idlerWheel3)cylinder(r=2.5,h=15,$fn=30);

  
  //


  
  
  // Attachement Holes
  
  for (i = [0:3]){
   x =  51.5 -30 +i*20 ;
   translate([x, 20, -0.1])
   cylinder(r=1.5,h=28, $fn=30);
  }

  translate([51.5 -10, 20, -0.10])cylinder(r=2.6,h=5, $fn=30);
  translate([51.5 +10, 20, -0.10])cylinder(r=2.6,h=5, $fn=30);

  }
}


translate([0,0,-bodyWidth/2])side();
//translate([0,0,bodyWidth/2])mirror([0,0,1])side();
