from app.src.service import firebase
from app.src.model.model_constants import INGREDIENT_ALL_REF, INGREDIENT_REF, INGREDIENT_UNIT_REF
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
        return db.get(INGREDIENT_ALL_REF)

    @staticmethod
    def get_ingredient(ingredient_id: str):
        return db.get(INGREDIENT_REF.format(ingredient_id))

    def add_ingredient(self, ingredient_dict: dict):
        unit = ingredient_dict.get("unit")
        supermarket = ingredient_dict.get("supermarket")

        if isinstance(unit, str):
            unit = [unit]
            ingredient_dict["unit"] = unit
        if isinstance(supermarket, str):
            supermarket = [supermarket]
            ingredient_dict["supermarket"] = supermarket

        self.unit.add_unit(unit)
        self.supermarket.add_supermarket(supermarket)

        ingredient_child = db.child("", INGREDIENT_ALL_REF)
        if ingredient_child.get():
            new_post_ref = db.add(INGREDIENT_ALL_REF, ingredient_dict)
        else:
            new_post_ref = ingredient_child.push(ingredient_dict)
        return {new_post_ref.key: ingredient_dict}

    @staticmethod
    def update_ingredient_units(ingredient_id: str, new_unit: str):
        ingredient_unit_child = db.child("", INGREDIENT_UNIT_REF.format(ingredient_id))
        ingredient_unit_updated = list(set(ingredient_unit_child.get() + [new_unit]))
        ingredient_unit_child.set(ingredient_unit_updated)

    @staticmethod
    def replace_ingredient(ingredient_dict: dict):
        db.set(INGREDIENT_ALL_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def update_ingredient(ingredient_dict: dict):
        db.update(INGREDIENT_ALL_REF, ingredient_dict)
        return ingredient_dict

    @staticmethod
    def delete_ingredient(ingredient_id: str):
        db.delete(INGREDIENT_REF.format(ingredient_id))
        return ingredient_id



