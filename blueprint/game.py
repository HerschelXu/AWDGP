from flask import Blueprint, render_template
from functools import wraps
from flask import g, redirect, url_for
from decor import login_req

bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')
@login_req
def game():
    return render_template('game.html')
