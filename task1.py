import math 
 
results = input("Enter a student's assessment marks(separated by comma):  ").split(',')
Lab_exercise, Report, Final_examination = ( float( assessment ) for assessment in results )

final_score = math.ceil( Lab_exercise * 0.2 + Report * 0.4 + Final_examination * 0.4 )

if final_score > 84:
        # when final_score is above 84, High Distinction is awarded
        score = 'HD'
        print (score)

elif final_score in range(75, 85):
        # when final_score is between 74 and 85, Distiction is awarded
        score = 'D'
        print(score) 

elif final_score in range(65, 75):
        # when final_mark is between 64 and 74,  Credit is awarded
        score = 'C'
        print(score) 

elif final_score in range(50, 65):
        # when final_mark is between 49 and 65,  Pass is awarded
        score = 'P' 
        print(score) 

elif final_score in range(45, 50) and ( float(marks) > 0 for marks in results ) and  ( sum(float(marks) < 50 for marks in results )<2):
    
        score = 'SE'
        print(score) 

        
elif   final_score < 45 and ( sum(float(marks) == 0 for marks in results ) > 1):  
        # when the final_mark is less than 45 and two or more Assessment is zero, Absent Fail is awarded.
        score = 'AF'
        print(score)   

else:
        score = 'F' 
        print(score)   



