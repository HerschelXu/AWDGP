from flask import Flask, session, g
import config
from exts import db, mail
from models import UserModel
from blueprint.forum import bp as forum_bp
from blueprint.auth import bp as auth_bp
from blueprint.game import bp as game_bp
from flask_migrate import Migrate



app = Flask(__name__)
# bind config
app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "asdjfajkzxc;';khasdhjq"

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(forum_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(game_bp)


@app.before_request
def before_request1():
    # track user -> cookie
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        # if no user -> empty cookie
        setattr(g, "user", None)


@app.context_processor
def content_processor1():
    return {"user": g.user}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
