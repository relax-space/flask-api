from turtle import update

from flask import Flask, jsonify, request
from flask_restful import abort

data = [
    {
        'id': 1,
        'name': 'apple',
        'price': 1,
    }, {
        'id': 2,
        'name': 'pear',
        'price': 2,
    }
]


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
        return jsonify(data), 200

    def get(self, id: int):
        fruits = [d for d in data if d.get('id') == id]
        if len(fruits) == 0:
            abort(404)
        return jsonify(fruits[0]), 200

    def add(self):
        req_data = request.json
        if not req_data:
            abort(400)
        req_data['id'] = data[-1]['id']+1
        data.append(req_data)
        return jsonify(req_data), 201

    def delete(self, id: int):
        length = len(data)
        #  倒序删除
        for i in range(length-1, -1, -1):
            if data[i]['id'] == id:
                del data[i]
                break
        return '', 204

    def update(self, id: int):
        req_data = request.json
        if not req_data:
            abort(400)
        req_data.update({'id':id})
        for i in data:
            if i['id'] == id:
                i.update(req_data)
                break
        return '', 204
