from typing import Union, List
from app.src.model.model_constants import UNIT_ALL_REF
from app.src.service import firebase

db = firebase.Firebase('firebase')


class Unit:
    @staticmethod
    def get_unit_list():
        return db.get(UNIT_ALL_REF)

    def add_unit(self, new_units: Union[int, List[str]]):
        if isinstance(new_units, str):
            new_units = [new_units]

        unit_child = db.child("", UNIT_ALL_REF)
        if unit_child.get():
            db_unit_list = self.get_unit_list()
            db_unit_list = list(set(db_unit_list + new_units))
            unit_child.set(db_unit_list)
        else:
            unit_child.set(new_units)
        return {UNIT_ALL_REF: new_units}

    def delete_unit(self, units: Union[int, List[str]]):
        if isinstance(units, str):
            units = [units]

        db_unit_list = self.get_unit_list()

        for unit in units:
            db_unit_list.remove(unit)

        unit_child = db.child("", UNIT_ALL_REF)
        unit_child.set(db_unit_list)

        return {UNIT_ALL_REF: units}
