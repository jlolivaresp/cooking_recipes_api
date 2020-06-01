from collections import Counter
from pyexcel_ods import get_data
from app.contants import INGREDIENTS_NAME_FORMAT


def _dict_counter(_dict: dict, key: str):
    counted_dict = Counter(dict())
    for r in _dict:
        counted_dict += Counter(_dict.get(r).get(key))
    return counted_dict


def ods_parser(path: str, sheet_name: str):
    data = get_data(path)
    data_list = dict(data).get(sheet_name)
    recipe_dict = {
        data_list[0][i]: {
            INGREDIENTS_NAME_FORMAT: {}
        } for i in range(1, len(data_list[0]))
    }
    j = 1
    for recipe in recipe_dict:
        for ingredient_list in data_list[1:]:
            try:
                if isinstance(ingredient_list[j], int) or isinstance(ingredient_list[j], float):
                    recipe_dict[recipe][INGREDIENTS_NAME_FORMAT][ingredient_list[0]] = ingredient_list[j]
            except Exception as e:
                pass
        j += 1
    return recipe_dict


print(ods_parser("/home/jorge/Downloads/db.ods", "Sheet2"))
