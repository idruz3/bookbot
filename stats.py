def numbers_of_words(text):
    split = text.split()
    return len(split)


def get_count_words(text):
    dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in dict:
            dict[lowered_char] += 1
        else:
            dict[lowered_char] = 1
    return dict

def sort_on(dict):
    return dict[1]

def get_sorted(dict):
    pairs = []
    for char in dict:
        if char.isalpha():
            pairs.append((char, dict[char]))
    
    # Sort using sort_on function as key
    pairs.sort(key=sort_on, reverse=True)
    
    
    sorted_dict = {}
    for char, count in pairs:
        sorted_dict[char] = count
    
    return sorted_dict




