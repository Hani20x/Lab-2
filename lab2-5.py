import csv

unique_publishers = set()

with open('books-en.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        publisher = row['Publisher']
        unique_publishers.add(publisher)

for publisher in sorted(unique_publishers):
    print(publisher)