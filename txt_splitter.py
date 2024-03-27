#get full file name then split name and extension

from glob import glob
file_name = glob('*.txt')[0]
f_name = file_name.split('.')
#print(f_name[0])

#open original file and grab the first line

f0 = open(file_name, "r")
first_line = f0.readline()
f0.close()

#count the lines in original file

f0 = open(file_name, "r")
count_total = 0
for x in f0:
    count_total += 1
#print(count_total)
f0.close()

#divide total lines with 5 to get each part number of lines

lines_of_part = (count_total - 1) // 5
#print(lines_of_part)

#create new files and then write first lines except in the first file

f1 = open(f_name[0]+"1."+f_name[1], "a")
f2 = open(f_name[0]+"2."+f_name[1], "a")
f2.write(first_line)
f3 = open(f_name[0]+"3."+f_name[1], "a")
f3.write(first_line)
f4 = open(f_name[0]+"4."+f_name[1], "a")
f4.write(first_line)
f5 = open(f_name[0]+"5."+f_name[1], "a")
f5.write(first_line)

#create and write the lines in the new files

count = 0
f0 = open(file_name, "r")
for line in f0:
    if count >= 0 and count <= lines_of_part:
        f1.write(line)
        count += 1
        #print(count)
        #print(line)
    elif count > lines_of_part and count <= (lines_of_part*2):
        f2.write(line)
        count += 1
        #print(count)
        #print(line)
    elif count > (lines_of_part*2) and count <= (lines_of_part*3): 
        f3.write(line)
        count += 1
        #print(count)
        #print(line)
    elif count > (lines_of_part*3) and count <= (lines_of_part*4):
        f4.write(line)
        count += 1
        #print(count)
        #print(line)
    elif count > (lines_of_part*4):
        f5.write(line)
        count += 1
        #print(count)
        #print(line)

#close files
        
f0.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

#print(count)