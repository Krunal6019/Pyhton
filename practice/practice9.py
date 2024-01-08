#os module
import os
# print(dir(os)) #display all the directory

print(os.getcwd()) #current working directory

os.chdir(r"C:\Users\kruna\OneDrive\Desktop\krunal") #here r represent the raw string
print(os.getcwd()) #current working directory

print(os.listdir()) #list of the directories from given path

# To make directory
# os.mkdir('OS-Demo-1/Sub-Dir-1') 
# os.makedirs('OS-Demo-2/Sub-Dir-1')

#To remove directory
# os.rmdir('OS-Demo-1/Sub-Dir-1')
# os.removedirs('OS-Demo-1/Sub-Dir-1')

#To rename
# os.rename("demo.txt.txt","test.txt")

#To shows information of that file
print(os.stat('test.txt'))
from datetime import datetime
mod_time=os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

#walk function to show all the directories in tree form
# for dirpath,dirnames,filenames in os.walk(os.getcwd()):
#     print('Current Path:',dirpath)
#     print('Directories:',dirnames)
#     print('Files:',filenames)
#     print()

#environment variable
# print(os.environ.get("HOME"))

#path method
print(os.getenv('HOME', "not found"))
# file_path = os.path.join(os.environ.get("HOME"),"test.txt")
# print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
# print(dir(os.path))











