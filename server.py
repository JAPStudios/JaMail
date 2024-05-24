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
const express = require('express');
const app = express();
const bodyParser = require('body-parser')
app.use(bodyParser.json());
app.get('/', (req, res) => {
    res.send('Welcome to Jmail');
});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});