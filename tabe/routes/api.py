from flask import Blueprint
from flask import request, jsonify
from tabe.models import Restaurant

bp = Blueprint('api', __name__)


@bp.route('/restaurants')
def restaurants():
    args = request.args
    tag = args.get('tag', type=int)
    rv = Restaurant.query.filter(Restaurant.tags.any(id=tag)).all()
    return jsonify(rv)
