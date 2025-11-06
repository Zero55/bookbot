def count_total_words(text):
    split_text = text.split()
    print(f"Found {len(split_text)} total words")

def number_of_each_char(texts):
    count_dict = {}
    for text in texts:
        lower = text.lower()
        count_dict[lower] = count_dict.get(lower, 0) + 1
    return count_dict

def sort_on(items):
    return items["num"]

def listed_dict(dict):
    dict_list = []
    for char, num in dict.items():
        if char.isalpha():
            dict_list.append({"char": char, "num": num})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

