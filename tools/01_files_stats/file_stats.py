# File stats tool
# TODO: explore directory and collect statistics


from pathlib import Path
root = Path(".")
to_visit = [root]
while to_visit:
	current_dir = to_visit.pop()
	print(current_dir)
	for entry in current_dir.iterdir():
		if (entry.is_dir() and entry.name!=".git"):
			print (entry)
			to_visit.append(entry)
print("done")
