__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os 
from zipfile import ZipFile

def clean_cache():
    if os.path.exists("cache"):
        all_files = os.listdir("cache")
        for f in all_files:
            os.remove("cache" + "\\" + f)           
    else: 
        os.makedirs("cache") 

def cache_zip(zip_path, cache_dir_path):
    clean_cache()
    with ZipFile(zip_path) as zipObj:
        zipObj.extractall(cache_dir_path)


def cached_files():
    file_list = []
    all_files = os.listdir("cache")
    for f in all_files: 
        if os.path.isfile(os.path.abspath("cache" + "\\" + f)):
            file_list.append(os.path.abspath("cache" + "\\" + f))
        else: print("Found a nonfile!")
    return file_list

def find_password(file_list):
    for f in file_list: 
        with open(f) as txt:
            for line in txt:
                if "password" in line:
                    return line


