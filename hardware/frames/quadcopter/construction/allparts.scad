createBracket = false;
createHolder = false;
createEnginePlatform = false;
mirrorHolder = false;
createLandingGear = false;
createShroudHolder = false;
createHardwareHolder = false;
createHardwareHolderLid = false;
createHardwareHolderPlatform = true;

plateLength = 25;
centralBodyWidth = 58;
centralBodyHeight = 12;
outerBodyWidth = 100;

profileWidth = 45;
profileHeight=6;

landingGearAttachementHolesWidth = 40;
landingGearAttachementHolesDia = 2;

centralCutOutWidth = 30;
centralCutOutHeight = 7;
cableHoleDiameter = 15;

armPlatformZOffset = 4 ; 
armBoltWidth = 70;
armBoltDistanceFac = 0.32;
armBoltInnerDia = 3;
armBoltOuterDia = 6;

armPlatformHeight = 4 ; 
armBearerDia=18;
armHolderHeight=25;
armHolderProfileHeight=8;
armAngle=20;

hardwareHolderWidth = 85;
hardwareHolderLength = 14;
hardwareHolderPlatformLength=70;

// ===================== HardwareHolder ===================================
module hardwareHolderOneSide(upperWallThck=5, lowerWallThk=6, createBrackets=true) {
  
  rd = 6;  
  rdi = 4;
  rdo = 2.5;
    
  x = hardwareHolderLength;
  r = hardwareHolderLength/2;
  y = hardwareHolderWidth/2 - r;
  
  y1 = profileWidth/2 + profileHeight/2;
  dy = profileHeight + upperWallThck;
  dy2  = dy+lowerWallThk;
  
  x2 = hardwareHolderLength*0.26;
  y2 = y1 - 0.5*profileHeight-0.25*upperWallThck;
  y3 = y1 + 0.5*profileHeight+0.25*upperWallThck;
    
  color("green")
  difference(){
    union(){
      translate([-x/2,0,-2])cube([x,y,2]);
      translate([0,y,-2])cylinder(r=r, h=2, $fn=20);
      
      if (createBrackets) {
        hull(){  
          translate([-x/2,y1-dy/2,0])cube([x,dy,profileHeight]);
          translate([-x/2,y1-dy2/2,-1])cube([x,dy2,1]);
        }
      }
      translate([0,y,0])cylinder(r=rd, h=4, $fn=20);
    }
    
    translate([0,y,-2.1])cylinder(r=rdi, h=3, $fn=20);
    translate([0,y,-2.1])cylinder(r=rdo, h=10, $fn=20);

    if (createBrackets) {
      translate([-(x-8)/2,-0.01,-3])cube([(x-8),0.4*y,4]);
      translate([0,0.4*y,-3])cylinder(r=(x-8)/2,h=4, $fn=20);
      translate([x2,y2,-5])cylinder(r=0.5, h=20, $fn=25);
      translate([x2,y3,-5])cylinder(r=0.5, h=20, $fn=25);
      translate([-x2,y2,-5])cylinder(r=0.5, h=20, $fn=25);
      translate([-x2,y3,-5])cylinder(r=0.5, h=20, $fn=25);
      translate([0,0,profileHeight+3+0.01])railCutOut();
    } else {
      translate([-(x-5)/2,-0.01,-3])cube([(x-5),0.8*y,4]);
      translate([0,0.8*y,-3])cylinder(r=(x-5)/2,h=4, $fn=20);
    }
  };
}

module hardwareHolder() {
   union(){
     hardwareHolderOneSide();
     mirror([0,1,0])hardwareHolderOneSide();   
   }
}

module hardwareHolderLid(upperWallThck=5) {
  x = hardwareHolderLength;
  r = hardwareHolderLength/2;
  y = hardwareHolderWidth/2 - r;
    
  y1 = profileWidth/2 + profileHeight/2;
  dy = profileHeight + upperWallThck;

  x2 = hardwareHolderLength*0.26;
  y2 = y1 - 0.5*profileHeight-0.25*upperWallThck;
  y3 = y1 + 0.5*profileHeight+0.25*upperWallThck;
    
  translate([0,0,10])color("red")
  difference(){
    translate([-x/2,y1-dy/2,0])cube([x,dy,1.6]);
      
    translate([x2,y2,-5])cylinder(r=0.5, h=20, $fn=25);
    translate([x2,y3,-5])cylinder(r=0.5, h=20, $fn=25);
    translate([-x2,y2,-5])cylinder(r=0.5, h=20, $fn=25);
    translate([-x2,y3,-5])cylinder(r=0.5, h=20, $fn=25);
    translate([0,y1,-5])cylinder(r=3, h=20, $fn=25); 
      
  };
}

