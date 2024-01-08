#raise function
try:
    f=open("test.txt")
   
    if f.name == 'test.txt':
       raise Exception
   
except FileNotFoundError:
    print("FileNotFoundError")

except Exception as e:
    print('Error')
else:
   x=f.read()
   print(x)
   f.close()
finally:
    print("Finally")
    pass    

