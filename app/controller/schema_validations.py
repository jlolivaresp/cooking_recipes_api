from jsonschema import validate

from app.contants import UNIT_DEFAULT_NAME, INGREDIENTS_NAME_FORMAT


class Schema:
    @staticmethod
    def get_delete_node_request_schema(json):
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

    @staticmethod
    def add_recipe_request_schema(json):
        schema = {
            "type": "object",
            "patternProperties": {
                "^.*$": {
                    "anyOf": [
                        {"type": "object"}
                    ],
                    "properties": {
                        INGREDIENTS_NAME_FORMAT: {
                            "type": "object",
                            "patternProperties": {
                                "^.*$": {
                                    "anyOf": [
                                        {"type": "number"}
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
        validate(json, schema)
