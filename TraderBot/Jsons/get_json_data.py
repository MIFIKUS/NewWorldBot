import json


class GetJsonData:
    checking_for_beggar = False
    balance_of_beggar = None

    @staticmethod
    def get_json():
        path = "E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\categories_cords.json"
        if GetJsonData.checking_for_beggar is True:
            path = "E:\\projects\\NewWorldBot\\TraderBot\\Jsons\\cords_of_categories_for_beggars.json"

        with open(path, 'r', encoding='utf-8') as data:
            categories = json.load(data)
        #print([categories.get(i) for i in categories.keys()]))
        return categories
        #{categories.get(i) for i in categories}



