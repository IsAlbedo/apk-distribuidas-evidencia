const socket = io("http://localhost:3000");

socket.on('connect', () => {
  socket.send('Hello!');
});

socket.on('greetings', (elem1, elem2, elem3) => {
  console.log(elem1, elem2, elem3);
});