from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
from decor import login_req
from models import UserModel, GameRecordModel
from exts import db

bp = Blueprint('game', __name__, url_prefix='/game')


@bp.route('/')
@login_req
def game():
    return render_template('game.html')


@bp.route('/update_time', methods=['POST'])
@login_req
def update_time():
    user_id = request.json.get('user_id')
    end_time = request.json.get('end_time')

    if not user_id or not end_time:
        return jsonify({'error': 'Missing data'}), 400

    user = UserModel.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    new_record = GameRecordModel(user_id=user_id, end_time=end_time)
    db.session.add(new_record)
    db.session.commit()

    return jsonify({'message': 'Time updated successfully'}), 200


@bp.route('/leaderboard')
@login_req
def leaderboard():
    records = GameRecordModel.query.order_by(GameRecordModel.end_time.asc()).limit(10).all()
    return render_template('leaderboard.html', records=records)
