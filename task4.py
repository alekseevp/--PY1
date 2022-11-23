import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, separator=',', new_line='\n') -> list[dict]:
    data_list = []
    json_dict = {}
    json_list = []
    with open(filename, 'r') as file:
        for line in file:
            data_list.append(line.rstrip(new_line))
    headers_list = data_list[0].split(separator)
    data_list = [i.split(separator) for i in data_list[1:]]
    for row in data_list:
        for i, cell in enumerate(row):
            json_dict[headers_list[i]] = cell
        json_list.append(json_dict.copy())
    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
