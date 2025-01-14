import string

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count = get_wordcount(book_text)
    character_count = count_characters(book_text)
    sorted_chars = sort_chars(character_count)

    for char in sorted_chars:
        print(f'The letter {char['char']} appears {char['count']} times')
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_wordcount(text):
    words = text.split()
    return(len(words))


def count_characters(text):
    characters = {}

    for letter in text:
        lower = letter.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1

    return characters

def sort_on(dict):
    return dict['count']

def sort_chars(dict):
    letters_only = {}

    #grab all the letters
    for char in dict:
        if char in string.ascii_lowercase:
            letters_only[char] = dict[char]

    #convert a dictionary to a list of dictionaries with 'char' and 'count' keys
    char_dict_list = [{'char': char, 'count': count} for char, count in letters_only.items()]
    
    #sorts list by count value
    char_dict_list.sort(reverse = True, key = sort_on)

    return char_dict_list


main()