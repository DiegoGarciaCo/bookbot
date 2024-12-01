def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        word_count = count_words(text)
        chars = char_count(text)
        list_of_chars = [{'character': key, 'count': value} for key, value in chars.items()]
        list_of_chars.sort(reverse=True, key=sort_on)
        print("--- Begin Report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for item in list_of_chars:
            character = item['character']
            count = item['count']
            print(f"The '{character}' character was found {count} times.")
        

def sort_on(dict):
    return dict["count"]


def char_count(book):
    lower_case = book.lower()
    count = {}
    for char in lower_case:
        if char in count:
            count[char] += 1
        elif char.isalpha(): 
             count[char] = 1
    return count


def count_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

main()