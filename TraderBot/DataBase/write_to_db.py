from MainClasses.Database.database import Database


class WriteToDB(Database):
    def recording_orders(self, character_id, table_name, data):
        finished_list = [[character_id, item[0], item[1], round(float(item[2]), 2), item[3]] for item in data]

        query = (f"INSERT INTO {table_name} "
                 "(character_id, category_name, product_name, price, count) "
                 "VALUES "
                 f"(%s, %s, %s, %s, %s)")

        self.cursor.executemany(query, finished_list)

    def record_transactions_goods(self, character_id, data):
        finished_list = [[character_id, item[0], item[1]] for item in data]

        query = (f"INSERT INTO transactions_goods "
                 "(character_id, product_name, how_many_bought_it) "
                 "VALUES "
                 f"(%s, %s, %s)")

        self.cursor.executemany(query, finished_list)

    def register_sale_of_goods(self, character_id, product_name, value):
        self.make_query(f"UPDATE transactions_goods SET how_many_were_sold = IFNULL(how_many_were_sold, 0) + {value} "
                        f"where character_id = {character_id} AND product_name = '{product_name}'")

    def record_purchase_and_sale_prices(self, character_id, data):
        finished_list = [[character_id, item[0], item[1], item[2], item[3], item[4]] for item in data]

        query = (f"INSERT INTO purchase_and_sale "
                 "(character_id, product_name, purchase_price, sale_price, quantity, ratio) "
                 "VALUES "
                 f"(%s, %s, %s, %s, %s, %s)")

        self.cursor.executemany(query, finished_list)

    def delete_all_from_table(self, table_name):
        self.make_query(f"DELETE FROM {table_name};")

    def delete_all_orders(self):
        self.make_query(f"DELETE FROM sell_orders;")
        self.make_query(f"DELETE FROM buy_orders;")
        self.make_query(f"DELETE FROM purchase_and_sale;")

    def delete_character_positions(self, character_id, table_name):
        self.make_query(f"delete FROM {table_name} where character_id = {character_id};")

#listik = [['Refined woods', 'Timber', '0.11', '703.'], ['Refined woods', 'Timber', '0.12', '613.'], ['Refined woods', 'Timber', '0.12', '1777'], ['Refined woods', 'Timber', '0.13', '1215'], ['Refined woods', 'Timber', '0.13', '396'], ['Refined woods', 'Timber', '0.13', '1723'], ['Refined woods', 'Timber', '0.13', '747'], ['Refined woods', 'Timber', '0.13', '140'], ['Refined woods', 'Timber', '0.13', '2883'], ['Refined woods', 'Timber', '0.16', '10000'], ['Refined woods', 'Timber', '0.16', '3799'], ['Refined woods', 'Timber', '0.18', '1920'], ['Refined woods', 'Timber', '0.18', '1186'], ['Refined woods', 'Timber', '0.19', '6412'], ['Refined woods', 'Timber', '0.20', '1182'], ['Refined woods', 'Timber', '0.20', '86'], ['Refined woods', 'Timber', '0.20', '10000'], ['Refined woods', 'Timber', '0.21', '2380'], ['Refined woods', 'Timber', '0.22', '9']]


write_to_db = WriteToDB()

#write_to_db.register_sale_of_goods(4, 'Timber', -4)
#datas = [['Timber', 203], ['Fibers', 166], ['Coarse Leather', 99], ['Rawhide', 109], ['Silver Ingot', 1404], ['Green Wood', 76]]
#write_to_db.record_transactions_goods(7, [['Coarse Leather', 339], ['Rawhide', 214]])

#write_to_db.make_query("CREATE TABLE transactions_goods(product_id INT PRIMARY KEY AUTO_INCREMENT, character_id INT, product_name varchar(50), how_many_bought_it INT, how_many_were_sold FLOAT, FOREIGN KEY (character_id) REFERENCES characters(character_id))")
#write_to_db.recording_orders(1, 'sell_orders', listik)
#write_to_db.recording_orders(1, 'buy_orders', listik)

#write_to_db.delete_character_positions(4, "sell_orders")

#write_to_db.make_query("ALTER TABLE purchase_and_sale CHANGE count ratio INT;")
#write_to_db.record_purchase_and_sale_prices(2, initial_list)
