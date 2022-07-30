from flask import Blueprint, jsonify

from models import Offer

offers_blueprint = Blueprint('offers_blueprint', __name__) # , template_folder='templates')


def offer_to_dict(offers):
    """
    Prepare an object for JSON
    """
    return {
        "id": offers.id,
        "order_id": offers.order_id,
        "executor_id": offers.executor_id,
    }


@offers_blueprint.route('/offers', methods=['GET'])
def get_all_offers():
    result = []
    offers = Offer.query.all()
    for offer in offers:
        result.append(offer_to_dict(offer))
    return jsonify(result)


@offers_blueprint.route('/offers/<int:uid>', methods=['GET'])
def get_one_offer(uid):
    offer = Offer.query.get(uid)
    return jsonify(offer_to_dict(offer))


@offers_blueprint.route('/offers', methods=['POST'])
def create_offer(offer: Offer):
    pass


@offers_blueprint.route('/offers/<int:uid>', methods=['PUT'])
def update_offer(uid):
    pass


@offers_blueprint.route('/offers/<int:uid>', methods=['DELETE'])
def delete_offer(uid):
    pass

