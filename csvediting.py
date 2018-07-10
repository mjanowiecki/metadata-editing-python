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

f=csv.writer(open('namesChecked.csv', 'wb'))
f.writerow(['individualName']+['errorType'])

with open(filename) as name_file:
    names = csv.DictReader(name_file)
    for name in names:
        individual_name = name['Names'].strip()
        match = re.search(r',\S', individual_name) #searches for the pattern:, non-whitespace character (Smith,Bob)
        match2 = re.search(r'\S\.\w', individual_name) #searches for the pattern:nonwhitespace character . nonwhitespace character (Smith, B.B.)
        match3 = re.search(r'\s[A-Z][A-Z]$', individual_name)#searches for the pattern:whitespace[CAPITALLETTER][CAPITALLETTER]endofstring (Smith, BB)
        match4 = re.search(r'fl\.', individual_name)
        match5 = re.search(r'ca\.', individual_name)
        match6 = re.search(r'cent\.', individual_name)
        match7 = re.search(r'b\.', individual_name)
        match8 = re.search(r'd\.', individual_name)
        if match2:
            f.writerow([individual_name] + ['Add space after period'])
            print individual_name, ': Add space after period'
        elif individual_name[-1] == '.' and individual_name[-3] != ' ': #if there is period at the end of the name, and the 3rd character from the end of the end isn't a space (Smith, Bob.)
            f.writerow([individual_name] + ['Remove period'])
            print individual_name, ': Remove period'
        elif individual_name[-1] != '.' and individual_name[-2].isspace(): #if there ISN'T period at the end of the name and the 2nd character is a space (Smith, B)
            f.writerow([individual_name] + ['Add period after initial'])
            print individual_name, ': Add period after initial'
        elif match:
            f.writerow([individual_name] + ['Add space after comma'])
            print individual_name, ': Add space after comma'
        elif match3:
            f.writerow([individual_name] + ['Might be initials'])
            print individual_name, ': Might be initials'
        elif match4 or match5 or match6 or match7 or match8:
            f.writerow([individual_name] + ['Not updated to RDA standards'])
            print individual_name, ': Not updated to RDA standards'
        else :
            f.writerow([individual_name] + [])
