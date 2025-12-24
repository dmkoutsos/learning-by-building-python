# File stats tool
# TODO: explore directory and collect statistics


from pathlib import Path
import sys
if len(sys.argv) == 1:
	root = Path(".")
else:
	root = Path(sys.argv[1])
to_visit = [root]
file_count = 0
dirs_visited = 0
line_count = 0
while to_visit:
	current_dir = to_visit.pop()
	print(current_dir)
	for entry in current_dir.iterdir():
		if (entry.is_dir() and entry.name!=".git"):
			to_visit.append(entry)
			dirs_visited += 1
		elif entry.is_file():
			file_count += 1
			p = entry
			with p.open() as f:
				for line in f:
					line_count += 1
print(f"Total files (recursive, no .git): {file_count}")
print(f"Total directories visited (recursive, no .git): {dirs_visited}")
print(f"Total lines (recursive, no .git): {line_count}")
