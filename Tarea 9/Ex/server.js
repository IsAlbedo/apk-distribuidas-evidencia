const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

io.on('connection', (socket) => {
  socket.emit('greetings', 'Hey!', { "ms": "jane" }, Buffer.from([4, 3, 3, 1]));

  socket.on('salutations', (elem1, elem2, elem3) => {
    console.log(elem1, elem2, elem3);
  });
});

server.listen(3000, () => {
  console.log('Servidor corriendo en http://localhost:3000');
});