import csv

dict = {}

with open('isocodes.csv') as metadata:
    reader = csv.DictReader(metadata)
    for row in reader:
        code = row['code']
        language = row['language']
        if language in dict:
            print(language)
            code1 = dict[language]
            code2 = code
            c1 = len(code1)
            c2 = len(code2)
            if c2 < c1:
                dict[language] = code2
        else:
            dict[language] = code

print(dict)
with open('newiso.csv', 'w') as output_file:
    writer = csv.writer(output_file)
    for k,v in dict.items():
        writer.writerow([k]+[v])
