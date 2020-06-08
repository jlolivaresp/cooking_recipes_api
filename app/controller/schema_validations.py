from jsonschema import validate

from app.contants import UNIT_DEFAULT_NAME, INGREDIENTS_NAME_FORMAT


class ModelSchema:
    @staticmethod
    def get_delete_node_request_schema(obj: dict):
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"}
            },
            "required": ["id"]
        }
        return validate(obj, schema)

    @staticmethod
    def update_node_field_request_schema(obj: dict):
        schema = {
            "type": "object",
            "patternProperties": {
                "^.*$": {"type": "array"}
            }
        }
        return validate(obj, schema)

    @staticmethod
    def add_ingredient_request_schema(obj: dict):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "unit": {"type": "array"},
                "supermarket": {"type": "array"},
                "category": {"type": "string"}
            },
            "required": ["name", "unit_list", "supermarket_list", "category"]
        }
        return validate(obj, schema)

    @staticmethod
    def add_recipe_request_schema(obj: dict):
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "supermarket": {"type": "string"},
                "ingredients": {
                    "type": "object",
                    "patternProperties": {
                        "^.*$": {
                            "anyOf": [{"type": "object"}],
                            "properties": {
                                "quantity": {"type": "string"},
                                "unit": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
        return validate(obj, schema)

    @staticmethod
    def summarize_selected_recipes_ingredients(obj: dict):
        schema = {
            "type": "object",
            "properties": {
                "recipe_list": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        }
        return validate(obj, schema)


class ApiSchema:
    @staticmethod
    def update_ingredient_field_request_schema(obj: dict):
        schema = {
            "type": "object",
            "patternProperties": {
                "^.*$": {
                    "properties": {
                        "supermarket": {"type": "array"},
                        "unit": {"type": "array"}
                    }
                }
            }
        }
        return validate(obj, schema)
