import sys
from stats import get_num_words

def main():
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    """
    
    dict_list = get_num_words()
    
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
            print(f"Number of {k}'s: {v}")


if __name__ == "__main__":
    main()