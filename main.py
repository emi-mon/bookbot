def count_words(text):
    #returns wordcount of given string
    words = text.split()
    return len(words)

def count_letters(text):
    #returns count of individual letters in a given string
    letters = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }
    text = text.lower()
    for letter in text:
        if letter in letters:
            letters[letter] += 1
    return letters

def dict_to_list(dict):
    #transforms a dict to a list of dicts
    list = []
    for key in dict:
        list.append({"char": key, "count": dict[key]})
    return list

def sort_on(dict):
    return dict["count"]

def sort_list_of_dict(list):
    #sorts given list of dicts by char count
    list.sort(reverse=True, key=sort_on)

def print_data(text, path):
    #prints text stats prettily
    wordcount = count_words(text)
    list_of_dict = dict_to_list(count_letters(text))
    sort_list_of_dict(list_of_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words were found in the document")
    print()
    for i in range(0, len(list_of_dict)):
        print(f"The '{list_of_dict[i]["char"]}' character was found {list_of_dict[i]["count"]} times")
    print("--- End report ---")
    return None



def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
    
    #print(f"word count : {count_words(file_contents)}")
    #print(f"letter count : {count_letters(file_contents)}")
    print_data(file_contents, path)

main()