module hardwareHolderPlatformOneSide(upperWallThck=5, lowerWallThk=6) {
  
  rd = 6;  
  rdi = 4;
  rdo = 2.5;
    
  x = hardwareHolderLength+5;
  r = x/2;
  y = hardwareHolderWidth/2 - 7;
  
  y1 = profileWidth/2 + profileHeight/2;
  dy = profileHeight + upperWallThck;
  dy2  = dy+lowerWallThk;
  
  x2 = hardwareHolderLength*0.26;
  y2 = y1 - 0.5*profileHeight-0.25*upperWallThck;
  y3 = y1 + 0.5*profileHeight+0.25*upperWallThck;
    
  color("green")
  difference(){
    union(){
      translate([-x/2,0,-2])cube([x,y,2]);
      translate([0,y,-2])cylinder(r=r, h=2, $fn=20);
      
      if (createBrackets) {
        hull(){  
          translate([-x/2,y1-dy/2,0])cube([x,dy,profileHeight]);
          translate([-x/2,y1-dy2/2,-1])cube([x,dy2,1]);
        }
      }
      translate([0,y,-5])cylinder(r=rd, h=4, $fn=20);
      
      hull(){
        translate([-19/2,31,-7])cube([19,1,5]);
        translate([0,y,-3])cylinder(r=r, h=1, $fn=20);
      }
      
      translate([-19/2,-1,-7])cube([19,2,5]);
      
    };
    
    translate([0,y,-2.1-10-3])cylinder(r=rdi, h=3+10, $fn=20);
    translate([0,y,-2.1-5])cylinder(r=rdo, h=100, $fn=20);
    translate([-50,1,-7])cube([100,30,5]);


  };
  
}


module hardwareHolderPlatform(panelWidth=7,nholes=13, outerPanelWidth=28){
   union(){
     hardwareHolderPlatformOneSide();
     mirror([0,1,0])hardwareHolderPlatformOneSide();   
   }

}

// ===================== Shroud Holder====================================
module shroudHolder() {
    
   x = armHolderProfileHeight+0.18;
    
   difference(){
   union(){
       hull(){
         translate([-1.3*x/2,0,-x-2])cube([1.3*x,20,2]);
         translate([-18/2,0,0])cube([18,20,2]);
       }
       hull(){ 
         translate([-18/2,0,2])cube([18,20,6]);
         translate([-8/2,0,2])cube([8,20,9]);
       }
   }
   translate([-x/2,-25,-x])cube([x,50,x]);
   translate([-14/2,-25,2])cube([14,50,5]);
   translate([-6/2,-25,2])cube([6,50,7]);
    translate([0,5,-5])cylinder(r=1.5,h=50,$fn=20);
    translate([0,15,-5])cylinder(r=1.5,h=50,$fn=20);
   }
   
   
   
   
}

// ===================== Landing Gear====================================

module landingGear() {
   color("yellow")
   difference(){
   rotate([0,0,90])
   rotate([-180,0,0])
   translate([0,0,centralBodyHeight]) import("landingGear.stl");
     RailFixHoles();
     mirror([0,1,0])RailFixHoles();
   };
    
}


// ===================== Engine Platform ====================================

module enginePlatform(length=10, transition=9, thickness=6) {
  armHolderProfileHeight2 =armHolderProfileHeight+0.1;
    
  difference(){
    union(){
      translate([-10,-10,-3])cube([20,20,3]);
      
      dy = armHolderProfileHeight2+thickness;
        
      translate([-dy/2,-length-transition-10,-dy])cube([dy,length,dy]);
      
      hull(){
        translate([-10,-10,-3])cube([20,1,3]);
        translate([-dy/2,-transition-10,-dy])cube([dy,1,dy]);
      };
      hull(){
        translate([-armHolderProfileHeight2/2-1,-transition-25,-armHolderProfileHeight2-thickness/2-1])cube([armHolderProfileHeight2+2,1,armHolderProfileHeight2+2]);
        translate([-dy/2,-transition-20,-dy])cube([dy,1,dy]);
          
      };
    };
  
    // Motor Holes
    translate([0,0,-5])cylinder(r=4,h=50, $fn=20);
    translate([0-6,-6,-5])cylinder(r=2,h=50, $fn=20);
    translate([0-6,6,-5])cylinder(r=2,h=50, $fn=20);
    translate([0+6,6,-5])cylinder(r=2,h=50, $fn=20);
    translate([0+6,-6,-5])cylinder(r=2,h=50, $fn=20);
    translate([0-5,-5,-5])cylinder(r=2,h=50, $fn=20);
    translate([0-5,5,-5])cylinder(r=2,h=50, $fn=20);
    translate([0+5,5,-5])cylinder(r=2,h=50, $fn=20);
    translate([0+5,-5,-5])cylinder(r=2,h=50, $fn=20);

    
    translate([-armHolderProfileHeight2/2,-length-transition-15-2,-armHolderProfileHeight2-thickness/2])cube([armHolderProfileHeight2,100,armHolderProfileHeight2]);
    
    translate([0,-transition-length/2-10,-15])cylinder(r=0.8,h=30, $fn=20);
    
  };
  
}



