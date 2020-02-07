import csv
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

f = csv.writer(open('decadesFAST_'+dt+'.csv', 'w'))
f.writerow(['dc.title']+['dc.identifier.other']+['uri']+['link']+['decade']+['dc.subject'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        dc_title = row['dc.title']
        dc_id = row['dc.identifier.other']
        uri = row['uri']
        link = row['link']
        decade = row['decade'].strip()
        if len(decade) == 4 or len(decade) == 5:
            print(decade)
            if decade[0:3] == '200':
                n_decade = 'Two thousands (Decade)'
                print(n_decade)
                f.writerow([dc_title]+[dc_id]+[uri]+[link]+[decade]+[n_decade])
            else:
                century = decade[0:2]
                if century == '18':
                    century = 'Eighteen'
                elif century == '19':
                    century = 'Nineteen'
                tens = decade[2]
                if tens == '0':
                    tens = 'hundreds (Decade)'
                elif tens == '1':
                    tens = 'tens'
                elif tens == '2':
                    tens = 'twenties'
                elif tens == '3':
                    tens = 'thirties'
                elif tens == '4':
                    tens = 'forties'
                elif tens == '5':
                    tens = 'fifties'
                elif tens == '6':
                    tens = 'sixties'
                elif tens == '7':
                    tens = 'seventies'
                elif tens == '8':
                    tens = 'eighties'
                elif tens == '9':
                    tens = 'nineties'
                n_decade = century+' '+tens
                print(n_decade)
                f.writerow([dc_title]+[dc_id]+[uri]+[link]+[decade]+[n_decade])
        else:
            f.writerow([dc_title]+[dc_id]+[uri]+[link]+[decade]+['not converted'])
