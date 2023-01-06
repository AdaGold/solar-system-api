from flask import make_response, abort


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except: 
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message": f"{cls.__name__} {model_id} is not found"}, 404))
    return model


def validate_moon(moon):
    invalid_dict = dict()
    if "name" not in moon or not isinstance(moon["name"], str) or moon["name"] is None:
        invalid_dict["details"] = "Request body must include name."
    if "description" not in moon or not isinstance(moon["description"], str) or \
        moon["description"] is None:
        invalid_dict["details"] = "Request body must include description."
    if "radius" not in moon or not isinstance(moon["radius"], int) or moon["radius"] is None:
        invalid_dict["details"] = "Request body must include radius."
    return invalid_dict


def validate_planet(planet):
    invalid_dict = dict()
    if "name" not in planet or not isinstance(planet["name"], str) or planet["name"] is None:
        invalid_dict["details"] = "Request body must include name."
    if "size" not in planet or not isinstance(planet["size"], int) or planet["size"] is None:
        invalid_dict["details"] = "Request body must include size."
    if "description" not in planet or not isinstance(planet["description"], str) or \
        planet["description"] is None:
        invalid_dict["details"] = "Request body must include description."
    if "distance_from_earth" not in planet or not isinstance(planet["distance_from_earth"], int) or \
        planet["distance_from_earth"] is None:
        invalid_dict["details"] = "Request body must include distance_from_earth."
    return invalid_dict