__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, shutil

def clean_cache():
    cache = r'C:\Users\HP\Winc\files\cache'
    if not os.path.exists(cache):
        return os.makedirs(cache)
    for filename in os.listdir(cache):
        file_path = os.path.join(cache, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
      
print (clean_cache())

import zipfile

def cache_zip(zip_file, dir1):
    dir1 = r'C:\Users\HP\Winc\files\cache'
    zip_file = 'data.zip'
    with zipfile.ZipFile(zip_file) as z:
        return z.extractall(dir1)
    
print (cache_zip('data.zip', r'C:\Users\HP\Winc\files\cache'))

import os

def cached_files():
    list_files = []
    with os.scandir('cache') as files:
        for file in files:
            if file.is_file():
                x = os.path.abspath(file)
                list_files.append(x)
                
    return list_files

def find_password(list_files):
    list_files = cached_files()
    for file in list_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'password' in line:
                    return line[line.find(' ')+1:-1]

print(find_password(r'C:\Users\HP\Winc\files\cache'))


