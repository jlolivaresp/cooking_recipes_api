from jsonschema import validate

from app.contants import UNIT_DEFAULT_NAME, INGREDIENTS_NAME_FORMAT


class Schema:
    @staticmethod
    def get_delete_node_request_schema(json: dict):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"}
            }
        }
        return validate(json, schema)

    @staticmethod
    def add_ingredient_request_schema(json: dict):
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
    def add_recipe_request_schema(json: dict):
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
        return validate(json, schema)

    @staticmethod
    def summarize_selected_recipes_ingredients(json: dict):
        schema = {
            "type": "object",
            "properties": {
                "recipe_list": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        }
        return validate(json, schema)

