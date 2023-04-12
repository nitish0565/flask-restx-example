
import json


def on_success_response(status_code, success_message, payload):
    """ for sending standard way of return response on success

    return response (Json):

    message :(string) # message to be passed on success/error
    "success": (boolean) # To know response success or failure
    "statusCode": (int) # status code for each individual api
    "payload": (list)  # list with set of payload/return response in it

    """
    if type(payload) == dict:
        payload = json.dumps(payload)
        payload = json.loads(payload)
    else:
        payload = payload

    response_data = {
        "success_status": True,
        "status_code": status_code,
        "message": success_message,
        "payload": payload
    }

    return response_data, 200


def on_error_response(status_code, success_message, payload=None):
    """ for sending standard way of return response on failuer

     return response (Json):

     message :(string) # message to be passed on success/error
     "success": (boolean) # To know response success or failure
     "statusCode": (int) # status code for each individual api
     "payload": (list)  # list with set of payload/return response in it

     """

    if type(payload) == dict:
        payload = json.dumps(payload)
        payload = json.loads(payload)
    else:
        payload = payload

    response_data = {
        "success_status": False,
        "status_code": status_code,
        "message": success_message,
        "payload": payload
    }
    return response_data, 200
