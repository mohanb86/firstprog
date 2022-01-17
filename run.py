from app import app
from db import db

db.init_app(app)

#used to create tables automatically without create script
@app.before_first_request
def create_tables():
    db.create_all()