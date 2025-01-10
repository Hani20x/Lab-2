import csv
import random

def generate_reference(book):
    author = book['Book-Author']
    title = book['Book-Title']
    year = book['Year-Of-Publication']
    return f"{author}. {title} - {year}"

with open('books-en.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    
    filtered_books = []
    for row in reader:
        try:
            year = int(row['Year-Of-Publication'])
            if year >= 2000:
                filtered_books.append(row)
        except ValueError:
            continue

if len(filtered_books) < 20:
    print("Недостаточно записей для выборки.")
else:
    selected_books = random.sample(filtered_books, 20)

    references = [generate_reference(book) for book in selected_books]

    with open('bibliography.txt', mode='w', encoding='utf-8') as output_file:
        for i, reference in enumerate(references, start=1):
            output_file.write(f"{i}. {reference}\n")

    print("Библиографические ссылки сохранены в файл 'bibliography.txt'")