import math
# imports math modules
hd = [] # list of students with HD
d = [] # list of students with D
c = [] # list of students with C
p = [] # list of students with P
sp = [] # list of students with SP
af = [] # list of students with AF
f = [] # list of students with F
assessment_1 = []  # list of assessment_1 results
assessment_2 = [] # list of assessment_2 results
assessment_3 = []#  list of assessment_ results
records = [] # list of the final marks
run = True
# while loop to collect data then terminate
while run:
    data = list(input("Enter a student's assessment marks(separated by comma), type in letter n to finish:  ").split(','))
    if  str.lower(data[0]) == 'n':
         break # the loop terminates when user types in letter n

    else:
        lab_exercise = float(data[0])
        report = float(data[1])
        final_examination = float(data[2])
        results = (lab_exercise, report, final_examination)

    # final mark computation
    final_mark = math.ceil(float(lab_exercise) * 0.2 + float(report) * 0.4 + float(final_examination )* 0.4)
    if final_mark >= 85:
        hd.append('hd') # appends to list HD
    elif final_mark in range(75, 85):
        d.append('d')   # appends to list D
    elif final_mark in range(65, 75):
        c.append('c')   # appends to list C 
    elif final_mark in range(50, 65):
        p.append('p')    # appends to list P
    elif final_mark in range(45, 50) and (all ( x > 0 for x in results)) and  ( sum ( x < 50 for x in results ) ) < 2:
        mark = int ( input ( 'enter supplimentary exam mark: '))
        if mark >= 50:
            sp.append('sp')   # appends to list SP
        else:
            f.append('f')      # appends to list F
    elif final_mark <= 44 and (sum(x ==0  for x in results))>=2:  
        af.append('af')  
    else:
        f.append('f')           # appends to list  F

    assessment_3.append(final_examination)
    assessment_2.append(report)  
    assessment_1.append(lab_exercise)  
    records.append(final_mark)
    # the number of students in the record
number_of_students = len(results) 
print(f'the number of students:  {number_of_students}')

student_pass_rate = round((( hd.count ('hd') + d.count ('d') + c.count ('c') + p.count ('p') + sp.count ('sp') ) / number_of_students ) * 100 , 2  )     
print (f"student's pass rate:  {student_pass_rate} %")
# the students pass rate  adjusted percentage
student_pass_rate_adjusted = round ((( hd.count ('hd') + d.count ('d') + c.count ('c') + p.count ('p') + sp.count('sp') ) / (number_of_students - af.count('af' )))*100 ,2 )      
print(f"student's pass rate(adjusted):  {student_pass_rate} % ")

# The Average marks of assessment 1 for the class
lab_exercise_total=sum(assessment_1)
average_assessment_1=round(lab_exercise_total/number_of_students,2)
print (f"Average mark for assessment 1:  {average_assessment_1}")

# The Average marks of assessment 2 for the students
report_total=sum(assessment_2)
average_assessment_2=round(report_total/number_of_students,2)
print (f"Average mark for assessment 2:  {average_assessment_2}")

# The Average marks of assessment 3 for the class 
final_examination=sum(assessment_3)
average_assessment_3=round(final_examination/number_of_students,2)
print (f"Average mark for assessment 3:  {average_assessment_3}")

#The average final marks of the class
final_mark_total=sum(records)
average_final_mark= round(final_mark_total/number_of_students, 2)
print (f"Average final mark:  {average_final_mark}")

# The average grade point of the class
grade_point=(hd.count('hd')* 4) + (d.count('d')*3)+(c.count('c')*2)+(p.count('p')*1)+(sp.count('sp')*0.5)
average_grade_point= grade_point/number_of_students
print(f"Average grade point  {average_grade_point}")

# The number of students with High Distinction grade
number_of_students_with_HD=hd.count('hd')
print(f" Number of HDs:  {number_of_students_with_HD}")

# The number of students with Distinction grade
number_of_students_with_Ds=d.count('d')
print(f" Number of Ds:  {number_of_students_with_Ds}")

# The number of students with C grade
number_of_students_with_Cs=c.count('c')
print(f" Number of Cs:  {number_of_students_with_Cs}")

# The number of students with SP
number_of_students_with_SPs=sp.count('sp')
print(f" Number of SPs:  {number_of_students_with_SPs}")

# The number of students with F grade
number_of_students_with_Fs=f.count('f')
print(f" Number of Fs:  {number_of_students_with_Fs}")




