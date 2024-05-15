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