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
  
    translate([0, 0,0])translate(driveWheel)cylinder(r=15,h=54,$fn=6);
    translate([0, 0,0])translate(idlerWheel1)cylinder(r=5,h=8,$fn=30);
    translate([0, 0,0])translate(idlerWheel2)cylinder(r=5,h=8,$fn=30);
    
    difference(){
      translate([0, 0,0])translate(idlerWheel3)cylinder(r=15,h=11,$fn=6);
      translate([0, 0,3])translate(idlerWheel3)cylinder(r=10.6,h=56,$fn=30);
    }
    
    difference(){
      translate([0, 0,0])translate(idlerWheel3)cylinder(r=10.6,h=13,$fn=30);
      translate([0, 0,3])translate(idlerWheel3)cylinder(r=9,h=55,$fn=30);
    }
    
    
    translate([0, 0,0])translate(idlerWheel3)cylinder(r=5,h=8,$fn=30); 
    //
    // Alignment rail
    x = idlerWheel3[0]-wheeldiameter;
    translate([wheeldiameter/2, 3,3])cube([x,3,15]);
    

  }
  // Differences
  translate([0, 0,3])translate(driveWheel)cylinder(r=11,h=55,$fn=30);
  translate([0, 0,9])translate(driveWheel)cylinder(r=11,h=55,$fn=30);
  translate([0,0,-5])translate(driveWheel)cylinder(r=3.55,h=15,$fn=30);
  translate([0, 7.5,-5])translate(driveWheel)cylinder(r=1,h=15,$fn=30);
  translate([0,-7.5,-5])translate(driveWheel)cylinder(r=1,h=15,$fn=30);
    
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

  for (i = [0:nholes]){
   x = 51.5 -25 +i*10 ;
   //translate([x, 18, -0.1])
   translate([x, 18, 10])
   rotate([90,0,0])
   cylinder(r=1.5,h=28, $fn=30);
  }


  }
}


translate([0,0,-bodyWidth/2])side();
//translate([0,0,bodyWidth/2])mirror([0,0,1])side();
