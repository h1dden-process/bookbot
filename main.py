from stats import *
import sys

try:
    book_path = sys.argv[1]
    
except:

    print("Usage: python3 main.py <path_to_book>")

    sys.exit(1)


def get_book_text(filepath): 

    with open(filepath) as f:
        content = f.read()

    return content

def main(): 

    book = get_book_text(book_path)

    print("============ BOOKBOT ============")

    print(f"Analysing book found at {sys.argv[1]}...")
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
