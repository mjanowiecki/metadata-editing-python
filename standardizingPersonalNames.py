import csv
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='collectionHandle of the collection to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('namesStandardized.csv', 'w'))
f.writerow(['personalName']+['errorType'])

with open(filename) as name_file:
    names = csv.DictReader(name_file)
    for name in names:
        individual_name = name['Names'].strip()
        match = re.search(r',\S', individual_name) #searches for the pattern--> [,]non-whitespace character (Smith,Bob)
        match2 = re.search(r'\S\.\w', individual_name) #searches for the pattern--> nonwhitespace character[.]nonwhitespace character (Smith, B.B.)
        match3 = re.search(r'\s[A-Z][A-Z]$', individual_name) #searches for the pattern--> whitespace[CAPITALLETTER][CAPITALLETTER]endofstring (Smith, BB)
        match4 = re.search(r'fl\.', individual_name) #searches for the string--> fl.
        match5 = re.search(r'ca\.', individual_name) #searches for the string--> ca.
        match6 = re.search(r'cent\.', individual_name) #searches for the string--> cent.
        match7 = re.search(r'b\.', individual_name) #searches for the string--> b.
        match8 = re.search(r'd\.', individual_name) #searches for the string--> d.
        if match2:
            f.writerow([individual_name] + ['Add space after period'])
            #print(individual_name, ': Add space after period')
        elif individual_name[-1] == '.' and individual_name[-3] != ' ': #searches for an instance where--> there is period at the end of the name, and the name doesn't end in an initial (Smith, Bob.)
            f.writerow([individual_name] + ['Remove period'])
            #print(individual_name, ': Remove period')
        elif individual_name[-1] != '.' and individual_name[-2].isspace(): ##searches for an instance where--> there ISN'T period at the end of the name when the name ends in an initial (Smith, B)
            f.writerow([individual_name] + ['Add period after initial'])
            #print(individual_name, ': Add period after initial')
        elif match:
            f.writerow([individual_name] + ['Add space after comma'])
            #print(individual_name, ': Add space after comma')
        elif match3:
            f.writerow([individual_name] + ['Might be initials'])
            #print(individual_name, ': Might be initials')
        elif match4 or match5 or match6 or match7 or match8:
            f.writerow([individual_name] + ['Not updated to RDA standards'])
            #print(individual_name, ': Not updated to RDA standards')
        else :
            f.writerow([individual_name] + [])
