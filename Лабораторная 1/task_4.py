users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
new_dict = {"Общее количество": 0,
            "Уникальные посещения": 0}
new_dict["Общее количество"] = len(users)
new_dict["Уникальные посещения"] = len(set(users))
print(new_dict)