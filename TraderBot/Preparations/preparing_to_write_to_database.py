

class PreparingToWriteToDatabase:
    @staticmethod
    def preparing_list_for_orders(list_of_orders):
        count_for_count = 0
        count = 0

        for i in list_of_orders:
            list_of_orders[count_for_count][3].replace('.', '')
            if not i[3].replace('\n', '').isdigit():
                del list_of_orders[count_for_count]
            count_for_count += 1

        for _ in list_of_orders:
            if ',' in str(list_of_orders[count][2]):
                list_of_orders[count][2] = list_of_orders[count][2].replace(',', '.')

            if not str(list_of_orders[count][2]).replace('.', '').replace('\n', '').isdigit():
                if 0 < count < len(list_of_orders) - 1:
                    if list_of_orders[count - 1][1] == list_of_orders[count][1] == list_of_orders[count + 1][1]:
                        list_of_orders[count][2] = (float(list_of_orders[count-1][2]) + float(list_of_orders[count + 1][2])) / 2
                    elif list_of_orders[count - 1][1] != list_of_orders[count][1] == list_of_orders[count + 1][1]:
                        list_of_orders[count][2] = float(list_of_orders[count + 1][2])
                    elif list_of_orders[count - 1][1] == list_of_orders[count][1] != list_of_orders[count + 1][1]:
                        list_of_orders[count][2] = float(list_of_orders[count - 1][2])
                    else:
                        del list_of_orders[count]
            count += 1

        if list_of_orders[-1][2] == '' or list_of_orders[-1][3] == '':
            del list_of_orders[-1]

        if list_of_orders[0][2] == '' or list_of_orders[0][3] == '':
            del list_of_orders[0]

        return list_of_orders



