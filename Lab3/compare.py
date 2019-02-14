import sys
import string


def count(file_name):
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    word_number = 0
    line_number = 0
    unique_words = set()
    with open(file_name, 'r') as text:
        for lines in text:
            lines = lines.lower()
            word = lines.translate(translator).split()
            unique_words.update(word)
            line_number += 1
            word_number += len(word)
    return word_number, unique_words


def print_format(file_name, number, unique):
    print(file_name + ':')
    print(' ', number, 'words')
    print('  unique:', len(unique))


try:
    f = open(sys.argv[1])
    f.close()
except FileNotFoundError:
    print(sys.argv[1], 'is not found')
except IOError:
    print(sys.argv[1], 'is not accessible')

try:
    f = open(sys.argv[2])
    f.close()
except FileNotFoundError:
    print(sys.argv[2], 'is not found')
except IOError:
    print(sys.argv[2], 'is not accessible')

if len(sys.argv) != 3:
    raise ValueError('Enter two files')
else:
    a_number, a_unique = count(sys.argv[1])
    b_number, b_unique = count(sys.argv[2])
    print_format(sys.argv[1], a_number, a_unique)
    print_format(sys.argv[2], b_number, b_unique)
    same_word = a_unique & b_unique
    print('Only', sys.argv[1] + ':', len(a_unique - b_unique))
    print('Only', sys.argv[2] + ':', len(b_unique - a_unique))
    print('Both files:', len(same_word))

