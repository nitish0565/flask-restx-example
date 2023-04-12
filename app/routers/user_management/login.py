from flask_restx import Resource
from flask import request

# custom modules
from app.routers.utils.http_response_pattern import on_success_response, on_error_response
from app.routers.utils.helper_functions import api_body_param_validation
from app.routers.user_management import user_login_namespace
from flask_restx import fields


user_login_model = user_login_namespace.model('UserModel Management login body data',

                                              {'email_id': fields.String(required=True,
                                                                         description="registered email id",
                                                                         help="Name cannot be blank."),
                                               'password': fields.String(required=True,
                                                                         description="Name of the person",
                                                                         help="Name cannot be blank.")}
                                              )


@user_login_namespace.route("/userlogin")
@user_login_namespace.doc(security=None)
class UserLogin(Resource):

    @user_login_namespace.doc("user login")
    @user_login_namespace.expect(user_login_model)
    def post(self):
        """
        login with email and password.
        """
        """
        :return: 
        """
        param_validation_status, param_value_status = api_body_param_validation(request, ["email_id", "password"])

        user_login_payload = request.get_json()
        try:

            param_validation_status, param_value_status = api_body_param_validation(request, ["email_id", "password"])

            # user_login_payload = request.get_json()

            if param_validation_status:
                return param_value_status
            user_login_namespace.logger.info("inside post method")
            return_response = self.user_validation()

            data = {"email_id": user_login_payload["email_id"]}
            return return_response
        except Exception as error:
            user_login_namespace.logger.error("failed to login" + str(error))
            return on_error_response(400, "failed to get login details " + str(error), None)

    def user_validation(self):
        user_model_dict = {"email_id": "abc@gmail.com",
                           "user_id": "7s7as9sdGH90JJuiooj",
                           "Name": "abc",
                           "token": {
                               "access_token": "fgyy89ghhgAW-hhdthyggtyy78887-ghgyghsggwsxgGHGGYsjahgx-788gbbxgsashxsGHJKKJ",
                               "expires_in": 3600,
                               "refresh_token": "fytftghxz78-ZFGYGF889hjjyhjkjhu-fgughytftyghjuhjZZ"}
                           }
        return on_success_response(200, "Logged In Successfully", user_model_dict)

