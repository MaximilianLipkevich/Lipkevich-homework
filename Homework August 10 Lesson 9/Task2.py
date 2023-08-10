import sys

for ind, spath in enumerate(sys.path):
    sys.path[ind] = spath.replace('August', 'October')

print(sys.path)
#Yes, I can change the path variable from within Python

from Task1_import_from import randomList

print(randomList(5))

#Yes, it does affect where Python looks for module files, because randomList would work if we imported if before changing the path