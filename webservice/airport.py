import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful_swagger import swagger
from flask_caching import Cache


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'top_airports.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# API documentation
api = swagger.docs(Api(app), apiVersion='1', api_spec_url="/api/v1/spec")

db.Model.metadata.reflect(db.engine)

# Primary key was needed! Pandas does not export index to primary_key by default
class Airports(db.Model):
    __tablename__ = 'list_airports'
    __table_args__ = {
        'autoload': True,
        'autoload_with': db.engine
    }

class AirportSchema(ma.Schema):
    class Meta:
        fields = ('arr_port', 'pax')

airport_schema = AirportSchema()
airports_schema = AirportSchema(many=True)

@api.resource('/list')
class ListAllAirports(Resource):
    "Retrieve all airports, sorted by number of passengers"
    @swagger.operation(
        notes='Biggest first'
    )
    @cache.cached()
    def get(self):
        all_airports = Airports.query.all()
        result = airports_schema.dump(all_airports)
        return jsonify(result.data)

@api.resource('/top/<int:top_num>')
class GetTopAirports(Resource):
    "Retrieve the top X number of airports, X is user-specified"
    @swagger.operation(
        notes='Input is a number'
    )
    @cache.cached()
    def get(self, top_num):
        top_airports = Airports.query.limit(top_num)
        result = airports_schema.dump(top_airports)
        return jsonify(result.data)

@api.resource('/numberAirports')
class GetNumberOfAirports(Resource):
    "Retrieve the number of registered airports in the database"
    @swagger.operation(
        notes=''
    )
    @cache.cached()
    def get(self):
        count_airports = Airports.query.count()
        return {'numberAirports': count_airports}

if __name__ == '__main__':
    app.run(debug=True)
