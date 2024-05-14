from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class EmailVerifyModel(db.Model):
    __tablename__ = "email_verify"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)
    # For deletion
    # used_captcha = db.Column(db.Boolean, default=False)


class PostsModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # Foreign Key
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref="posts")


class ReplyModel(db.Model):
    __tablename__ = "reply"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # Foreign Key
    reply_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    # relations
    post = db.relationship(PostsModel, backref=db.backref('replies', order_by=create_time.desc()))
    author = db.relationship(UserModel, backref='replies')


class GameRecordModel(db.Model):
    __tablename__ = "game_records"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    end_time = db.Column(db.Float, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(UserModel, backref="game_records")
