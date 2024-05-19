from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import PostsForm, ReplyForm
from models import PostsModel, ReplyModel
from exts import db
from decor import login_req

bp = Blueprint("forum", __name__, url_prefix="/")


@bp.route("/")
def index():
    posts = PostsModel.query.order_by(PostsModel.create_time.desc()).all()
    return render_template("index.html", posts=posts)


@bp.route("/forum/post", methods=['GET', 'POST'])
@login_req
def publish_post():
    if request.method == 'GET':
        return render_template("publish_post.html")
    else:
        form = PostsForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            posts = PostsModel(title=title, content=content, author=g.user)
            db.session.add(posts)
            db.session.commit()
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("forum.publish_post"))


@bp.route("/forum/detail/<post_id>")
def post_detail(post_id):
    post = PostsModel.query.get(post_id)
    return render_template("detail.html", post=post)


@bp.route("/reply/publish", methods=['POST'])
@login_req
def publish_reply():
    form = ReplyForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        reply = ReplyModel(content=content, reply_id=post_id, author_id=g.user.id)
        db.session.add(reply)
        db.session.commit()
        return redirect(url_for("forum.post_detail", post_id=post_id))
    else:
        print(form.errors)
        return redirect(url_for("forum.post_detail", post_id=request.form.get("post_id")))


@bp.route("/search")
def search():
    s = request.args.get("s")
    searches = PostsModel.query.filter(PostsModel.title.contains(s)).all()
    return render_template("index.html", posts=searches)

@bp.route("/introduction")
def introduction():

    return render_template("introduction.html")
