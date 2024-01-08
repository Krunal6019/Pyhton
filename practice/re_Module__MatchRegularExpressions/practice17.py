#How to Write and Match Regular Expressions (Regex) part-2 : grouping
import re
urls='''
https://www.google.com
http://coreysm.com
https://youtube.com
http://www.nasa.gov
'''

pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls=pattern.sub(r'\2\3',urls)
print(subbed_urls)

matches=pattern.finditer(urls)

for match in matches:
    print(match.group(0))
print("\n")

matches=pattern.finditer(urls)
for match in matches:
    print(match.group(1))
print("\n")

matches=pattern.finditer(urls)    
for match in matches:
    print(match.group(2))
print("\n")
  
matches=pattern.finditer(urls)
for match in matches:
    print(match.group(3))