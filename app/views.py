from flask import Blueprint, render_template, request, url_for
from .models import Words
from . import db
from datetime import datetime
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('home.html')

@views.route('/add', methods=['GET', 'POST'])
def addWord():
    
    if request.method == 'POST':
        word = request.form.get('word')
        meaning = request.form.get('meaning')
        note = request.form.get('note')
        NewWord = Words(word=word, meaning=meaning, note=note, added=datetime.now())
        db.session.add(NewWord)
        db.session.commit()


    return render_template('add.html')
    

    