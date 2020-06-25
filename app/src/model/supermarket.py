from app.src.model.model_constants import SUPERMARKET_ALL_REF, SUPERMARKETS_SUB_NODE_REF_FORMAT
from app.src.service import firebase

db = firebase.Firebase("firebase")


class Supermarket:
    @staticmethod
    def get_supermarket_list():
        return db.get(SUPERMARKET_ALL_REF)

    def add_supermarket(self, new_supermarkets: list):
        supermarket_child = db.child("", SUPERMARKET_ALL_REF)
        if supermarket_child.get():
            db_unit_list = self.get_supermarket_list()
            db_unit_list = list(set(db_unit_list + new_supermarkets))
            supermarket_child.set(db_unit_list)
        else:
            supermarket_child.set(new_supermarkets)
        return {SUPERMARKET_ALL_REF: new_supermarkets}

    @staticmethod
    def delete_supermarket(supermarket_id: str):
        db.delete(SUPERMARKETS_SUB_NODE_REF_FORMAT.format(supermarket_id))
        return supermarket_id
