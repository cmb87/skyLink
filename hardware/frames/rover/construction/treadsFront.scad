driveWheel = [0,24,0];
idlerWheel1 = [25,0,0];
idlerWheel2 = [25+73,0,0];
rearpoint  = [25+73-20, 23, 0];
bodyWidth = 100;

nholes = 6;

chainDistance = 23;

module side(){
  difference(){
  union(){
    hull(){
      translate(driveWheel)cylinder(r=15,h=3,$fn=6);
      translate(idlerWheel1)cylinder(r=5,h=3,$fn=6);
      translate(idlerWheel2)cylinder(r=5,h=3,$fn=6);
      translate(rearpoint)cylinder(r=1,h=3,$fn=6);
    };
  

    translate([45,0,0])cube([30,10,chainDistance]);
    translate([45,5,0])cylinder(r=5,h=chainDistance);
    translate([75,5,0])cylinder(r=5,h=chainDistance);
    
    translate(idlerWheel1)cylinder(r=3,h=5,$fn=16);
    translate(idlerWheel2)cylinder(r=3,h=5,$fn=16);
    
  }
  // Differences
  translate([0,0,-5])translate(driveWheel)cylinder(r=3.55,h=15,$fn=30);

    
  translate([0, 0 ,-5])translate(idlerWheel1)cylinder(r=1.5,h=15,$fn=30);
  translate([0, 0 ,-5])translate(idlerWheel2)cylinder(r=1.5,h=15,$fn=30);

  // Attachement Holes
  
  for (i = [0:3]){
   x = idlerWheel1[0] + i*10 +20 ;
   translate([x, 5, -0.1])
   cylinder(r=1.5,h=28, $fn=30);
  }


  }
}

translate([0,0,-bodyWidth/2])side();
//translate([0,0,bodyWidth/2])mirror([0,0,1])side();
