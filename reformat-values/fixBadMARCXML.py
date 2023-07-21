from lxml import etree
from bs4 import BeautifulSoup

# Name of fixed XML file here.
filename = 'fixed.xml'

NSMAP = {'marc': 'http://www.loc.gov/MARC21/slim'}

# Load the bad MARC XML file into an iterative parser.
context = etree.iterparse('bad.xml', events=('start', 'end'), recover=True)

# Get the root element.
event, root = next(context)
assert event == "start"
last_record = 0
bad_count = 0


# Put the control numbers from the 001 field of the problematic records in this list.
bad_records = ['991008238639707861', '991023794499707861']

# Loop through XML record
with open(filename, 'wb') as f:
    # Add header.
    header = '<?xml version="1.0" encoding="UTF-8" ?>'.encode(encoding='utf-8')
    # Add collection entity wrapper.
    collection = '<marc:collection xmlns:marc="http://www.loc.gov/MARC21/slim" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd">'.encode(encoding='utf-8')
    end_collection = '</marc:collection>'.encode(encoding='utf-8')
    f.write(header)
    f.write(collection)
    try:
        for event, elem in context:
            # Add one bib record at a time to new XML file, unless record in bad_record list.
            if event == 'end' and elem.tag == '{http://www.loc.gov/MARC21/slim}record':
                last_record = last_record + 1
                if last_record % 1000 == 0:
                    print(last_record)
                string_element = etree.tostring(elem, encoding='utf-8', xml_declaration=None)
                soup = BeautifulSoup(string_element, 'lxml')
                field_001 = soup.find(tag="001")
                control_num = field_001.contents[0]
                if control_num in bad_records:
                    print('EVIL')
                    pass
                else:
                    f.write(string_element)
    except etree.ParseError:
        print(last_record)
        errors = context.error_log
        for error in errors:
            print(error.message)
            print(error.line)
        bad_count = bad_count + 1
        print("not added: "+str(bad_count))
        pass
    f.write(end_collection)
    f.close()