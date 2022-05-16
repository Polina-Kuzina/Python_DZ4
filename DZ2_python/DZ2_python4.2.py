# Распаковка сжатого файла

file2 = 'DZ2_number4.2.txt'
with open(file2, 'r') as Str_rle:
    List = [i for i in Str_rle.read()]
Str = ''
i = 0
while i < len(List):
    Str += (f'{List[i+1]*int(List[i])}')
    i += 2
print(Str)
