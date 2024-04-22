from functools import wraps
from flask import g, redirect, url_for


def login_req(func):
    # keep args of func
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            # if g.user is user(app.py)
            return func(*args, **kwargs)
        else:
            # if g.user is None
            return redirect(url_for("auth.login"))
    return inner
