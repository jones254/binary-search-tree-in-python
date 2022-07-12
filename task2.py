import math


Lab_exercise_list = []
Report_list = []
Final_examination_list = []
score_list = []
grade_point_value = {'HD':4.0, 'D':3.0, 'C':2.0, 'P':1.0, 'SP':0.5, 'F':0}


while True:

    Assessment_marks = list(input("Enter a student's assessment marks(separated by comma), type in letter n to finish:  ").split(','))
   
    if  str.upper(Assessment_marks[0]) == 'N':
        #terminates the loop
         break

    else:  # iniciates calculation   
        Lab_exercise, Report, Final_examination = ( float( assessment ) for assessment in Assessment_marks )
        
        Lab_exercise_list.append(Lab_exercise)
        Report_list.append(Report)
        Final_examination_list.append(Final_examination)
         
        final_score = math.ceil( Lab_exercise * 0.2 + Report * 0.4 + Final_examination * 0.4 )


        if final_score > 84:
            # when final_score is above 84, High Distinction is awarded
        
            score_list.append('HD') 

        elif final_score in range(75, 85):
            # when final_score is between 74 and 85, Distiction is awarded
    
            score_list.append('D') 

        elif final_score in range(65, 75):
            # when final_mark is between 64 and 74,  Credit is awarded
        
            score_list.append('C') 

        elif final_score in range(50, 65):
            # when final_mark is between 49 and 65,  Pass is awarded
         
                score_list.append('P') 

        elif final_score in range(45, 50) and ( float(marks) > 0 for marks in Assessment_marks ) and  ( sum(float(marks) < 50 for marks in Assessment_marks )<2):
    
            score = int ( input ( 'enter supplimentary exam mark: '))
            if score >= 50:
                # passed supplimentary exam
                score_list.append('SP') 

     
        elif   final_score < 45 and ( sum(float(marks) == 0 for marks in Assessment_marks ) > 1):  
            # when the final_mark is less than 45 and two or more Assessment is zero, Absent Fail is awarded.
        
            score_list.append('AF')   

        else:
         
            score_list.append('F')   



        students = len(score_list) 
        # get the number of students
        print(f'The number of students:  {students}')


        student_passed =  score_list.count ('HD') + score_list.count ('D') + score_list.count ('C') + score_list.count ('P') + score_list.count ('SP') 
        pass_rate = round((student_passed / students) * 100 , 2  )     
        print (f"student's pass rate:  {pass_rate} %")


        pass_rate_adjusted = round ( student_passed / (students - score_list.count( 'AF' )) * 100 , 2 )      
        print(f"student's pass rate(adjusted):  {pass_rate_adjusted} % ")


        average_Lab_exercise = round( sum( Lab_exercise_list ) /  students , 2 )
        print (f"Average mark for assessment 1:  {average_Lab_exercise}")


        average_Report = round( sum( Report_list ) /  students , 2 )
        print (f"Average mark for assessment 2:  {average_Report}")


        average_Final_examination = round( sum( Final_examination_list ) /  students , 2 )
        print (f"Average mark for assessment 3:  {average_Final_examination}")
 

        average_mark = round(math.ceil((average_Report + average_Lab_exercise + average_Final_examination) / 3 ) , 2)
        print (f"Average final mark:  {average_mark}")


        points =  ( score_list.count('HD') * grade_point_value['HD']) + ( score_list.count('D') * grade_point_value['D']) + ( score_list.count('C') * grade_point_value['C'])  + (score_list.count('P') * grade_point_value['P'] ) + (score_list.count('SP') * grade_point_value['SP']) +  (score_list.count('F') * grade_point_value['F'])
        grade_point = points / students
        print(f"Average grade point  {grade_point}")


        High_Distinction = score_list.count('HD')
        #  students who got High Distinction
        print(f" Number of HDs:  {High_Distinction}")


        Distinction = score_list.count('D')
        #  students who got Distinction 
        print(f" Number of Ds:  {Distinction}")


        Credit = score_list.count('C')
        # students who got Credit 
        print(f" Number of Cs:  {Credit}")


        Pass_ = score_list.count('P')
        # students who got a Pass 
        print(f" Number of Ps:  {Pass_}") 
 
        Supplementary_Assessment = score_list.count('SP')
        # students who did Supplementary Assessment
        print(f" Number of SPs:  {Supplementary_Assessment}")


        Fail = score_list.count('F')
        #  students who Failed 
        print(f" Number of Fs:  {Fail}")
        
             

          



     



    
