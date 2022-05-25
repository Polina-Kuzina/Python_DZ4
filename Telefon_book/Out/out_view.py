def look_phone_book():
    data = open(r'Telefon_book\Prog\telephon_book.txt', 'r')
    for line in data:
        print(line)
    data.close()
