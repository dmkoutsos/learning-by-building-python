# File stats tool
# TODO: explore directory and collect statistics


from pathlib import Path
found = 0 
for entry in Path("/home/dimitrios/Documents/learning-by-building-python/").iterdir(): 
	if entry.is_dir():
		print(entry.name)
		found +=1
print (found)
