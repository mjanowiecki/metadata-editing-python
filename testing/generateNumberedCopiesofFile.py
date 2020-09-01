import shutil

count = 150
while count < 300:
    count = count + 1
    location = 'C:/Users/filelocationhere'
    filename = 'file_example.jpg'
    shutil.copy2(location+filename, location+str(count).zfill(2)+filename)
