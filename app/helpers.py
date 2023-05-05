from flask import abort, make_response 


def validate_model(cls, id):

    try:
        id = int(id)
    except:
        message = f"The {cls.__name__}{id} is invalid"
        abort(make_response({"message": message}, 400))

    model = cls.query.get(id)
    
    if not model:
        message = f"The {cls.__name__} {id} not found"
        abort(make_response({"message": message}, 404))

    return model


def apply_filters(model_class, query_params):

    query = model_class.query
    for key, value in query_params.items():
        if value:
            query = query.filter_by(**{key:value})
        
    return query