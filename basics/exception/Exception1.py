import sys

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
        print(f"TypeError test. Conversion failed!")
        x = -1
    return x


def convert_simple(s):
    """Convert a string to an integer simplified"""
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}",
              file=sys.stderr)
    return -1


if __name__ == '__main__':
    print('Testing exception: ')
    print(convert('one three three seven'.split()))
    print(convert('one three three seven ten'.split()))
    print(convert(512))
    print(convert_simple('one three three seven'.split()))
    print(convert_simple('one three three seven ten'.split()))
    print(convert_simple(512))
