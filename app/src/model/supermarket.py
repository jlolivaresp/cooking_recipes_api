from app.src.model.model_constants import SUPERMARKETS_NODE_REF, SUPERMARKETS_SUB_NODE_REF_FORMAT
from app.src.service import firebase

db = firebase.Firebase("firebase")


class Supermarket:
    @staticmethod
    def get_supermarket_list():
        return db.get(SUPERMARKETS_NODE_REF)

    def add_supermarket(self, new_supermarkets: list):
        if isinstance(new_supermarkets, str):
            new_supermarkets = [new_supermarkets]

        supermarket_child = db.child("", SUPERMARKETS_NODE_REF)
        if supermarket_child.get():
            db_unit_list = self.get_supermarket_list()
            db_unit_list = list(set(db_unit_list + new_supermarkets))
            supermarket_child.set(db_unit_list)
        else:
            supermarket_child.set(new_supermarkets)
        return {SUPERMARKETS_NODE_REF: new_supermarkets}

    def delete_supermarket(self, supermarkets: str):
        if isinstance(supermarkets, str):
            supermarkets = [supermarkets]

        db_supermarket_list = self.get_supermarket_list()

        for supermarket in supermarkets:
            db_supermarket_list.remove(supermarket)

        supermarket_child = db.child("", SUPERMARKETS_NODE_REF)
        supermarket_child.set(db_supermarket_list)

        return {SUPERMARKETS_NODE_REF: supermarkets}
