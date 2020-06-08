from app.model.model_constants import UNIT_ALL_REF, UNIT_REF
from app.service import firebase

db = firebase.Firebase('firebase')


class Unit:
    @staticmethod
    def get_all_units():
        return db.get(UNIT_ALL_REF)

    @staticmethod
    def get_unit(unit_id: str):
        return db.get(UNIT_REF.format(unit_id))

    @staticmethod
    def add_unit(unit_dict: dict):
        new_post_ref = db.add(UNIT_ALL_REF, unit_dict)
        return {new_post_ref.key: unit_dict}

    @staticmethod
    def replace_unit(unit_dict: dict):
        db.set(UNIT_ALL_REF, unit_dict)
        return unit_dict

    @staticmethod
    def update_unit(unit_dict: dict):
        db.update(UNIT_ALL_REF, unit_dict)
        return unit_dict

    @staticmethod
    def delete_unit(unit_id: str):
        db.delete(UNIT_REF.format(unit_id))
        return unit_id
