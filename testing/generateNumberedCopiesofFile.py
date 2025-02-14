"""
Generates numbered copies of a file for testing purposes.
"""

import shutil

count = 150
while count < 300:
    count += 1
    location = 'C:/Users/file_location_here'
    filename = 'file_example.jpg'
    shutil.copy2(location+filename, location+str(count).zfill(2)+filename)
