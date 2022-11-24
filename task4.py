import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, separator=',', new_line='\n') -> list[dict]:
    json_list = []
    with open(filename, 'r') as file:
        header = file.readline().rstrip(new_line).split(separator)
        for line in file:
            values = line.rstrip(new_line).split(separator)
            json_list.append(dict(zip(header, values)))
    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
