from flask import Flask, jsonify

from controllers.fruit import FruitController
from models.database import Base, engine


def init_db():
    # 导入所有的model,然后,初始化数据库
    import models.fruit
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    app = Flask(__name__)

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify(error=str(e)), 404

    init_db()
    FruitController(app, '/fruits')
    app.run(port=8080, debug=True)
