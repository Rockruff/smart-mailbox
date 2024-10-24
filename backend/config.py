# Make sure to change this value depending on how your frontend is hosted
FRONTEND_HOST_NAME = "localhost:5173"


# Class to hold configuration settings related to mail events
class MailEventConfig:
    # Specify the path to the SQLite database file
    DATABASE = "mailbox.db"
    # Directory where images will be stored
    IMAGE_FOLDER = "images"
    # API key for accessing GPT services
    GPT_API_KEY = "sk-your-api-key-here"


# Class to hold configuration settings for email functionality
class EmailConfig:
    # SMTP server address for sending emails
    SMTP_SERVER = "smtp.example.com"
    # Port number for the SMTP server
    SMTP_PORT = 465
    # User email address for authentication
    EMAIL_USER = "name@example.com"
    # Password for the email account
    EMAIL_PASSWORD = "1234567890abcdef"
    # Hostname for the dashboard
    HOST_NAME = FRONTEND_HOST_NAME
