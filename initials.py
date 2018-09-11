import csv
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = raw_input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('namesInitialsSearchResults.csv', 'wb'))
f.writerow(['names']+['errorType'])

with open(filename) as name_file:
    names = csv.DictReader(name_file)
    for name in names:
        individual_name = name['value'].strip()
        contains_initials = re.search(r'(\s|,|[A-Z]|([A-Z]\.))[A-Z](\s|$|\.|,)', individual_name)
        contains_middleinitial = re.search(r'((\w{2,},\s)|(\w{2,},))\w[a-z]+', individual_name)
        contains_parentheses = re.search(r'\(|\)', individual_name)
        if contains_middleinitial :
            f.writerow([individual_name] + [''])
        elif contains_parentheses:
            f.writerow([individual_name] + [''])
        elif contains_initials :
            f.writerow([individual_name] + ['might be initials'])
            print individual_name
        else:
            f.writerow([individual_name] + [''])
