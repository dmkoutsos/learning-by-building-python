# File stats tool
# TODO: explore directory and collect statistics


from pathlib import Path 
for entry in Path("/home/dimitrios/Documents/learning-by-building-python/").iterdir(): 
    if entry.is_dir():
        print(entry.name)
