def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


with open("somefile.txt", mode = 'rt', encoding='utf-8') as real_file:
    wpl = words_per_line(real_file)