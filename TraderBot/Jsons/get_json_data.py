import TraderBot.shared_variables as shared_variables
import json


def get_json():
    path = "E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json"
    if shared_variables.checking_for_beggar is True:
        path = "E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\cords_of_categories_for_beggars.json"
    with open(path, 'r', encoding='utf-8') as data:
        categories = json.load(data)
    return categories



