from collections import Counter
from collections.abc import Generator
# from pyexcel_ods import get_data
from app.src.contants import INGREDIENTS_NAME_FORMAT, RECIPES_SHEET_NAME, RECIPES_DETAILS, INGREDIENTS_SHEET_NAME


def _dict_counter(_dict: dict, key: str):
    counted_dict = Counter(dict())
    for r in _dict:
        counted_dict += Counter(_dict.get(r).get(key))
    return counted_dict


def ods_list_to_dict_default(ods_list: list):
    ods_dict = {
        ods_list[i][0]: {
            ods_list[0][j]: ods_list[i][j]
            for j in range(1, len(ods_list[0]))
        } for i in range(1, len(ods_list) - 2)
    }
    return ods_dict


def ods_to_dict(path: str):
    data = get_data(path)

    # Recipes
    recipes_data_list = dict(data).get(RECIPES_SHEET_NAME)
    recipe_dict = {
        recipes_data_list[0][i]: {
            INGREDIENTS_NAME_FORMAT: {

            }
        } for i in range(1, len(recipes_data_list[0]))
    }
    j = 1
    for recipe in recipe_dict:
        for ingredient_list in recipes_data_list[1:]:
            try:
                if isinstance(ingredient_list[j], int) or isinstance(ingredient_list[j], float):
                    recipe_dict[recipe][INGREDIENTS_NAME_FORMAT][ingredient_list[0]] = ingredient_list[j]
            except Exception as e:
                pass
        j += 1

    # Recipes details
    recipes_details_data_list = dict(data).get(RECIPES_DETAILS)
    recipes_details_dict = ods_list_to_dict_default(recipes_details_data_list)

    # Merge recipe details with recipes dictionary
    merged_dict = merge_dicts(recipe_dict, recipes_details_dict)

    # Ingredients
    ingredients_data_list = dict(data).get(INGREDIENTS_SHEET_NAME)
    ingredient_dict = ods_list_to_dict_default(ingredients_data_list)

    return merged_dict, ingredient_dict


def merge_dicts(a, b, path=None):
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dicts(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a


def string_formatter(string: str):
    return '_'.join(string.lower().split(' '))


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, pre + [key]):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, pre + [key]):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]


def value_collector(walked_dict_generator: Generator, key: str):
    collection = list()
    for element in walked_dict_generator:
        if key in element:
            idx = element.index(key)
            collection.append(element[idx + 1])
    return collection
