import os
import threading

results = []

print("--- Directory Scanner ---\n")
# User input
base = input("Enter the directory path: ").strip()
ext = input("Enter the file extension: ").strip()

# Adds dot (.) if user forgot it
if not ext.startswith("."):
    ext = "." + ext

# Validates the path
if not os.path.exists(base):
    print("Path does not exist")
    exit()

#Loops the directory and appends files matching the given ext
def scan(path, ext):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(ext.lower()):
                results.append(os.path.join(root, file))

# Gets subdirectories and return to main path if none found
subdirs = [os.path.join(base, d) for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))] or [base]

# Includes the base path itself so it is not missed
if base not in subdirs:
    subdirs.append(base)

# Launches a  thread in each subdirectory and waits for all to finish at once
threads = [threading.Thread(target=scan, args=(d, ext,)) for d in subdirs]
for t in threads: t.start()
for t in threads: t.join()

# Prints the results
print(f"\n{len(results)} file(s) found:")
for r in results: print(r)

# Saves the results
with open("results.txt", "w", encoding="utf-8") as f:
    f.write(f"Base: {base} | Extension: {ext}\n\n")
    f.write("\n".join(results))

print("\nSaved to scan_results.txt")