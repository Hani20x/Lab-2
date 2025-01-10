import csv

def find_books_by_author(author_name):
    with open('books-en.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        
        found_books = []
        for row in reader:
            try:
                year = int(row['Year-Of-Publication'])
                if year >= 2000 and author_name.lower() in row['Book-Author'].lower():
                    found_books.append(row)
            except ValueError:
                continue

    return found_books

author_name = input("Введите имя автора для поиска: ")

found_books = find_books_by_author(author_name)

if found_books:
    print(f"Найдено {len(found_books)} книг автора {author_name}, опубликованных с 2000 года:")
    for i, book in enumerate(found_books, start=1):
        print(f"{i}. {book['Book-Title']} - {book['Year-Of-Publication']}")
else:
    print(f"Книги автора {author_name}, опубликованные с 2000 года, не найдены.")