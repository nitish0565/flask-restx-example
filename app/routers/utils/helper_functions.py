import logging
from app.routers.utils.http_response_pattern import on_success_response,on_error_response

def api_body_param_validation(req, mandatory_param_list):
    """
    function for validating the mandatory params in thr API request body and
    return error if any param is null or missing
    """
    try:
        dic_data = req.get_json()
    except Exception as e:
        return on_error_response(400, "some params are missing in body", None)

    for each_key in mandatory_param_list:

        if each_key in dic_data.keys():
            if dic_data[each_key] is None or len(str(dic_data[each_key])) <= 0:
                logging.error(str(each_key) + " can not be null/None")
                return True, on_error_response(400, each_key + " can not be null/None ", None)
            else:
                logging.info(str(each_key) + " " + str(dic_data[each_key]))
        else:
            logging.error(str(each_key) + " is a mandatory fields")
            return True, on_error_response(400, each_key + " is a mandatory fields ", None)
    return False, None