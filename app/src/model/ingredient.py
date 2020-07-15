from app.src.service import firebase
from app.src.model.model_constants import INGREDIENTS_NODE_REF, INGREDIENTS_SUB_NODE_REF_FORMAT, \
    INGREDIENTS_SUB_NODE_UNITS_REF_FORMAT, NEW_INGREDIENT_UNIT_REF, NEW_INGREDIENT_SUPERMARKET_REF
from app.src.model.unit import Unit
from app.src.model.supermarket import Supermarket

db = firebase.Firebase("firebase")


class Ingredient:
    def __init__(self, name: str = None, category: str = None, supermarket: str = None):
        self.name = name
        self.category = category
        self.supermarket = Supermarket()
        self.unit = Unit()

        self.attribute_dict = dict(name=self.name, category=self.category, supermarket=self.supermarket)

    @staticmethod
    def get_all_ingredients():
        return db.get(INGREDIENTS_NODE_REF)

    @staticmethod
    def get_ingredient(ingredient_id: str):
        return db.get(INGREDIENTS_SUB_NODE_REF_FORMAT.format(ingredient_id))

    def add_ingredient(self, ingredient_dict: dict):
        unit = ingredient_dict.get(NEW_INGREDIENT_UNIT_REF)
        supermarket = ingredient_dict.get(NEW_INGREDIENT_SUPERMARKET_REF)

        if isinstance(unit, str):
            unit = [unit]
            ingredient_dict[NEW_INGREDIENT_UNIT_REF] = unit
            
        if isinstance(supermarket, str):
            supermarket = [supermarket]
            ingredient_dict[NEW_INGREDIENT_SUPERMARKET_REF] = supermarket

        self.unit.add_unit(unit)
        self.supermarket.add_supermarket(supermarket)

        ingredient_child = db.child("", INGREDIENTS_NODE_REF)
        
        if ingredient_child.get():
            new_post_ref = db.add(INGREDIENTS_NODE_REF, ingredient_dict)
            
        else:
            new_post_ref = ingredient_child.push(ingredient_dict)
            
        return {new_post_ref.key: ingredient_dict}

    @staticmethod
    def update_ingredient_units(ingredient_id: str, new_unit: str):
        ingredient_unit_child = db.child("", INGREDIENTS_SUB_NODE_UNITS_REF_FORMAT.format(ingredient_id))
        if isinstance(new_unit, str):
            new_unit = [new_unit]
        ingredient_unit_updated = list(set(ingredient_unit_child.get() + new_unit))
        ingredient_unit_child.set(ingredient_unit_updated)

    @staticmethod
    def replace_ingredient(ingredient_dict: dict):
        db.set(INGREDIENTS_NODE_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def update_ingredient(ingredient_dict: dict):
        db.update(INGREDIENTS_NODE_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def delete_ingredient(ingredient_id: str):
        db.delete(INGREDIENTS_SUB_NODE_REF_FORMAT.format(ingredient_id))
        return ingredient_id



