const express = require('express');
const bodyParser = require("body-parser");
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

// Now attach the socket.io variable with the HTTP server created
io.attach(http, {
 pingInterval: 10000,
 pingTimeout: 5000,
 cookie: false
});

// Boolean if armed button has been pressed
var armed = false;

// =========================================
// http web endpoints
// =========================================
app.use(bodyParser.json());

app.use(express.static(process.cwd()));

app.get('/', (req, res) => {
  res.sendFile(process.cwd()+"/index.html")
});

app.get('*', function(req, res) {
  res.sendFile(process.cwd()+"/index.html")
})

// =========================================
// Web Namespace
// =========================================
io.of("/web").on('connection', (socket) => {
  console.log('a user connected');
});

// =========================================
// Camera Namespace
// =========================================
io.of("/cam").on('connection', (socket) => {
  console.log('a camera connected');
});


// =========================================
// ROS2 Namespace
// =========================================
io.of("/ros2").on('connection', (socket) => {
  console.log('a user connected in ros2 namespace');

  socket.on('videofeed1', function (msg) {
    io.of("/web").emit('videofeed1', msg);
  });

});

// =========================================
// Drone Namespace
// =========================================
io.of("/control").on('connection', (socket) => {
  console.log('a device entered the control space');

  socket.on('disconnect', function () {
    console.log('user disconnected');
  });

  // SocketIoRos2 bridge
  socket.on('ros2server', function (msg) {
   io.of("/ros2").emit('control', msg);
  });

  // Receive control command
  socket.on('joystick', function (msg) {
    var aux1 = msg[4];

    console.log(msg);

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

});


// =========================================
// SocketIO endpoints
// =========================================
io.on('connection', (socket) => {
  console.log('a user connected');

  socket.on('disconnect', () => {
    console.log('user disconnected');
  });

});

// =========================================
// Start Server
// =========================================
http.listen(5000, () => {
  console.log('listening on *:5000');
});
