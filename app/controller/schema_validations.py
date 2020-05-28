from jsonschema import validate

from app.contants import UNIT_DEFAULT_NAME


class Schema:
    @staticmethod
    def get_ingredient_request_schema(json):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            }
        }
        return validate(json, schema)

    @staticmethod
    def add_ingredient_request_schema(json):
        schema = {
            "type": "object",
            "patternProperties": {
                "^.*$": {
                    "anyOf": [
                        {"type": "object"}
                    ],
                    "properties": {
                        UNIT_DEFAULT_NAME: {"type": "string"}
                    }
                }
            }
        }
        return validate(json, schema)
