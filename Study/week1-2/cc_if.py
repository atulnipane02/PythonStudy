""" 
    Students  |  Grades  |  Letters
   ------------|----------|----------
     George    |  46      |  F
     Michell   |  80      |  B
     Josh      |  12      |  F
     Chloe     |  68      |  D
     Stanley   |  99      |  A
     Annie     |  100     |  A+
"""
gradeToTest = 100
if gradeToTest > 100:
    print("Grades cannot be greater than 100")
elif gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90 and gradeToTest < 100:
    print("A")
elif gradeToTest >= 80 and gradeToTest < 90:
    print("B")
elif gradeToTest >= 70 and gradeToTest < 80:
    print("C")
elif gradeToTest >= 50 and gradeToTest < 70:
    print("D")
elif gradeToTest >= 0 and gradeToTest < 50:
    print("F")
else:
    print("Grades cannot be less than 0")
