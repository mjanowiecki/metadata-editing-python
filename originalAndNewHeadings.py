
import csv
import re

def splitSubjects(delimiter):
    subject_elements = many_subjects.split(delimiter)
    subjects_elements_edited = []
    for each_element in subject_elements:
        each_element = each_element.strip()
        subjects_elements_edited.append(each_element)
    subjectDict = {}
    subjectDict[many_subjects] = subjects_elements_edited
    for k,v in subjectDict.items():
        f.writerow([k] + [v])

file_name = 'subjectsToBeSplit.csv'

f=csv.writer(open('originalAndSplitSubjects.csv', 'wb'))
f.writerow(['originalSubject'] + ['listOfSubject'])

with open(file_name) as subject_file:
    subjects = csv.DictReader(subject_file)
    for row in subjects:
        many_subjects = row['value'].strip()
        multiple_subjects = row['multipleTerms'].strip()
        bad_comma = row['Non-delimiterUseOfCharacter'].strip()
        staff = row['staff']
        possible_delimiter = row['possibleDelimiter'].strip()
        comments = row['comments']
        match1 = re.search(r'^,$', possible_delimiter)
        match2 = re.search(r';$', possible_delimiter)
        if multiple_subjects == 'y' and bad_comma == 'n' and match1:
            splitSubjects(',')
        elif multiple_subjects == 'y' and match2:
            splitSubjects(';')
