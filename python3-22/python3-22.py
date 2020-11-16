#Navigating folders

#Special note - there are always multiple ways to do something
#Use what works for you!

#Import a module
import os
d = os.getcwd()
print(f'Current: {d}') #Current directory

#Change folders
os.chdir('..')
print(f'Current: {os.getcwd()}') #Current directory
os.chdir(d)
print(f'Current: {os.getcwd()}') #Current directory

#ListDir
for f in os.listdir(): 
    print(f)
    print(f'Path: {os.path.abspath(f)}')
    if os.path.isdir(f): print(f'Dir: {f}')
    if os.path.isfile(f): print(f'File: {f}')
    if os.path.islink(f): print(f'Link: {f}')

#ScanDir - Python 3.5
#https://docs.python.org/3/library/os.html#os.scandir
for e in os.scandir():
    print(e)
    print(f'Name: {e.name}')
    print(f'Path: {e.path}')
    if e.is_dir(): print(f'Dir: {e.name}')
    if e.is_file(): print(f'File: {e.name}')
    if e.is_symlink(): print(f'Link: {e.name}')

#Glob - multiple ways 
#Use whats right for you
#https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory

#Recursive scan

import glob
os.chdir('..')
dir = os.getcwd()

for filename in glob.glob(pathname= dir + '**/**', recursive=True):
    print(f'glob: {filename}')

for currentpath, folders, files in os.walk('.'):
    for file in files:
        print(f'walk: {os.path.join(currentpath, file)}')
