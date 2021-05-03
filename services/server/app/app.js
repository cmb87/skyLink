// express framwork for a basic http server
var app = require('express')();
// create the http server
var http = require('http').createServer(app);
// require the socket.io and bind it to a port 
var io = require('socket.io')(5000);

// Now attach the socket.io variable with the HTTP server created

io.attach(http, {
 pingInterval: 10000,
 pingTimeout: 5000,
 cookie: false
});


var armed = false;

io.on('connection', function (socket) {

  console.log('user connected');

  socket.on('disconnect', function () {
    console.log('user disconnected');
  });

  socket.on('ros2server', function (msg) {
   console.log(msg);
  });


  socket.on('j1', function (msg) {
   console.log(msg);
   controller.throttle = msg[0];
   controller.yaw = msg[1];
   io.emit('control', controller.get());
  });

  socket.on('j2', function (msg) {
   console.log(msg);
   controller.pitch = msg[0];
   controller.roll = msg[1];
   io.emit('control', controller.get());
  });

  socket.on('gamepad', function (msg) {

   var aux1 = msg[4];
   var aux2 = msg[5];

   console.log(msg);

   io.emit('control', msg);
 
   if ( aux1 > 1500 && !armed) {
      console.log("Armed!");
      io.emit('toggleled', "");
      armed = true;

   } else if ( aux1 < 1500 && armed ) {
      console.log("Disarmed!");
      io.emit('toggleled', "");
      armed = false;
   }

  });

  // Toggle led
  socket.on('statechange', function (msg) {
   console.log("statechange: "+msg);
   io.emit('toggleled', "");
  });

  timeout();
});

function timeout() {
  setTimeout(function () {
   io.emit('state_change_request',"A message from server");
    timeout();
  }, 5000);
}

// start listening on a ephemeral port or you can specify a port itself,Now the Server is almost set up
http.listen();
