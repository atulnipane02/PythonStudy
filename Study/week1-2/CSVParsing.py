import csv
import datetime
x = (datetime.datetime.now()).year
outfile = open("Students_age.csv", 'w')
outfile_header = "First Name,Last Name,Birth Year, Age,Grade\n"
outfile.write(outfile_header)
with open("Student_Details.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)

    for row in reader:
        first_name = row[0]
        last_name = row[1]
        birth_year = row[2]
        grade = row[3]
        age = x - int(birth_year)
        line = "{},{},{},{},{}\n".format(
            first_name, last_name, birth_year, age, grade)
        outfile.write(line)
outfile.close()
