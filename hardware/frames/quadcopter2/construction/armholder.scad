pdx1 = 5;
pdx2 = 8;
pdxm = 13;

t = 1;
tol = 0.2;
x1 = 50;
x2 = 20;
y1 = 26;

arot = 10;

difference(){
union(){
    hull(){
      translate([-x1/2,-pdx1/2-t,-pdx1/2-t])cube([1,pdx1+2*t,pdx1+2*t]);
      translate([-x2/2,-pdxm/2-t,-pdxm/2-t])cube([1,pdxm+2*t,pdxm+2*t]);
        
    };
    hull(){
      translate([-x2/2,-pdxm/2-t,-pdxm/2-t])cube([1,pdxm+2*t,pdxm+2*t]);
      translate([+x1/2,-pdx1/2-t,-pdx1/2-t])cube([1,pdx1+2*t,pdx1+2*t]);  
      translate([+x2/2,-pdxm/2-t,-pdxm/2-t])cube([1,pdxm+2*t,pdxm+2*t]);
    };
    hull(){
      rotate([arot,0,0])translate([-pdx2/2-t,1/2+y1,-pdx2/2-t])cube([pdx2+2*t,1,pdx2+2*t]);
      rotate([ 0,0,0])translate([-pdxm/2-t-6/2,1/2+pdxm/2,-pdxm/2-t])cube([pdxm+2*t+6,1,pdxm+2*t]);
    };
};

  translate([-50,-pdx1/2-tol,-pdx1/2-tol])cube([100,pdx1+2*tol,pdx1+2*tol]);
  rotate([arot,0,0])translate([-pdx2/2,1/2+y1-20,-pdx2/2-tol])cube([pdx2+2*tol,30,pdx2+2*tol]);
};


