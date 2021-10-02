import csv
with open('kyphosis.csv','r') as csv_files:
    #cs = csv.reader(csv_files)
    csv_reader=csv.DictReader(csv_files)#with Dictionary Reader we don't have to change much anything\
    #But with DictWriter we have add fieldnames
            #next(cs)#it can loop over first value while we do printing
    with open('new.csv','w') as csw:
        #we can add field names while working with DictWriter for more clarity and also we have to pass
        # them in DictWriter
        fieldnames=['Kyphosis','Age','Number','Start']
        csv_writer=csv.DictWriter(csw,fieldnames=fieldnames,delimiter='\t')#if we don't use delimiter then
        # it is going # to print out the content without splitting
        csv_writer.writeheader()
        for line in csv_reader:
          #csv_writer.writerow(line)
            #print(line['Age'])
            csv_writer.writerow(line)