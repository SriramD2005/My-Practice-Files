section = ''
books = {}
borrowers = {}
result = []

BOOKS = "Books"
BORROWERS = "Borrowers"
CHECKOUTS = "Checkouts"
EOI = "EndOfInput"

while True:
    line = input().strip()
    if line == EOI:
        break
    if line in (BOOKS, BORROWERS, CHECKOUTS):
        section = line
        continue

    if section == BOOKS:
        book_id, book_title = line.split('~')
        books[book_id] = book_title
    elif section == BORROWERS:
        user_id, full_name = line.split('~')
        borrowers[user_id] = full_name
    elif section == CHECKOUTS:
        user_id, book_id, due_date = line.split('~')
        result.append((due_date, borrowers[user_id], book_id, books[book_id]))
        # result.append(f'{due_date}~{borrowers[user_id]}~{book_id}~{books[book_id]}')

sorted_result = sorted(result, key=lambda x: (x[0], x[2]))
print('\n'.join(map(lambda x: '~'.join(x), list(sorted_result))))