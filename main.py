
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # print(count_words(text))
    unsorted_dict = count_letters(text)
    # print(unsorted_dict)
    # print(convert_dict_to_listdicts(unsorted_dict))
    unsorted_multi_dict=convert_dict_to_listdicts(unsorted_dict)
    unsorted_multi_dict.sort(reverse=True, key=sort_on)
    # print(unsorted_multi_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    print()

    for item in unsorted_multi_dict:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["count"]} times")
    


def convert_dict_to_listdicts (unsorted_dict):
    finallist =[]
    for key in unsorted_dict:
        finallist.append({"char":key,"count":unsorted_dict[key]})
    return finallist

def sort_on(dict):
    return dict["count"]





def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(booktext):
    words = booktext.split()
    # print(words)
    sum = 0
    for i in words:
        sum+=1
    return sum


def count_letters(booktext):
    text_lowered = booktext.lower()
    mydict = {}

    for char in text_lowered:
        if (char in mydict):
            mydict[char] = mydict[char] + 1
        else:
             mydict[char] = 1

    return mydict




main()