def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lowered_text = text.lower()
    num_words = get_num_words(text)
    letter_count = get_num_letters(lowered_text)
    letter_list = convert_to_list(letter_count)
    letter_list.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for letter in letter_list:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")
    

def convert_to_list(dict):
    result = []
    for key, value in dict.items():
        if key.isalpha():
            result.append({"letter": key, "num": value})
    return result

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letters(lowered_text):
    letter_count = {}
    for char in lowered_text:
        letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count
    
def sort_on(letter_count):
    return letter_count["num"]

main()
