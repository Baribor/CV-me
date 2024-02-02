from flask import Blueprint, make_response


cv_route = Blueprint("cv", __name__)


@cv_route.get("/:id")
def get_cv():
    return make_response({
        "message": "cv retrieved successfully"
    })


@cv_route.post("/")
def create_cv():
    return make_response({
        "message": "cv created successfully"
    })


@cv_route.put("/")
def update_cv():
    return make_response({
        "message": "cv updated successfully"
    })


@cv_route.delete("/:id")
def delete_cv():
    return make_response({
        "message": "cv deleted successfully"
    })
