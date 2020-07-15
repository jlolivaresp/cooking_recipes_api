from flask import render_template, jsonify
from jsonschema import ValidationError
from app.src.service.firebase import ReferenceNotFoundException, ElementAlreadyExistsError

from app import app


@app.errorhandler(ValidationError)
def validation_error(e: ValidationError):
    response = jsonify(message=e.message, code=400)
    response.status_code = 400
    return response


@app.errorhandler(ReferenceNotFoundException)
def reference_not_found_error(e: ReferenceNotFoundException):
    response = jsonify(e.error_dict)
    response.status_code = 404
    return response


@app.errorhandler(ElementAlreadyExistsError)
def element_already_exists_error(e: ElementAlreadyExistsError):
    response = jsonify(e.error_dict)
    response.status_code = 409
    return jsonify(e.error_dict)


@app.errorhandler(400)
def bad_request_default(e):
    return jsonify(message=e.get_description(), code=400), 400


# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'), 500
