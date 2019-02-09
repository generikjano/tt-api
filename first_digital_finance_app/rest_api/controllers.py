import flask
import sqlalchemy as sa
from flask_restplus import Namespace, Resource
from marshmallow import Schema, fields as mm_fields
from sqlalchemy.orm import aliased

import rest_api.models as m

api = Namespace('', description='Test task for the candidates')


class ClientCreateSchema(Schema):
    last_name = mm_fields.String(required=True)
    first_name = mm_fields.String(required=True)
    dob = mm_fields.Date(required=True, format='%Y-%m-%d')
    social_status_id = mm_fields.Integer(required=True)
    gender = mm_fields.String(required=True)


class ClientRetrieveSchema(ClientCreateSchema):
    id = mm_fields.Integer()
    social_status = mm_fields.String()
    gender_id = mm_fields.String()


c = m.Client


def return_query():
    d1 = aliased(m.Dictionary)
    d2 = aliased(m.Dictionary)
    query = m.session.query(c.id, c.last_name, c.first_name, c.dob, c.social_status_id, c.gender.label('gender_id')). \
        outerjoin(d1, sa.and_(c.social_status_id == d1.int_id, d1.category == 'social_status_id')). \
        outerjoin(d2, sa.and_(c.gender == d2.str_id, d2.category == 'gender')) \
        .add_columns(
        d1.value.label('social_status'),
        d2.value.label('gender'))
    return query


@api.route('/clients/')
class Clients(Resource):
    parser = api.parser()
    parser.add_argument('body', required=True, help='json content', location='json')

    def get(self):
        query = return_query()
        return ClientRetrieveSchema(many=True).dump(query).data

    @api.expect(parser)
    def post(self):
        data, errors = ClientCreateSchema().load(flask.request.get_json())

        if errors:
            return errors, 422
        client = m.Client(**data)
        m.session.add(client)
        m.session.commit()
        return client.id


@api.route('/clients/<string:id>', methods=['GET', 'POST'])
class Client(Resource):
    def get(self, id):
        query = return_query().filter(c.id == id).first()
        if not query:
            return "Not Found", 404

        return ClientRetrieveSchema().dump(query).data
