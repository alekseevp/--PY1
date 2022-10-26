dict = {}


def get_count_char(str_):
    str_lower = str_.lower()
    for symbol in str_lower:
        if symbol.isalpha():
            if symbol not in dict: #без двухуровнего условия оно отказывается работать
                dict[symbol] = 0
            dict[symbol] += 1


    return dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))


def get_percentage(dict_):
    pct_dict = {}
    summa = sum(dict_.values())
    for k, v in dict_.items():
        pct = round(v * 100.0 / summa)
        pct_dict.update({k: pct})
    return pct_dict

print(get_percentage(dict))