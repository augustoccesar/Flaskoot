from flask import jsonify, Blueprint
from flasgger import swag_from

from lib.api.utils.limiter import limiter

from lib.api.decorators.versionable_endpoint import versionable_endpoint
from lib.api.controllers.actions.v1 import user_actions as v1_user_actions
from lib.api.controllers.schemas.v1 import user_schemas as v1_user_schemas

from lib.api.controllers.documentation.v1 import user_controller_doc as v1_user_controller_doc


user_controller = Blueprint('user_controller', __name__)


@limiter.limit("5/minute")
@user_controller.route('/', methods=['GET'])
@versionable_endpoint([1])
@swag_from(v1_user_controller_doc.get_users)
def get_users(version):
    if version == 1:
        users = v1_user_actions.get_users()

        return v1_user_schemas.BasicUserSchema(many=True).jsonify(users)


@limiter.limit("5/minute")
@user_controller.route('/<id>', methods=['GET'])
@versionable_endpoint([1])
@swag_from(v1_user_controller_doc.get_user)
def get_user(version, id):
    if version == 1:
        user = v1_user_actions.get_user_by_id(id)

        return v1_user_schemas.BasicUserSchema().jsonify(user)
