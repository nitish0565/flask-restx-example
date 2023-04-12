from flask_restx import Resource, fields
from flask import request

# custom modules
from app.routers.utils.http_response_pattern import on_success_response, on_error_response
from app.routers.utils.helper_functions import api_body_param_validation
from app.routers.user_management import user_registration_namespace

create_user_fields = user_registration_namespace.model('to create a new user',
                                                       {'first_name': fields.String(required=True),
                                                        'last_name': fields.String(required=True),
                                                        'email': fields.String(required=True),
                                                        'contact_no': fields.Integer(required=True),
                                                        'tenant_id': fields.Integer(required=True),
                                                        'role_id': fields.Integer(required=True)}
                                                       )

update_user_fields = user_registration_namespace.model('to update user details',
                                                       {'first_name': fields.String(required=True,
                                                                                    ),
                                                        'last_name': fields.String(required=True,
                                                                                   ),
                                                        'profile_pic_content': fields.String(required=False,
                                                                                             )
                                                        }
                                                       )


@user_registration_namespace.route("/user")
class User(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @user_registration_namespace.doc("create new user")
    @user_registration_namespace.expect(create_user_fields)
    def post(self, user_id):
        """
        creating user for first time.
        """
        """
        :param user_id: user_id that has permission to create new user
        :return: Success/Failed message
        """
        # getting required data for audit log
        request_data = request
        action = "creating user for first time"
        data = {"id": "null"}

        try:
            user_request_body = request.get_json()

            # Validations
            param_validation_status, param_value_status = api_body_param_validation(request,
                                                                                    ["first_name", "last_name", "email",
                                                                                     "contact_no", "tenant_id",
                                                                                     "role_id"])

            if param_validation_status:
                return param_value_status
            user_registration_namespace.logger.info("checked validations")
            return on_success_response(201, "User Registered Successfully", None)
        except Exception as e:
            user_registration_namespace.logger.info(e)

            return on_error_response(400, "Something Went Wrong", None)

    @user_registration_namespace.doc("get logged user registered details")
    def get(self, user_id):
        """
        to get user register login details.
        """
        """
        :param user_id: 
        :return: registration details of the current user
        """
        # getting required data for audit log
        request_data = request
        action = "to get user register login details"
        data = {"id": "null"}

        user = [{"name": "abc", "email": "abc@gmail.com", "emp_id": 909090, "user_id": "guihsgd8y31122"},
                {"name": "xyz", "email": "xyz@gmail.com", "emp_id": 908890, "user_id": "OPOOd8y31122"}]
        return on_success_response(200, "user details", user)
