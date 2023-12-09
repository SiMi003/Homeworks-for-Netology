import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    
    # loading data from the file
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    # getting the tree root
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    
    list_ = []
    list_draft = []
    for item in xml_items:
        list_draft = (item.find('description').text).strip().split()
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
    print(read_xml('newsafr.xml'))
