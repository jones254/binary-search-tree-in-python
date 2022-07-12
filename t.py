grade={}
records=[]
while True:
    data= input("Enter a student's assessment marks(separated by comma):  ").split(',')
    if str.lower(data[0])=='n':
        break
    else:
        first= (data[0])
        middle= (data[1])         
        last= (data[2])
        print(first)
        print(middle)


    
    records.append(data)
for x in records: 
      
    print(x)
number_of_students=len(records) 
print(f'the number of students:  {number_of_students}')     
   