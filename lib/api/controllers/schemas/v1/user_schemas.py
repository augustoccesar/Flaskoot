from marshmallow import fields

from lib.api.utils.marshmallow import marshmallow


class BasicUserSchema(marshmallow.Schema):
    id = fields.String()
    username = fields.String()

    _links = marshmallow.Hyperlinks({
        'self': marshmallow.URLFor('user_controller.get_user', id='<id>')
    })
