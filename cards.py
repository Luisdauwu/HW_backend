from app import app1
from flask import Namespace, Resource, fields
from flask_restx import Api


cards = Namespace('Cards', description= 'hola')
api = Api(app1)

cards_model = api.model('Cards', {
    'number': fields.String(required=True, description=''),
    'cvv': fields.String(required=True, description=''),
    'date': fields.Date(required=True, description='',dt_format='rfc822'),

})


