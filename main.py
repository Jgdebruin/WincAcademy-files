__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# 1
import os
import shutil
from zipfile import ZipFile

def clean_cache():
    path = os.getcwd()
    try:
        os.mkdir(path+"/cache")
    except OSError:
        shutil.rmtree(path+"/cache")
        os.mkdir(path+"/cache")
        #print("Cache flushed.")
    else:
        ...
        #print("Cache map created.")

clean_cache()

# 2
def cache_zip(zip_path,cache_path):
    with ZipFile(zip_path, "r") as zip:
        zip.extractall(cache_path)
        #print("Data.zip extracted.")

zip_path = os.path.join(os.getcwd(), "data.zip")        
cache_path = os.path.join(os.getcwd(), "cache")       
cache_zip(zip_path,cache_path)

# 3
def cached_files():
    cpath = os.path.join(os.getcwd(), "cache")  
    output = []
    for filename in os.listdir(cpath):
        if filename.endswith(".txt"):
            output.append(os.path.join(cpath, filename))
        else:
            continue
    return output

cached_files()

#print("test: "+str(cached_files()))

# 4
def find_password(cached_files):
    for fname in cached_files:
        f = open(fname, "r")            
        if "password" in f.read():
            f.seek(0)
            check = f.read()
            for item in check.split("\n"):
                if "password" in item:
                    passw = item.strip()
                    passw = passw.split(" ")
                    passw = passw[-1]
            break
        else:
            passw = "Password not found."
    f.close()
    return passw

#print(find_password(cached_files()))