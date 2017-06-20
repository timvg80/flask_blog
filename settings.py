SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'tim'
DB_PASSWORD = 'password'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = 'localhost'
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' % (
    DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME
)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
