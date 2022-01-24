from flask import Blueprint, render_template, request
from .models import Words

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('layout.html')

@views.route('/add', methods=['GET', 'POST'])
def addWord():
    
    return render_template('add.html')
    
    if request.method == 'POST':
        NewWord = Words()
    