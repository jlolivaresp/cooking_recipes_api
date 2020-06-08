from app.service import firebase
from app.model.model_constants import INGREDIENT_ALL_REF, INGREDIENT_REF

db = firebase.Firebase('firebase')


class Ingredient:
    def __init__(self, name: str = None, category: str = None, supermarket: str = None):
        self.name = name
        self.category = category
        self.supermarket = supermarket

        self.attribute_dict = dict(name=self.name, category=self.category, supermarket=self.supermarket)

    @staticmethod
    def get_all_ingredients():
        return db.get(INGREDIENT_ALL_REF)

    @staticmethod
    def get_ingredient(ingredient_id: str):
        return db.get(INGREDIENT_REF.format(ingredient_id))

    @staticmethod
    def add_ingredient(ingredient_dict: dict):
        new_post_ref = db.add(INGREDIENT_ALL_REF, ingredient_dict)
        return {new_post_ref.key: ingredient_dict}

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



