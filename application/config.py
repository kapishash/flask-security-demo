class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATION = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///secure_db.sqlite3'
    SECRET_KEY = "THIS-IS-DUMMY-KEY"
    SECURITY_PASSWORD_HASH = "bcrypt"
    SECURITY_PASSWORD_SALT = "THIS-IS-DUMMY-SECRET-KEY"
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"