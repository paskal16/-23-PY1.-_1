# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    mydata =[]
    with open(INPUT_FILENAME) as f:
        data_ = csv.DictReader(f)

        for i in data_:

            mydata.append(i)



    with open('output_json', 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(mydata, indent=4))





if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open('output_json') as output_f:
        for line in output_f:
            print(line, end="")
