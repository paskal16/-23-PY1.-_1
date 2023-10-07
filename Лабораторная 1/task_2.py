list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_players = int(len(list_players)/2)
first_team = list_players[:num_players]
second_team = list_players[num_players::]
print(first_team)
print(second_team)
