from flask import Flask
from controllers.fruit import FruitController

if __name__ == '__main__':
    app = Flask(__name__)
    FruitController(app,'/fruits')
    app.run(port=8080,debug=True)
