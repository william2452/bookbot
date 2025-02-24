import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    word_count = 0
    with open(sys.argv[1]) as f:
        file_contents = f.read()

        #Uses the string split function to count the number of words in the text.
        words = file_contents.split()
        for x in words:
            word_count += 1
        print("Number of words =", word_count, "\n")

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

        #Defines a function that takes a dictionary as an argument and
        #returns a list of keys in the that are alphabetical characters
        def sort_on(dict):
            key = []
            for value in dict.values():
                key.append(value)            
            return key

        #Sorts the list of dictionaries from most used letters to least
        dict_list.sort(key=sort_on, reverse=True)

        #Prints the list of dictionaries in a clean, more legible way
        for dict in dict_list:
            for k, v in dict.items():
                print(f"The '{k}' character was found '{v}' times in the text.")


if __name__ == "__main__":
    main()