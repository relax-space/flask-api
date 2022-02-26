

from flask import Flask, abort, jsonify, request
from models.fruit import Fruit


class FruitController:
    def __init__(self, app: Flask, resource_name: str):
        app.add_url_rule(f'{resource_name}',
                         view_func=self.get_all, methods=['GET'])
        app.add_url_rule(f'{resource_name}/<int:id>',
                         view_func=self.get, methods=['GET'])
        app.add_url_rule(f'{resource_name}',
                         view_func=self.add, methods=['POST'])
        app.add_url_rule(f'{resource_name}/<int:id>',
                         view_func=self.delete, methods=['DELETE'])
        app.add_url_rule(f'{resource_name}/<int:id>',
                         view_func=self.update, methods=['PUT'])

    def get_all(self):
        req_data = request.values
        offset = req_data.get('offset', 0)
        limit = req_data.get('limit', 20)
        return jsonify(Fruit.get_all(offset, limit)), 200

    def get(self, id: int):
        fruits = Fruit.get(id)
        if len(fruits) == 0:
            abort(404)
        return jsonify(fruits[0]), 200

    def add(self):
        req_data = request.json
        if not req_data:
            abort(400)
        resp = Fruit.insert(req_data)
        return jsonify(resp), 201

    def delete(self, id: int):
        Fruit.delete(id)
        return '', 204

    def update(self, id: int):
        req_data = request.json
        if not req_data:
            abort(400)
        Fruit.update(id, req_data)
        return '', 204
