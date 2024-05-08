from flask import Blueprint, render_template
from decor import login_req

bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')
@login_req
def game():
    return render_template('game.html')
