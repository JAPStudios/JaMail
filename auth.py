class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
class AuthService:
    def __init__(self):
        self.users = [
            User(username='user1', password='password1'),
            User(username='user2', password='password2')
        ]
    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False
if __name__ == '__main__':
    auth_service = AuthService()
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    if auth_service.authenticate_user(username_input, password_input):
        print("Authentication successful!")
    else:
        print("Authentication failed. Invalid username or password.")
app.post('/register', async (req, res) => {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const result = await pool.query('INSERT INTO users (username, password) VALUES ($1, $2) RETURNING *', [username, hashedPassword]);
    res.status(201).json(result.rows[0]);
});
app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const result = await pool.query('SELECT * FROM users WHERE username = $1', [username]);
    const user = result.rows[0];
    if (user && await bcrypt.compare(password, user.password)) {
        const token = jwt.sign({ id: user.id }, 'your-secret-key', { expiresIn: '1h' });
        res.json({ token });
    } else {
        res.status(401).send('Invalid credentials');
    }
});