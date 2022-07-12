import math
# imports math modules to provide some computation functionalities
def user(lab_exercise, report, final_examination):
    # a function to compute the final mark
    results=(lab_exercise, report, final_examination)
    final_mark=math.ceil(lab_exercise * 0.2 + report * 0.4 + final_examination * 0.4)
    # if functions to determine the grade of the student
    if final_mark >= 85:
        return 'HD'
    elif final_mark in range(75,85):
        return 'D'
    elif final_mark in range(65,75):
        return 'C'
    elif final_mark in range(50,65):
        return 'P'
    elif final_mark in range(45,50) and ((x>0 for x in results)) and  (sum (x<50 for x in results))<2:
        return 'SE'
    # an if condition to determine if the student qualifies for a suplimentary or just failed.    
    elif final_mark <=44 and (sum(x in range(0,45) for x in results))>=2:  
        return  'AF'
    else:
        return 'F'   

#promts user to input scores for the assessments             
lab_exercise, report, final_examination=(float(x)for x in input("Enter a student's assessment marks(separated by comma):  ").split(','))  
grade=user(lab_exercise, report, final_examination) 
print(grade)   