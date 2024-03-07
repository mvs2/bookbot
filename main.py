def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        word_count = count_words(file_contents)
        words_dict = count_letters(file_contents)
        words_sorted_list = dict_to_sorted_list(words_dict)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for item in words_sorted_list:
             print(f"The '{item['word']}' character was found {item['num']} times")

def count_words(words):
    split_words = words.split() # splits string on whitespace
    return(len(split_words))

def count_letters(text):
    text = text.lower()
    letter_dict = {}
    for letter in text:
        if letter.isalpha() and letter in letter_dict:
            letter_dict[letter] += 1
        elif letter.isalpha():
            letter_dict[letter] = 1 
    return letter_dict

def sort_on(d):
    return d["num"]

def dict_to_sorted_list(word_dict):
    sorted_list = []
    for word in word_dict:
        sorted_list.append({"word": word, "num" : word_dict[word] })
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list

    


if __name__ == "__main__":
    main()

