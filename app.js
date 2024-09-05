// server.js (basic Node.js backend)
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/login.html');
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (username === 'testuser' && password === 'testpassword') {
    res.send('Login Successful!');
  } else {
    res.send('Invalid Credentials!');
  }
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
