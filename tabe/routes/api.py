from flask import Blueprint
from flask import request, jsonify

from tabe.models import db
from tabe.models import Restaurant, Tag

bp = Blueprint('api', __name__)


@bp.route('/restaurants')
def restaurants():
    args = request.args
    tag = args.get('tag', type=int)
    rv = Restaurant.query.options(db.joinedload(Restaurant.tags)) \
        .filter(Restaurant.tags.any(id=tag)).all()
    return jsonify(rv)


@bp.route('/tags')
def tags():
    rv = Tag.query.all()
    return jsonify(rv)


@bp.route('/grouped_tags')
def grouped_tags():
    return jsonify(Tag.grouped())
