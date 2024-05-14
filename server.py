const express = require('express');
const app = express();
app.post('/login', (req, res) => {
});
app.post('/register', (req, res) => {
});
app.get('/emails', (req, res) => {
});
app.post('/send-email', (req, res) => {
});
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});