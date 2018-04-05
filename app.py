from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields
from measure.cpu import api_v1_cpu
from measure.storage import api_v1_storage

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1_cpu)
    app.register_blueprint(api_v1_storage)
    app.run(debug=True)