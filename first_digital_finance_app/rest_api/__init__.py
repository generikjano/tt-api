from flask_restplus import Api

from .controllers import api as first_controller

api = Api(
    title='TT Api',
    version='1.0',
    description='Test task for the candidates',
)

api.add_namespace(first_controller)

