from flask import abort, make_response, jsonify

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        msg = f"{cls.__name__} id {model_id} is Invalid"
        abort(make_response(jsonify({"message" : msg }),400))

    model = cls.query.get(model_id)    

    if model:
        return model

    abort(make_response(jsonify({"message":f"{cls.__name__} id {model_id} is Not Found" }),404))

def validate_request_body(request_body,required_data):
    if not request_body:
        msg = "An empty or invalid json object was sent."
        abort(make_response(jsonify({"details":msg}),400))
    
    for data in required_data:
        if data not in request_body: 
            msg = f"Request body must include {data}."
            abort(make_response(jsonify({"details":msg}),400))

    return request_body
