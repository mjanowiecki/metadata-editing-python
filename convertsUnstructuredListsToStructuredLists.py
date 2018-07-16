
import csv
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='file_name to retreive. optional - if not provided, the script will ask for input')
args = parser.parse_args()

if args.file:
    file_name = args.file
else:
    file_name = raw_input('Enter file name as filename.csv: ')

def splitValues(delimiter):
    unstructured_values_split = unstructured_values.split(delimiter)
    unstructured_values_edited = []
    for each_value in unstructured_values_split:
        each_value = each_value.strip()
        unstructured_values_edited.append(each_value)
    valuesDict = {}
    valuesDict[unstructured_values] = unstructured_values_edited
    for k,v in valuesDict.items():
        f.writerow([k] + [v])


f=csv.writer(open('structuredAndUnstructuredLists.csv', 'wb'))
f.writerow(['unstructuredList'] + ['structuredList'])

with open(file_name) as unstructuredList_file:
    unstructuredList = csv.DictReader(unstructuredList_file)
    for row in unstructuredList:
        unstructured_values = row['value'].strip()
        multiple_values = row['multipleTerms'].strip()
        possible_delimiter = row['possibleDelimiter'].strip()
        match1 = re.search(r'^,$', possible_delimiter)
        match2 = re.search(r';$', possible_delimiter)
        if multiple_values == 'y' and match1:
            splitValues(',')
        elif multiple_values == 'y' and match2:
            splitValues(';')
