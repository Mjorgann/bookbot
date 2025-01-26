def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    charac = character_count(text)
    sorted_list = sort_dict(charac)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

def sort_dict(x):
    list_of_keys = []
    for key in x:
        list_of_keys.append({"char": key, "num" : x[key]})
    list_of_keys.sort(reverse=True, key=sort_on)
    return list_of_keys


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    lowerx = text.lower()
    d = {}
    for i in lowerx:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

main()
