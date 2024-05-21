const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const dotenv = require("dotenv");
const app = express();

dotenv.config();

const PORT = 3000;
const secretKey = process.env.JWT_SECRET;

app.use(bodyParser.json());

const users = [];

// Register route
app.post('/register', async (req, res) => {
  const { username, email, contact, password, role } = req.body;
  existingUser(req, res);

  const encryptedPassword = await bcrypt.hash(password, 10);
  const newUser = { id: users.length + 999, username, email, contact, password: encryptedPassword, role };
  users.push(newUser);

  res.status(201).json({ message: 'User registered successfully' });
});

// Login route
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);

  if (!user || !bcrypt.compareSync(password, user.password)) {
    return res.status(401).json({ message: 'Invalid credentials' });
  }

  const token = jwt.sign({ userId: user.id, role: user.role }, secretKey, { expiresIn: '1d' });

  res.json({ id: user.id, token });
});

// username is already exist or not
function existingUser(req, res) {
  const { username } = req.body;
  if (users.find(user => user.username === username)) {
    return res.status(400).json({ message: 'Username already exists, please enter a new username.' });
  }
}

// authenticating JWT token
function authentication(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ message: 'Unauthorized, token absent.' });
  }

  jwt.verify(token, secretKey, (err, user) => {
    if (err) {
      return res.status(403).json({ message: 'Invalid token' });
    }
    req.user = user;
    next();
  });
}

function authorizeRoles(...roles) {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ message: "Access denied, you don't have permission to access this API endpoint." });
    }
    next();
  };
}

// Admin route (can be accessed by only admin)
app.get('/admin', authentication, authorizeRoles('admin'), (req, res) => {
  res.json({ message: 'Admin route accessed successfully (Logged in as admin)' });
});

// User route (can be accessed by user and admin both)
app.get('/user', authentication, (req, res) => {
  res.json({ message: 'User route accessed successfully' });
});

// Get a list of all registered users
app.get('/users', (req, res) => {
  res.json(users);
});

// protected route
app.get('/protected', authentication, (req, res) => {
  res.json({ message: 'Protected route accessed successfully' });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
