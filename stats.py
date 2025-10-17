def get_num_words(book):

    return len(book.split())

def get_word_freq(book):

    freq_list = {}

    l_book = book.lower()

    for char in l_book:
        
        if not char in freq_list:
            freq_list[char] = 1
        else:
            freq_list[char] += 1

     
    return freq_list

def sort_on(item):

    return item["num"]

def sorted_freq(freq): 

    new_list = []

    for key in freq: 
        
        new_dict = {}

        new_dict["char"] = key 
        new_dict["num"] = freq[key]

        new_list.append(new_dict)

    
    new_list.sort(reverse=True, key=sort_on)

    return new_list
