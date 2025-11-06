import sys
from stats import count_total_words
from stats import number_of_each_char
from stats import listed_dict

def get_book_text(book):
    with open(book) as f:
        return f.read()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        content = get_book_text(book_path)
        char_counts = number_of_each_char(content)
        sorted_list = listed_dict(char_counts)
        print("============ BOOKBOT ============")
        print("----------- Word Count ----------")
        count_total_words(content)
        print("--------- Character Count -------")
        for item in sorted_list:
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    