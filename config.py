class Config:
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'your_smtp_username'
    SMTP_PASSWORD = 'your_smtp_password'
    ENCRYPTION_METHOD = 'TLS'
    DATABASE_URL = 'mongodb://localhost:27017/email_service_db'
    MAX_ATTACHMENT_SIZE_MB = 10
    WELCOME_EMAIL_TEMPLATE = """
        Hello {username},
        Welcome to our secure email service! We're excited to have you on board.
        Best regards,
        The Email Service Team
    """
    PASSWORD_RESET_EMAIL_TEMPLATE = """
        Hi {username},
        You have requested a password reset. Click the following link to reset your password:
        {password_reset_link}
        If you did not request this, please ignore this email.
        Best regards,
        The Email Service Team
    """
    INVALID_ATTACHMENT_ERROR = "Attachment exceeds the maximum allowed size of {max_size} MB."
    LOGIN_FAILED_ERROR = "Login failed. Please check your credentials and try again."
    @staticmethod
    def is_valid_email(email):
        pass
    @staticmethod
    def sanitize_input(data):
        pass
config = Config()