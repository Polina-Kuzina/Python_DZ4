def search_view_number(kont):
    f = open(r'Telefon_book\Prog\telephon_book.txt', 'r')
    Line_new = f.readlines()
    # print(Line_new)
    f.close()
    for line in Line_new: 
        if line.find(kont) == 0:
            print(line)

# search_view_number('Oleg')