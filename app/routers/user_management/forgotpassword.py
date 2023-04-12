

from flask_restx import Resource,fields
from flask import request

# custom Module
from app.routers.utils.http_response_pattern import on_success_response, on_error_response
from app.routers.user_management import user_forgot_password_namespace



user_forgot_password_fields = user_forgot_password_namespace.model('To rest the use password',
                                                  {'email_id': fields.String(required=True, )} )


@user_forgot_password_namespace.route("/forgotpassword")
@user_forgot_password_namespace.doc(security=None)
class ForgotPassword(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @user_forgot_password_namespace.doc("forgot password")
    @user_forgot_password_namespace.expect(user_forgot_password_fields)
    def post(self):

        """

          If user forgot the password and want to reset it.
          """
        """
          he need to pass the registered email for
          this and  API will send mail with newly generated password.

          :param email_id: (string) registered email id
          :return: Message for message weather new password sent to mail
          """
        return on_success_response(200, "New Password Is Sent To Your Mail", None)