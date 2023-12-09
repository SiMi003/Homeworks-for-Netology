import json


def read_json(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # Ваш алгоритм
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    list_ = []
    list_draft = []
    for item in json_data["rss"]["channel"]["items"]:
        list_draft = item["description"].strip().split()
        for el in list_draft:
            if len(el) > word_max_len:
                list_.append(el)
        
    from collections import Counter
    dict_ = Counter(list_)
    raiting = sorted(list(dict_.items()), 
                     key=lambda el: int(el[1]), reverse = True)[:top_words_amt]
    popular_words = []
    for el in raiting:
        popular_words.append(el[0])
        
    return popular_words
            

if __name__ == '__main__':
    print(read_json('newsafr.json'))




# import xml.etree.ElementTree as ET


# def read_xml(file_path, word_max_len=6, top_words_amt=10):
#     """
#     функция для чтения файла с новостями.
#     """
#     # Ваш алгоритм


# if __name__ == '__main__':
#     print(read_xml('newsafr.xml'))