// ===================== ARM New ====================================
//------------------------------

//------------------------------
// Arm Base
module armPlatformBottom(fillet=4){
    
  y1 = (outerBodyWidth-plateLength)/2;
  //translate([0,y1,armPlatformZOffset])cylinder(r=plateLength/2, h=armPlatformHeight, $fn=6);
    
  dy = (y1 - profileWidth/2)-2;
  z0 = armPlatformZOffset+armPlatformHeight;
  dx = armBoltDistanceFac*plateLength;
  y0 = (outerBodyWidth-armBearerDia)/2;
    
  hull(){
    translate([-plateLength/2,profileWidth/2+2,armPlatformZOffset])cube([plateLength, dy, armPlatformHeight]); 

    translate([dx,armBoltWidth/2, z0])cylinder(r=0.75*armBoltOuterDia,h=fillet, $fn=20);
    translate([-dx,armBoltWidth/2, z0])cylinder(r=0.75*armBoltOuterDia,h=fillet, $fn=20);
    translate([0,y0, z0])cylinder(r=armBearerDia/2,h=fillet, $fn=30);
      
  }
}
// ------------------------------------
module armPlatformHead(){
    z0 = armPlatformZOffset+armPlatformHeight;
    z1 = armHolderHeight + z0;
    translate([0,0,z1])mirror([0,0,1])armPlatformBottom();
    
}
// ------------------------------------
module armPlatformMiddle(){    
  z0 = armPlatformHeight;
  dx = armBoltDistanceFac*plateLength;
  y0 = (outerBodyWidth-armBearerDia)/2;

  translate([dx,armBoltWidth/2, z0])cylinder(r=0.75*armBoltOuterDia,h=armHolderHeight-1, $fn=20);
  translate([-dx,armBoltWidth/2, z0])cylinder(r=0.75*armBoltOuterDia,h=armHolderHeight-1, $fn=20);
  translate([0,y0, z0])cylinder(r=armBearerDia/2,h=armHolderHeight, $fn=30);
}

// ------------------------------------
module armAttachmentHole(){    
    
  y0 = (outerBodyWidth-armBearerDia)/2;
  z0 = -armHolderProfileHeight/2 +armHolderHeight/2 + armPlatformHeight;
    
  translate([0,y0,0])rotate([0,0,armAngle])translate([-armHolderProfileHeight/2,-(armBearerDia)/2,z0])cube([armHolderProfileHeight,100,armHolderProfileHeight]);
}


// ------------------------------------
module armAttachmentHoleFillet(innerFac=1.85, outerFac=1.2, length=10){   
  y0 = (outerBodyWidth-armBearerDia)/2;
    
  dzi = innerFac*armHolderProfileHeight;
  dzo = outerFac*armHolderProfileHeight;
    
  z0i = -dzi/2 +armHolderHeight/2 + armPlatformHeight;
  z0o = -dzo/2 +armHolderHeight/2 + armPlatformHeight;
  
  hull(){
  translate([0,y0,0])rotate([0,0,armAngle])translate([-dzi/2,(armBearerDia)/4,z0i])cube([dzi,1,dzi]);
    
  translate([0,y0,0])rotate([0,0,armAngle])translate([-dzo/2,(armBearerDia)/4+length,z0o])cube([dzo,1,dzo]);
  };
      
}



//------------------------------
// Assemble Arm
module assembleArmOneSideNew(){
  color("red"){
  difference(){
    union(){
      armPlatformBottom();
      armPlatformMiddle();
      armPlatformHead();
      armAttachmentHoleFillet();
    };
    ArmBoltHoles();
    armAttachmentHole();
  }}
}






// ===================== BRACKET ====================================
//------------------------------
// Main Bracket
module centralBodyBlock(){
    
  union(){
    translate([-plateLength/2,0,-centralBodyHeight])cube([plateLength,centralBodyWidth/2, centralBodyHeight]);
        
    // Outer wings for arm attachment bolts
    dy = (outerBodyWidth-plateLength)/2;
    hull(){
      translate([0,dy,-3])cylinder(r=plateLength/2, h=3, $fn=6);
      translate([-plateLength/2,centralBodyWidth/2-1,-centralBodyHeight])cube([plateLength,1, centralBodyHeight]);
    };
    
  };   
 };
 
