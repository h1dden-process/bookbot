from stats import *
import sys

def get_book_text(filepath): 

    with open(filepath) as f:
        content = f.read()

    return content

def main(): 

    book = get_book_text(f'')

    print("============ BOOKBOT ============")

    print("Analysing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words") 
    print("--------- Character Count -------")
    freq_list = get_word_freq(book)
    sorted_list = sorted_freq(freq_list)

    for d in sorted_list:
        
        if d["char"].isalpha():
            char = d["char"]
            num = d["num"]

            print(f"{char}: {num}")
    
    
    print("============= END ===============")


main()
