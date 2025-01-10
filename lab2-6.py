import csv

books = []

with open('books-en.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        book_title = row['Book-Title']
        downloads = int(row['Downloads'])
        books.append({'title': book_title, 'downloads': downloads})

sorted_books = sorted(books, key=lambda x: x['downloads'], reverse=True)

print("20 самых популярных книг:")
for i, book in enumerate(sorted_books[:20], 1):
    print(f"{i}. {book['title']} - {book['downloads']} скачиваний")