from flask import Blueprint, render_template, request, url_for
from .models import Words
from . import db
from datetime import tzinfo, timedelta, datetime
from sqlalchemy import desc

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    words = Words.query.order_by(desc(Words.added)).all()
    return render_template('home.html', words=words)
    
@views.route('/add', methods=['GET', 'POST'])
def addWord(): 
    if request.method == 'POST':
        word = request.form.get('word')
        meaning = request.form.get('meaning')
        note = request.form.get('note')
        NewWord = Words(word=word, meaning=meaning, note=note, added=datetime.now())
        db.session.add(NewWord)
        db.session.commit()
    print(datetime.now().strftime("%Y-%m-%d %I:%M %p"))
    return render_template('add.html')

    