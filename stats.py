import sys


def get_num_words():
    word_count = 0
    with open(sys.argv[1]) as f:
        file_contents = f.read()

    #Uses the string split function to count the number of words in the text.
    words = file_contents.split()
    for x in words:
        word_count += 1
    print(f"{word_count} words found in the document\n")

    #Create a dictionary of characters appearing in the text
    #Made it all lower-case so it wouldn't count the same letter twice
    char_dict = {}
    lowered_string = file_contents.lower()
    for spot in lowered_string:
        if spot in char_dict:
            char_dict[spot] += 1
        else:
            char_dict[spot] = 1

    #Creates a list of dictionaries from the former dictionary
    #Contains only letter characters
    dict_list = []
    for key in char_dict:
        if key.isalpha():
            dict_list.append({key: char_dict[key]})

    return dict_list