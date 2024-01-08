#File Objects

with open('test.txt','r') as rf: #read file
    with open('textcopy.txt','w') as wf:
        for line in rf:
            wf.write(line)
        