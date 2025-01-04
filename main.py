def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_char_count(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    words = text.split()

    return len(words)


def count_chars(text):
    count = {}

    for char in text:
        char = char.lower()
        
        if char.isalpha() == True:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count


def sort_on(dict):
    return dict["num"]


def sort_char_count(char_dict):
    char_list = []

    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})

    
    char_list.sort(reverse=True, key=sort_on)

    return char_list

main()
