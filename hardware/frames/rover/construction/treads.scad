driveWheel = [0,24,0];
idlerWheel1 = [25,0,0];
idlerWheel2 = [25+73,0,0];
rearpoint  = [25+73-20, 23, 0];
bodyWidth = 100;

nholes = 5;

module side(){
  difference(){
  union(){
    hull(){
      translate(driveWheel)cylinder(r=15,h=3,$fn=6);
      translate(idlerWheel1)cylinder(r=5,h=3,$fn=6);
      translate(idlerWheel2)cylinder(r=5,h=3,$fn=6);
      translate(rearpoint)cylinder(r=1,h=3,$fn=6);
    };
  
    translate([0, 0,0])translate(driveWheel)cylinder(r=15,h=52,$fn=6);
    translate([0, 0,0])translate(idlerWheel1)cylinder(r=5,h=8,$fn=30);
    translate([0, 0,0])translate(idlerWheel2)cylinder(r=5,h=8,$fn=30);
    
    // Alignment rail
    translate([7, 11,3])cube([idlerWheel2[0]-idlerWheel1[0],5,15]);
    

  }
  // Differences
  translate([0, 0,3])translate(driveWheel)cylinder(r=10.9,h=55,$fn=30);
  translate([0, 0,9])translate(driveWheel)cylinder(r=11,h=55,$fn=30);
  translate([0,0,-5])translate(driveWheel)cylinder(r=3.55,h=15,$fn=30);
  translate([0, 7.5,-5])translate(driveWheel)cylinder(r=1,h=15,$fn=30);
  translate([0,-7.5,-5])translate(driveWheel)cylinder(r=1,h=15,$fn=30);
    
  translate([0, 0 ,-5])translate(idlerWheel1)cylinder(r=2,h=15,$fn=30);
  translate([0,0,-0.01])translate(idlerWheel1)cylinder(r=4,h=2.2,$fn=6);
  translate([0,0,4])translate(idlerWheel1)cylinder(r=2.75,h=2.8,$fn=30);
  
  translate([0, 0 ,-5])translate(idlerWheel2)cylinder(r=2,h=15,$fn=30);
  translate([0,0,-0.01])translate(idlerWheel2)cylinder(r=4,h=2.2,$fn=6);
  translate([0,0,4])translate(idlerWheel2)cylinder(r=2.75,h=2.8,$fn=30);
  // Attachement Holes
  
  for (i = [0:3]){
   x = idlerWheel1[0] + i*10 +20 ;
   translate([x, 5, -0.1])
   cylinder(r=1.5,h=28, $fn=30);
  }

  for (i = [0:nholes]){
   x = idlerWheel1[0] + i*10;
   //translate([x, 18, -0.1])
   translate([x, 18, 10])
   rotate([90,0,0])
   cylinder(r=1.5,h=28, $fn=30);
  }


  }
}


translate([0,0,-bodyWidth/2])side();
//translate([0,0,bodyWidth/2])mirror([0,0,1])side();
