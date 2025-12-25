# File stats tool
# TODO: explore directory and collect statistics


from pathlib import Path
import sys

files_only = False

if len(sys.argv) == 1:
	root = Path(".")
elif len(sys.argv) == 2:
	if sys.argv[1] == "--files":
		root = Path(".")
		files_only = True
	else:
		root = Path(sys.argv[1])
else: 
	print("Unsupported feature for now")


to_visit = [root]
file_count = 0
dirs_visited = 0
line_count = 0
skipped_files = 0


while to_visit:
	current_dir = to_visit.pop()
	for entry in current_dir.iterdir():
		if (entry.is_dir() and entry.name!=".git"):
			to_visit.append(entry)
			dirs_visited += 1
		elif entry.is_file():
			file_count += 1
			try:
				with entry.open() as f:
					for line in f:
						line_count += 1
			except: skipped_file += 1


if files_only == True:
	print(f"Total files (recursive, no .git): {file_count}")
	print(f"Total files skipped: {skipped_files}")
else:
	print(f"Total files (recursive, no .git): {file_count}")
	print(f"Total directories visited (recursive, no .git): {dirs_visited}")
	print(f"Total lines (recursive, no .git): {line_count}")
	print(f"Total files skipped: {skipped_files}")

