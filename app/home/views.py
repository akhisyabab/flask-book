from flask import render_template, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def index():
    return render_template('index.html')