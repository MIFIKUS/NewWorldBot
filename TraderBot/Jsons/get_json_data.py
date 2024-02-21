import TraderBot.shared_variables as shared_variables
import json


def get_json():
    path = shared_variables.path_to_json + "categories_cords.json"
    if shared_variables.checking_for_beggar is True:
        path = shared_variables.path_to_json + "cords_of_categories_for_beggars.json"
    with open(path, 'r', encoding='utf-8') as data:
        categories = json.load(data)
    return categories



