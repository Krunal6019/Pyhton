#How to Write and Match Regular Expressions (Regex) part-3 
import re
emails='''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
meet47mandani@gmail.com 
meet$&mandani@gmail.com '''# not matched whole email id


pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z0-9_.-]+')



matches=pattern.finditer(emails)

for match in matches:
    print(match)


