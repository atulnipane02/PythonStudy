"""import csv
outfile = open("Students_age.csv", 'w')
outfile_header = "First Name,Last Name,Birth Year, Age,Grade\n"

line = "{},{},{},{},{}\n".format(
    "Atul", "n", 1989, 32, "a")
outfile.write(line)

line = "{},{},{},{},{}\n".format(
    "Atul1", "n1", 19891, 321, "a1")
outfile.write(line)"""

import csv
f = open('Students_age.csv', 'w')

writer = csv.writer(f)
writer.writerow("Text1")
f.close()
f = open('Students_age.csv', 'w+')
writer.writerow("Text2")
writer.writerow("Text3")
