def del_phone_number(kont):
    f = open(r'Telefon_book\Prog\telephon_book.txt', 'r')
    Line_new = f.readlines()
    # print(Line_new)
    f.close()
    f = open(r'Telefon_book\Prog\telephon_book.txt', 'w')
    for line in Line_new: 
        if line.find(kont) == -1:
            f.write(line)
    f.close()
    
# del_phone_number('anna')
