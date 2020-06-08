from app.model.model_constants import SUPERMARKET_ALL_REF, SUPERMARKET_REF
from app.service import firebase

db = firebase.Firebase('firebase')


class Supermarket:
    @staticmethod
    def get_all_supermarkets():
        return db.get(SUPERMARKET_ALL_REF)

    @staticmethod
    def get_supermarket(supermarket_id: str):
        return db.get(SUPERMARKET_REF.format(supermarket_id))

    @staticmethod
    def add_supermarket(supermarket_dict: dict):
        new_post_ref = db.add(SUPERMARKET_ALL_REF, supermarket_dict)
        return {new_post_ref.key: supermarket_dict}

    @staticmethod
    def replace_supermarket(supermarket_dict: dict):
        db.set(SUPERMARKET_ALL_REF, supermarket_dict)
        return supermarket_dict

    @staticmethod
    def update_supermarket(supermarket_dict: dict):
        db.update(SUPERMARKET_ALL_REF, supermarket_dict)
        return supermarket_dict

    @staticmethod
    def delete_supermarket(supermarket_id: str):
        db.delete(SUPERMARKET_REF.format(supermarket_id))
        return supermarket_id
