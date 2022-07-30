from flask import Blueprint, jsonify, request

import db
from models import User

users_blueprint = Blueprint('users_blueprint', __name__) # , template_folder='templates')


def user_to_dict(user):
    """
    Prepare an object for JSON
    """
    return {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone,
    }


@users_blueprint.route('/users', methods=['GET'])
def get_all_users():
    result = []
    users = User.query.all()
    for user in users:
        result.append(user_to_dict(user))
    return jsonify(result)


@users_blueprint.route('/users/<int:uid>', methods=['GET'])
def get_one_user(uid):
    user = User.query.get(uid)
    return jsonify(user_to_dict(user))


@users_blueprint.route('/users', methods=['POST'])
def create_user(user: User):
    data = request.json
    user = User(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        age=data.get('age'),
        email=data.get('email'),
        role=data.get('role'),
        phone=data.get('phone'),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user_to_dict(user))


@users_blueprint.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    data = request.json

    user = User.query.get(uid)
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.age = data.get('age')
    user.email = data.get('email')
    user.role = data.get('role')
    user.phone = data.get('phone')

    db.session.commit()
    return jsonify(user_to_dict(user))


@users_blueprint.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    user = User.query.get(uid)
    db.session.delete(user)
    db.session.commit()
    return jsonify('')

