"""
City objects that handles all default RESTFul API actions:
"""
from models.state import State
from models.city import City
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, make_response, request


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def all_cities(state_id=None):
    """ status view function """
    city_list = []
    my_state = storage.get(State, state_id)
    if not my_state:
        abort(404)
    my_cities = my_state.cities
    for city in my_cities:
        city_list.append(city.to_dict())
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def city_id(city_id=None):
    """ status view function """
    my_city = storage.get(City, city_id)
    if not my_city:
        abort(404)
    return jsonify(my_city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def city_delete(city_id=None):
    """ status view function """
    my_city = storage.get(City, city_id)
    if my_city:
        storage.delete(my_city)
        storage.save()
        dict_empty = {}
        return make_response(jsonify(dict_empty), 200)
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def city_post(state_id=None):
    """ status view function """
    my_state = storage.get(State, state_id)
    if not my_state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "name" not in request.get_json():
        abort(400, description="Missing name")
    body_obj = request.get_json()
    body_obj["state_id"] = state_id
    new_city = City(**body_obj)
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def city_put(city_id=None):
    """ status view function """
    my_city = storage.get(City, city_id)
    if not my_city:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at', 'state_id']

    for k, v in request.get_json().items():
        if k not in ignore:
            setattr(my_city, k, v)
    my_city.save()
    return make_response(jsonify(my_city.to_dict()), 200)
