from flask import abort, make_response

# HELPER FUNCTIONS
def validate_model(cls, id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"Planet {id} is invalid."}, 400))

    model = cls.query.get(id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} with id {id} was not found"}, 404))

    return model