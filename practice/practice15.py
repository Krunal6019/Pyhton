#csv file
#works on tuples,list
import csv

with open('test.txt','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    # next(csv_reader) removed first line
    # for line in csv_file:
    #     print(line)
    #     print(line[2])

    with open('tnew_names.csv','w') as new_file:
            csv_writer=csv.writer(new_file,delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)