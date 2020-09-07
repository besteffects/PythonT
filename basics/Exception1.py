DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def convert(s):
    """Convert a string to an integer"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion succeeded! x={x}")
    except KeyError:
        x = -1
        print("Conversion failed!")
    except TypeError:
        print("TypeError test. Conversion failed!")
        x = -1
    return x


if __name__ == '__main__':
    print('Testing exceptions: ')
    print(convert('one three three seven'.split()))
    print(convert('one three three seven ten'.split()))
    print(convert(512))
