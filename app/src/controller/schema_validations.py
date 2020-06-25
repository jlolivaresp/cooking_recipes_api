from jsonschema import validate

from app.src.model.model_constants import GENERAL_ID_REF, INGREDIENTS_SUB_NODE_NAME_REF, NEW_INGREDIENT_UNIT_REF, \
    NEW_INGREDIENT_SUPERMARKET_REF, INGREDIENT_SUB_NODE_CATEGORY_NAME, RECIPES_SUB_NODE_NAME_REF, \
    RECIPES_SUB_NODE_DESCRIPTION_REF, RECIPES_SUB_NODE_LINK_REF, RECIPE_SUB_NODE_INGREDIENTS_REF, \
    RECIPE_INGREDIENT_UNIT_REF, RECIPE_INGREDIENT_QUANTITY_REF, RECIPE_IDS_REF, INGREDIENT_SUB_NODE_UNIT_REF, \
    INGREDIENT_SUB_NODE_SUPERMARKET_REF


class ModelSchema:
    @staticmethod
    def get_delete_node_request_schema(obj: dict):
        schema = {
            "type": "object",
            "properties": {
                GENERAL_ID_REF: {"type": "string"}
            },
            "required": [GENERAL_ID_REF]
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
                INGREDIENTS_SUB_NODE_NAME_REF: {"type": "string"},
                NEW_INGREDIENT_UNIT_REF: {"type": "array"},
                NEW_INGREDIENT_SUPERMARKET_REF: {"type": "array"},
                INGREDIENT_SUB_NODE_CATEGORY_NAME: {"type": "string"}
            },
            "required": [INGREDIENTS_SUB_NODE_NAME_REF, NEW_INGREDIENT_UNIT_REF,
                         NEW_INGREDIENT_SUPERMARKET_REF, INGREDIENT_SUB_NODE_CATEGORY_NAME]
        }
        return validate(obj, schema)

    @staticmethod
    def add_recipe_request_schema(obj: dict):
        schema = {
            "type": "object",
            "properties": {
                RECIPES_SUB_NODE_NAME_REF: {"type": "string"},
                RECIPES_SUB_NODE_DESCRIPTION_REF: {"type": "string"},
                RECIPES_SUB_NODE_LINK_REF: {"type": "string"},
                RECIPE_SUB_NODE_INGREDIENTS_REF: {
                    "type": "object",
                    "patternProperties": {
                        "^.*$": {
                            "anyOf": [{"type": "object"}],
                            "properties": {
                                RECIPE_INGREDIENT_QUANTITY_REF: {"type": "number"},
                                RECIPE_INGREDIENT_UNIT_REF: {"type": "string"}
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
                RECIPE_IDS_REF: {
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
                        INGREDIENT_SUB_NODE_SUPERMARKET_REF: {"type": "array"},
                        INGREDIENT_SUB_NODE_UNIT_REF: {"type": "array"}
                    }
                }
            }
        }
        return validate(obj, schema)
