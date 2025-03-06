

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


