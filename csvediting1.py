import csv
import re
filename = raw_input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('namesChecked.csv', 'wb'))
f.writerow(['individualName']+['errorType'])

with open(filename) as name_file:
    names = csv.DictReader(name_file)
    for name in names:
        individual_name = name['names'].strip()
        match = re.search(r',\S', individual_name)
        match2 = re.search(r'\S\.\w', individual_name) #
        match3 = re.search(r'\s[A-Z][A-Z]$', individual_name)
        match4 = re.search(r'fl\.', individual_name)
        match5 = re.search(r'ca\.', individual_name)
        match6 = re.search(r'cent\.', individual_name)
        match7 = re.search(r'b\.', individual_name)
        match8 = re.search(r'd\.', individual_name)
        if match2:
            f.writerow([individual_name] + ['Add space after period'])
            print individual_name, ': Add space after period'
        elif individual_name[-1] == '.' and individual_name[-2] != 'r' and individual_name[-3] != ' ':
            f.writerow([individual_name] + ['Remove period'])
            print individual_name, ': Remove period'
        elif individual_name[-1] != '.' and individual_name[-2].isspace():
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
