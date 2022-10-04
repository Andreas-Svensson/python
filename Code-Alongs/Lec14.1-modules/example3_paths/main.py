# import module1 # NOTE cannot import directly due to folder structure
# import module2

import sys, os

root_path = os.path.dirname(__file__) # finds directory of this file

path_folder1 = os.path.join(root_path, "folder1")
path_folder2 = os.path.join(root_path, "folder2")

os.system("cls||clear")

print("="*(len(path_folder1) + len("path_folder1") + 15))
print(f"| {path_folder1 = } |")
print(f"| {path_folder2 = } |")
print("="*(len(path_folder1) + len("path_folder1") + 15))

sys.path.append(path_folder1)
sys.path.append(path_folder2)

import module1
import module2
