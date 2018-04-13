import random
import sys
import argparse
import csv
import string
from faker import Faker
fake = Faker()
fake.seed(5423)

def integer_csv(rows, schema, delimiter):
    random.seed(42)
    generators = []
    char_set = (string.ascii_letters + string.digits +
                '"' + "'" + "#&* \t")

    for column in schema:
        if column == 'int':
            generators.append(lambda: random.randint(0, 1e9))
        elif column == 'str':
            generators.append(lambda: ''.join(
                random.choice(char_set) for _ in range(12)))
        elif column == 'float':
            generators.append(lambda: random.random())
        elif column == "name":
            generators.append(lambda: fake.name())

    writer = csv.writer(sys.stdout, delimiter=delimiter)
    for x in range(rows):
        writer.writerow([g() for g in generators])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a large CSV file.',
        epilog='''"Space is big. You just won't believe how vastly,
        hugely, mind-bogglingly big it is."''')
    parser.add_argument('rows', type=int,
                        help='number of rows to generate')
    parser.add_argument('--delimiter', type=str, default=',', required=False,
                        help='the CSV delimiter')
    parser.add_argument('schema', type=str, nargs='+',
                        choices=['int', 'str', 'float', "name"],
                        help='list of column types to generate')

    args = parser.parse_args()
    integer_csv(args.rows, args.schema, args.delimiter)