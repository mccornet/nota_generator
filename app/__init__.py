from flask import Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.template_filter('valuta')
def valuta(n):
    n = float(n)
    return f'{n:.2f}'.replace('.', ',')

@app.template_filter('tuinen')
def tuinen(n):
    n = float(n)
    return f'{n:.1f}'.replace('.', ',')


from app import routes, models