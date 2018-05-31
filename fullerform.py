import csv
import re
filename = raw_input('Enter filename (including \'.csv\'): ')

f=csv.writer(open('namesChecked.csv', 'wb'))
f.writerow(['name']+['primaryName']+['fullerFormOfName'])

with open(filename) as name_file:
    names = csv.DictReader(name_file)
    for name in names:
        if '(' in name:
            primaryName = name[:'(']
            fullerFormOfName = name[('('+1):')']
            f.writerow ([name]+[primaryName]+[fullerFormOfName])
            print name, primaryName, fullerFormOfName
        else :
            f.writerow([name] + [])
