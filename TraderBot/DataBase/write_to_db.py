from MainClasses.Database.database import Database


class WriteToDB(Database):
    def recording_orders(self, character_id, table_name, data):
        finished_list = [[character_id, item[0], item[1], item[2], item[3]] for item in data]

        query = (f"INSERT INTO {table_name} "
                 "( character_id, category_name, product_name, price, count) "
                 "VALUES "
                 f"(%s, %s, %s, %s, %s)")

        self.cursor.executemany(query, finished_list)

    def record_purchase_and_sale_prices(self, character_id, data):
        finished_list = [[character_id, item[0], item[1], item[2], item[3], item[4]] for item in data]

        query = (f"INSERT INTO purchase_and_sale "
                 "(character_id, product_name, purchase_price, sale_price, ratio, count) "
                 "VALUES "
                 f"(%s, %s, %s, %s, %s, %s)")

        self.cursor.executemany(query, finished_list)

    def delete_character_positions(self, character_id, table_name):
        self.make_query(f"delete FROM {table_name} where character_id = {character_id};")


write_to_db = WriteToDB()
#write_to_db.recording_orders(2, 'sell_orders', initial_list)
#write_to_db.delete_character_positions(1, "purchase_and_sale")
#write_to_db.record_purchase_and_sale_prices(2, initial_list)
