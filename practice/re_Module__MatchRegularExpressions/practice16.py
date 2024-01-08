#How to Write and Match Regular Expressions (Regex)
import re

text_to_search= ''' 
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
800.555.1234
900.555.1234

Mr.Krunal
Mr skf
Mr damis
Mrs.Dombins
Mr.
'''

sentence= 'Start a sentence and then bring it to and end'

# pattern=re.compile(r'[67]1[-.]\d\d\d[-.]\d\d\d\d') 
pattern=re.compile(r'[[a-zA-Z]+@[a-zA-z]*\.com')                                                             
                                                            

matches=pattern.findall(text_to_search)

# for  match in matches :
#     print(match) 
    
# print(text_to_search[1:4])

with open('data.txt','r',encoding='utf-8') as f:
    contents=f.read()
    
    matches=pattern.finditer(contents)

for match in matches:
    print(match)