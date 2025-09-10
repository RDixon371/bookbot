def word_count(text):
    return len(text.split())

def char_count(text):
    lowercase = text.lower()
    list_of_chars = [char for char in lowercase]
    char_dict = {}
    for char in list_of_chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
    
def num_key(d):
     return d["num"]

def sort_dict(num_char_dict):
    list_to_be_sorted = []
    for ch in num_char_dict:
        list_to_be_sorted.append({"char": ch, "num": num_char_dict[ch]})
    list_to_be_sorted.sort(reverse=True, key=num_key)
    return list_to_be_sorted


