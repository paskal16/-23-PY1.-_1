
def find_common_participants(str1, str2, sep_=','):
    lst1 = list(set(str1.split(sep_)).intersection(set(str2.split(sep_))))
    lst1.sort()
    return lst1



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"



print(find_common_participants(participants_first_group, participants_second_group, '|'))
