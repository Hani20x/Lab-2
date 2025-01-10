import csv

with open('books-en.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    
    next(reader)
    
    count = 0
    
    for row in reader:
        title = row[1]
        
       
        if len(title) > 30:
            count += 1


print(f"Количество записей с длиной названия больше 30 символов: {count}")