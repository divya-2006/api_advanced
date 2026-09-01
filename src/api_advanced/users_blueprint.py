from flask import Blueprint, Flask

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/tests', methods=['GET'])
def test():
    return "This is blurprint!"
