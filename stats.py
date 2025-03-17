def get_num_words(text):
    word_list = text.split()
    num = len(word_list)
    return num
    
def get_characters(text):
    char_dict = {}
    for i in text.lower():
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    return char_dict

def sorted_list(char_dict):
    char_list = []
    for key in dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True)):
        if key.isalpha():
            char_list.append(f"{key}: {char_dict[key]}")
    return char_list