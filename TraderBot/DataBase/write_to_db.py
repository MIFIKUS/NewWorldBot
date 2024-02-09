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

#listik = [['Refined woods', 'Timber', '0.11', '703.'], ['Refined woods', 'Timber', '0.12', '613.'], ['Refined woods', 'Timber', '0.12', '1777'], ['Refined woods', 'Timber', '0.13', '1215'], ['Refined woods', 'Timber', '0.13', '396'], ['Refined woods', 'Timber', '0.13', '1723'], ['Refined woods', 'Timber', '0.13', '747'], ['Refined woods', 'Timber', '0.13', '140'], ['Refined woods', 'Timber', '0.13', '2883'], ['Refined woods', 'Timber', '0.16', '10000'], ['Refined woods', 'Timber', '0.16', '3799'], ['Refined woods', 'Timber', '0.18', '1920'], ['Refined woods', 'Timber', '0.18', '1186'], ['Refined woods', 'Timber', '0.19', '6412'], ['Refined woods', 'Timber', '0.20', '1182'], ['Refined woods', 'Timber', '0.20', '86'], ['Refined woods', 'Timber', '0.20', '10000'], ['Refined woods', 'Timber', '0.21', '2380'], ['Refined woods', 'Timber', '0.22', '9']]

write_to_db = WriteToDB()
#write_to_db.recording_orders(1, 'sell_orders', listik)
#write_to_db.recording_orders(1, 'buy_orders', listik)
#write_to_db.delete_character_positions(1, "sell_orders")
#write_to_db.record_purchase_and_sale_prices(2, initial_list)
