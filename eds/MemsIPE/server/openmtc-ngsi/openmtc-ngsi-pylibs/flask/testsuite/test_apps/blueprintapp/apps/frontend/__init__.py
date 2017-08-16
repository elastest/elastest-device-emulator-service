from flask import Blueprint, render_template

frontend = Blueprint('FrontEnd', __name__, template_folder='templates')


@frontend.route('/')
def index():
    return render_template('FrontEnd/motor.html')
