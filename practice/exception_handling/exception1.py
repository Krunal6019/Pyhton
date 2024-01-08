try:
    f=open("test.txt")
   # fghjk=ffghjkl
except FileNotFoundError:
    print("FileNotFoundError")

except Exception as e:
    print(e)
else:
   x=f.read()
   print(x)
   f.close()
finally:
    print("Finally")
    pass    

