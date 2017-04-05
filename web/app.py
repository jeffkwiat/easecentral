import psycopg2

from flask import Flask
from models import db

app = Flask(__name__)

# load config from the config file we created earlier
app.config.from_object('config')

# initialize and create the database
db.init_app(app)
db.create_all(app=app)

@app.route('/')
def home():
    return 'hello world'

@app.route('/favorites')
def favorites():
    return 'hello favorites'

if __name__ == '__main__':
    app.run()