import argparse
import chardet
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')


def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc


my_encoding = find_encoding(filename)

print(my_encoding)
df = pd.read_csv(filename, encoding=my_encoding)

df['dc.title'] = df['dc.title'].str.upper()

duplicatedRows = df[df.duplicated(['dc.title'], keep=False)]
print(duplicatedRows)
if duplicatedRows.empty is False:
    duplicatedRows.to_csv(path_or_buf='duplicatedCSV.csv', index=False)
