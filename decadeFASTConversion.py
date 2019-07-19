import csv
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('decadesFAST.csv', 'w'))
f.writerow(['dc.title']+['dc.description.abstract']+['dc.identifier.other']+['uri']+['link']+['decade']+['dc.subject'])

with open(filename) as itemMetadataFile:
    itemMetadata = csv.DictReader(itemMetadataFile)
    for row in itemMetadata:
        dc_title = row['dc.title']
        dc_description = row['dc.description.abstract']
        dc_identifier = row['dc.identifier.other']
        uri = row['uri']
        link = row['link']
        decade = row['decade'].strip()
        if len(decade) == 4 or len(decade) == 5:
            print(decade)
            if decade[0:3] == '200':
                newdecade = 'Two thousands (Decade)'
                print(newdecade)
                f.writerow([dc_title]+[dc_description]+[dc_identifier]+[uri]+[link]+[decade]+[newdecade])
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
                newdecade = century+' '+tens
                print(newdecade)
                f.writerow([dc_title]+[dc_description]+[dc_identifier]+[uri]+[link]+[decade]+[newdecade])
        else:
            f.writerow([dc_title]+[dc_description]+[dc_identifier]+[uri]+[link]+[decade]+['not converted'])
