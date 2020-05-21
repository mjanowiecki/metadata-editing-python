import argparse
import chardet
import pandas as pd
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')
columnToCheck = ''


def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc


my_encoding = find_encoding(filename)
print(my_encoding)

df = pd.read_csv(filename, encoding=my_encoding)
df[columnToCheck] = df[columnToCheck].str.upper()

dupRows = df[df.duplicated([columnToCheck], keep=False)]

print(dupRows)
if dupRows.empty is False:
    dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
    dupRows.to_csv(path_or_buf='duplicatedValues_'+dt+'.csv', index=False)
