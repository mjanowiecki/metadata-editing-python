from pymarc import MARCReader
import csv
import argparse
import re
import os
from datetime import datetime
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()
if args.file:
    filename = args.file
else:
    filename = input('Enter filename (including \'.mrc\'): ')

fileDir = os.path.dirname(__file__)

gacs_dict = {}
types_dict = {}
datetypes_dict = {}
lang_dict = {}
cat_dict = {}


def createDict(csvname, column1, column2, dictname):
    with open(csvname) as codes:
        codes = csv.DictReader(codes)
        for row in codes:
            code = row[column1]
            name = row[column2]
            dictname[code] = name


#  Import gacs codes used in 043 fields.
createDict(os.path.join(fileDir, 'dictionaries/gacs_code.csv'), 'code', 'location', gacs_dict)
#  Import type codes used in 006.
createDict(os.path.join(fileDir, 'dictionaries/marc_006types.csv'), 'Type', 'Name', types_dict)
#  Import date type codes used in 008.
createDict(os.path.join(fileDir, 'dictionaries/marc_datetypes.csv'), 'Type', 'Name', datetypes_dict)
# Import language codes used in Lang.
createDict(os.path.join(fileDir, 'dictionaries/marc_lang.csv'), 'Code', 'Name', lang_dict)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
relatorTerms = ['director', 'producer', 'writer', 'narrator', 'speaker', 'announcer']


#  Creates k,v pair in dict where key = field_name, value = values of MARC tags in record.
def field_finder(record, field_name, tags):
    field_list = []
    field = record.get_fields(*tags)
    for my_field in field:
        my_field = my_field.format_field()
        field_list.append(my_field)
    if field_list:
        field_list = sorted(field_list)
        field_list = '|'.join(str(e) for e in field_list)
        mrc_fields[field_name] = field_list
    else:
        mrc_fields[field_name] = ''


# Creates k,v pair in dict where key = field_name, value = values of specific subfield in MARC tag in record.
def subfield_finder(record, field_name, subfields, tags):
    field_list = []
    field = record.get_fields(*tags)
    for my_field in field:
        my_subfield = my_field.get_subfields(*subfields)
        for field in my_subfield:
            field_list.append(field)
    if field_list:
        field_list = sorted(field_list)
        field_list = '|'.join(str(e) for e in field_list)
        mrc_fields[field_name] = field_list
    else:
        mrc_fields[field_name] = ''


# Converts code from MARC record into name from imported dictionaries.
def convert_to_name(keyname, dictname):
    for k, v in mrc_fields.items():
        if k == keyname:
            if isinstance(v, list):
                for count, item in enumerate(v):
                    for key, value in dictname.items():
                        if item == key:
                            v[count] = value
                mrc_fields[k] = v
            else:
                for key, value in dictname.items():
                    if v == key:
                        mrc_fields[k] = value


