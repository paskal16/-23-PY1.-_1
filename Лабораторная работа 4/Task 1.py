import json
FILENAME = 'input.json'
def task() -> float:
    sum_ =0
    with open (FILENAME) as f:
        data_ = json.load(f)
    for i in data_:
        sum_+= (i['score']*i['weight'])
    return round(sum_, 3)


    ...


print(task())
