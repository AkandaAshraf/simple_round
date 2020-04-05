import re
import sys

if 4 >len(sys.argv):
    print('requires two arguments: (the last param is number of digits to keep for rounding)')
    print('python round.py input_file_path.txt output_file_path.txt 4')
    exit(1)

try:
    digits = int(sys.argv[3])
except ValueError:
    print('could not understand how many digits to round')
    exit(1)


def round_up(input_file, output_file, digits=4):
    f= open(input_file, 'r')
    content = f.readlines()
    f.close()
    new_content = []
    for c in content:
        words = re.split(r"(\d+\.\d+)", c)
        j=0
        for w in words:
            if re.match(r"\d+\.\d+", w) is not None:
                words[j] = str(round(float(w), digits))
            j = j +1
        new_content.append(words)
    f2= open(output_file, 'w')
    for words in new_content:
        for word in words:
            f2.write(word)
    f2.close()

round_up(input_file=sys.argv[1], output_file=sys.argv[2], digits=digits)
