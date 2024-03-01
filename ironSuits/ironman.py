from flask import Blueprint, render_template
import json

bp = Blueprint('ironman', __name__, url_prefix="/ironman")
 
@bp.route('/')
def index():
    ironmen = json.load(open('iron.json'))  # Assuming 'iron.json' contains a list of ironman objects
    return render_template('ironman.html', ironmen=ironmen)  # Pass the list of ironman objects
                

@bp.route('/<int:index>')
def show(index):
    ironmen = json.load(open('iron.json')) 
    ironman = ironmen[index]
    return render_template('show.html', ironman=ironman)
  