all_fields = []
record_count = 0
with open(filename, 'rb') as fh:
    marc_recs = MARCReader(fh, to_unicode=True)
    for record in marc_recs:
        mrc_fields = {}
        leader = record.leader
        #  Finds fields/subfield values in record.
        subfield_finder(record, 'bib', subfields=['a'], tags=['910'])
        subfield_finder(record, 'oclc', subfields=['a'], tags=['035'])
        field_finder(record, 'people',  tags=['700'])
        field_finder(record, 'corporate',  tags=['710'])
        field_finder(record, 'program', tags=['730'])
        subfield_finder(record, 'publisher', subfields=['b'], tags=['260', '264'])
        subfield_finder(record, 'length', subfields=['a'], tags=['300'])
        subfield_finder(record, 'color', subfields=['b'], tags=['300'])
        field_finder(record, 'subjects', tags=['600', '610', '650', '651'])
        field_finder(record, 'descs', tags=['500', '520'])
        field_finder(record, 'video_1', tags=['508'])
        field_finder(record, 'video_2', tags=['511'])
        field_finder(record, 'broadcast', tags=['518'])
        field_finder(record, '008', tags=['008'])
        mrc_fields['title'] = record.title()
        subfield_finder(record, 'alt_title', subfields=['a', 'b'], tags=['246'])
        subfield_finder(record, 'cdates', subfields=['x', 'y'], tags=['034'])


        tiny_dict = {}
        # Edit & convert values in dictionary.
        for k, v in mrc_fields.items():
            # Find Lang codes, DtSt and Dates from field 008.
            if k == '008':
                if v:
                    datetype = v[6]
                    date1 = v[7:11].strip()
                    date2 = v[11:15].strip()
                    lang = v[35:38]
                else:
                    datetype = ''
                    date1 = ''
                    date2 = ''
                    lang = ''
            # Finds only oclc number, deleting prefixes.
            elif k == 'oclc' and v != '':
                oclc_list = []
                v = v.split('|')
                for item in v:
                    item = str(item)
                    oclc_num = re.search(r'([0-9]+)', item)
                    if oclc_num:
                        oclc_num = oclc_num.group(1)
                        if oclc_num not in oclc_list:
                            if oclc_num != mrc_fields['bib'][0]:
                                oclc_list.append(oclc_num)
                v = '|'.join(str(e) for e in oclc_list)
                mrc_fields[k] = v
            elif k == 'broadcast':
                for count, m in enumerate(months, start=1):
                    if m in v:
                        month = str(count).zfill(2)
                year = re.search(r'\d{4}', v)
                date = re.search(r'\d{1,2},', v)
                if year and date and month:
                    year = year.group()
                    date = date.group()
                    date = date.replace(',', '').zfill(2)
                    creation_date = year+'-'+month+'-'+date
            elif k == 'length':
                time = re.findall(r'\d{2}', v)
                minutes = time[0]
                try:
                    seconds = time[1]
                    if seconds:
                        duration = '00:'+minutes+':'+seconds
                except IndexError:
                    sec = re.search(r'\s\d\s', v)
                    if sec:
                        seconds = sec.group()
                        seconds = seconds.strip().zfill(2)
                        duration = '00:'+minutes+':'+seconds
                        print(duration)
                    else:
                        duration = '00:'+minutes+':00'
            elif k == 'color':
                if 'b&w' in v:
                    mrc_fields['color'] = 'Black and white'
                else:
                    pass
            elif k == 'corporate':
                if '.' in v:
                    v = v.replace('.|', '|')
                    v = v.replace(r'.$', '')
                    mrc_fields[k] = v
            elif k == 'video_1':
                values = v.split(';')
                for x in relatorTerms:
                    for value in values:
                        if x in value.lower():
                            value = value.replace(x+'s', '')
                            value = value.replace(x, '')
                            value = value.replace('executive', '')
                            value = value.strip()
                            if value[-1] == ',':
                                value = value[:-1]
                            value_list = value.split(',')
                            data = tiny_dict.get(x)
                            if data:
                                for item in value_list:
                                    item = item.replace(',', '').strip()
                                    if item not in relatorTerms:
                                        if item:
                                            data.append(item)
                                tiny_dict[x] = data
                            else:
                                new_value = []
                                for item in value_list:
                                    item = item.replace(',', '').strip()
                                    if item not in relatorTerms:
                                        if item:
                                            new_value.append(item)
                                tiny_dict[x] = new_value
                print(tiny_dict)
            elif k == 'video_2':
                new_list = []
                terms = [', presenters.', ', presenter.']
                for x in terms:
                    if x in v:
                        value = v.replace(x, '')
                        value = value.strip()
                        value = value.split(',')
                        for item in value:
                            item = item.strip()
                            new_list.append(item)
                        tiny_dict['presenter'] = new_list



        del mrc_fields['008']
        del mrc_fields['length']
        mrc_fields['duration'] = duration
        mrc_fields['creation_date'] = creation_date
        mrc_fields['datetype'] = datetype
        convert_to_name('datetype', datetypes_dict)
        mrc_fields['date1'] = date1
        mrc_fields['date2'] = date2
        mrc_fields['lang'] = lang
        convert_to_name('lang', lang_dict)
        for k, v in tiny_dict.items():
            v = '|'.join(str(e) for e in v)
            mrc_fields[k] = v

        # Adds dict created by this MARC record to all_fields list.
        all_fields.append(mrc_fields)
        record_count = record_count + 1
        print(record_count)

df = pd.DataFrame.from_dict(all_fields)
print(df.head(15))
dt = datetime.now().strftime('%Y-%m-%d %H.%M.%S')
df.to_csv(path_or_buf='marcRecords_'+dt+'.csv', header='column_names', encoding='utf-8', sep=',', index=False)