//------------------------------
// Arm Platform
 module armPlatform(){
  y1 = (outerBodyWidth-plateLength)/2;
  translate([0,y1,0])cylinder(r=plateLength/2, h=armPlatformZOffset, $fn=6);

  dy = (y1 - profileWidth/2);
  translate([-plateLength/2,profileWidth/2,0])cube([plateLength, dy, armPlatformZOffset]);
  
  z = armPlatformZOffset + armPlatformHeight;
     
  hull(){
    translate([-plateLength/2,profileWidth/2,0])cube([plateLength, 2, z]);
     
    translate([-plateLength/2,profileWidth/2-5,-1])cube([plateLength, 5, 1]);
  }
 };
 
//------------------------------
// CFK profile cutout
module railCutOut() {
  z = -0.5*(profileHeight+centralBodyHeight);
  translate([-50,profileWidth/2,z])cube([100,profileHeight, profileHeight]);
}

//------------------------------
// Rail fix Holes
module RailFixHoles() {
  dy = 0.5*(profileWidth+profileHeight);
  translate([0,dy, -centralBodyHeight-10])cylinder(r=1 ,h=centralBodyHeight-1+9, $fn=20);
}

//------------------------------
// Central cutout
module centralCutOut() {
  dy = (centralCutOutWidth-centralCutOutHeight)/2 +2;
  z = -0.5*(centralCutOutHeight+centralBodyHeight);
  translate([-50,-1, z])cube([100, dy+1, centralCutOutHeight]);
    
  z1 = z+centralCutOutHeight/2;
  translate([-50,dy, z1])rotate([0,90,0])cylinder(r=centralCutOutHeight/2,h=100, $fn=20);
}
 
//------------------------------
// Central cutout
module CabelHole() {
  z = 0.5*(centralCutOutHeight + centralBodyHeight);
  translate([0,0, -z])cylinder(r=cableHoleDiameter/2,h=100, $fn=20);
}
 

//------------------------------
// LandingGearAttachment Holes
module LandingGearAttachmentHoles() {
 
  dx = armBoltDistanceFac*plateLength;
    
  translate([dx,landingGearAttachementHolesWidth/2, -centralBodyHeight-1])cylinder(r=landingGearAttachementHolesDia/2,h=centralBodyHeight, $fn=20);
  translate([-dx,landingGearAttachementHolesWidth/2, -centralBodyHeight-1])cylinder(r=landingGearAttachementHolesDia/2,h=centralBodyHeight, $fn=20);

}



//------------------------------
// Arm Bolt Holes
module ArmBoltHoles() {
 
//armBoltWidth = 40;
//armBoltInnerDia = 3;
//armBoltOuterDia = 6;
    
  dx = armBoltDistanceFac*plateLength;
    
  translate([dx,armBoltWidth/2, -50])cylinder(r=armBoltInnerDia/2,h=100, $fn=20);
  translate([-dx,armBoltWidth/2, -50])cylinder(r=armBoltInnerDia/2,h=100, $fn=20);
  translate([dx,armBoltWidth/2, -10])cylinder(r=armBoltOuterDia/2,h=10, $fn=20);
  translate([-dx,armBoltWidth/2, -10])cylinder(r=armBoltOuterDia/2,h=10, $fn=20);
    
  y0 = (outerBodyWidth-armBearerDia)/2;
  translate([0,y0, -50])cylinder(r=armBoltInnerDia/2,h=100, $fn=20);
  translate([0,y0, -10])cylinder(r=armBoltOuterDia/2,h=10, $fn=20);
}

// ========================================
//------------------------------
// Assemble One Side
module assembleBracketOneSide(){
  difference(){
    union(){
      centralBodyBlock();
      armPlatform();
    };
    railCutOut();
    centralCutOut();
    CabelHole();
    ArmBoltHoles();
    LandingGearAttachmentHoles();
    RailFixHoles();
  }
}


// ========================================
//------------------------------
// Mirror Assembly
module assembleBracketMirror(){
  union(){
    assembleBracketOneSide();
    mirror([0,1,0])assembleBracketOneSide();
  }    
}


//------------------------------

if (createBracket) {
  assembleBracketMirror();
}

if (createHolder) {
  if (mirrorHolder) {
    mirror([0,1,0])assembleArmOneSideNew();
  } else {
    assembleArmOneSideNew();
  }
}

if (createEnginePlatform) {
  enginePlatform();
}

if (createLandingGear) {
  landingGear();
}

if (createShroudHolder){
  shroudHolder();
}

if (createHardwareHolder){
    hardwareHolder();
};

if (createHardwareHolderLid){
    hardwareHolderLid();
};
      
if (createHardwareHolderPlatform){
    hardwareHolderPlatform();
};
    