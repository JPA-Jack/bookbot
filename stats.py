def split_words (file_contents):
    words_list = file_contents.split()
    return len(words_list)

def count_ch (words):
    ch_dict = {}
    word_list = words.split()
    temp = 0
    for word in word_list:
        word = word.lower()
        for ch in word:   
            if ch in ch_dict:
                temp = ch_dict[ch]
                ch_dict[ch] = temp + 1
            else:
                ch_dict[ch] = 1
    return ch_dict
    
def sort_on (items):
    return items["num"]

def split_dict (dict):
    dict_list = []
    dict_to_split = {}
    for i in dict:
        dict_to_split["name"] = i
        dict_to_split["num"] = dict[i]
        dict_list.append(dict_to_split)
        dict_to_split = {}
    return dict_list

