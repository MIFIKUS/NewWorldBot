from MainClasses.Database.database import Database


class ReadDB(Database):
    def switching_between_characters(self):
        '''функция возвращает сортированный список координат персонажей которые прикрепленны к серверам'''

        list_of_characters_cords = self.make_query(
                "SELECT " 
                "character_server.character_id, "
                "servers.position_x, "
                "servers.position_y, "
                "cords_for_characters.position_x, "
                "cords_for_characters.position_y "
                "FROM "
                "character_server "
                "JOIN characters ON characters.character_id = character_server.character_id "
                "JOIN servers ON servers.server_id = character_server.server_id "
                "JOIN cords_for_characters ON cords_for_characters.cords_id = characters.position;")

        return sorted(list_of_characters_cords)

    def get_data_from_table_of_orders(self, character_id, table_name):
        table = self.make_query(f"SELECT * FROM {table_name} where character_id = {character_id};")
        return [[x[2], x[3], x[4], x[5]] for x in table]

    def get_data_from_purchase_and_sale(self, character_id):
        purchase_and_sale = self.make_query(f"SELECT * FROM purchase_and_sale where character_id = {character_id};")
        return [[x[2], x[3], x[4], x[5], x[6]] for x in purchase_and_sale]


read_db = ReadDB()
#print(read_db.switching_between_characters())
#print(read_db.get_data_from_table_of_orders('1', "sell_orders"))
#print(read_db.get_data_from_purchase_and_sale(2))

