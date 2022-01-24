from . import db

class Words(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    meaning = db.Column(db.String(100), nullable=False)
    note  = db.Column(db.String(200))
    revised = db.Column(db.Integer)
    last_review  = db.Column(db.DateTime)
    added = db.Column(db.DateTime)
    success = db.Column(db.Integer)