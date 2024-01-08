#File Objects

# f=open('test.txt','r')

# print(f.name)
# f.close()

#use of contxt

with open('test.txt','r') as f:
    f_content=f.read()
    # f_contents=f.readlines()
    print(f_content)
    # print(f_contents)
    # print(f.tell)
    
with open('test2.txt','w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')