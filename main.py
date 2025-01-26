def main():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)       <-- This prints the whole text.

        words = file_contents.split()
        for x in words:
            word_count += 1
        print("Number of words = ", word_count)

        
        
        char_dict = {}
        lowered_string = file_contents.lower()
        for spot in lowered_string:
            if spot in char_dict:
                char_dict[spot] += 1
            else:
                char_dict[spot] = 1
        print(char_dict)
if __name__ == "__main__":
    main()