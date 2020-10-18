from pprint import pprint as pp

sunday = [12, 14, 15, 17, 21, 22, 20]
monday = [13, 14, 14, 16, 21, 23, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]


def print_zip():
    for item in zip(sunday, monday):
        print(item)
    print("Adding Tuesday:")
    for item in zip(sunday, monday, tuesday):
        print(item)

    daily = [sunday, monday, tuesday]
    print("With pprint:")
    pp(daily)
    print("Passing to the list constructor(third list is cut). Columns are converted into rows:")
    transposed = list(zip(*daily))
    pp(transposed)

if __name__ == '__main__':
    print_zip()