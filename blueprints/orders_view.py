from flask import Blueprint, jsonify

from models import Order

orders_blueprint = Blueprint('orders_blueprint', __name__) # , template_folder='templates')


def order_to_dict(order):
    """
    Prepare an object for JSON
    """
    return {
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id,
    }


@orders_blueprint.route('/orders', methods=['GET'])
def get_all_orders():
    result = []
    orders = Order.query.all()
    for order in orders:
        result.append(order_to_dict(order))
    return jsonify(result)


@orders_blueprint.route('/orders/<int:uid>', methods=['GET'])
def get_one_order(uid):
    order = Order.query.get(uid)
    return jsonify(order_to_dict(order))


@orders_blueprint.route('/orders', methods=['POST'])
def create_order(order: Order):
    pass


@orders_blueprint.route('/orders/<int:uid>', methods=['PUT'])
def update_order(uid):
    pass


@orders_blueprint.route('/orders/<int:uid>', methods=['DELETE'])
def delete_order(uid):
    pass

