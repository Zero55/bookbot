from stats import count_total_words
from stats import number_of_each_char
def get_book_text(book):
    with open(book) as f:
        return f.read()


if __name__ == '__main__':
    book_path = 'books/frankenstein.txt'
    content = get_book_text(book_path)
    count_total_words(content)
    print(number_of_each_char(content))
    #if content:
       # print(content)