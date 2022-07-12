first_submission=input('Enter the first submission:  ').split()
second_submission=input('Enter the second submission:  ').split()

# new list of unique elements in first list
first_unique_list=[] 
# traverse for all elements

for x in first_submission:
	# check if exists in unique_list or not
	if x not in first_unique_list:
			first_unique_list.append(x)

 # new list of unique elements in second list           
second_unique_list=[]

# traverse for all elements
for x in second_submission:
	# check if exists in unique_list or not
	if x not in second_unique_list:
			second_unique_list.append(x)

# to check words appering in both lists while counting them            
not_unique=0
for x in first_unique_list:
    if x in second_unique_list:
        not_unique+=1
        
#count number of elements in first list which are not repeated
num_elem_in_first=len(first_unique_list) 
#count number of elements in second list which are not repeted
num_elem_in_second=len(second_unique_list)   
# the sum of all elements in both lists, which have not been duplicated in the same list  
total_elements=num_elem_in_first+num_elem_in_second
# the unique elements in the two lists
unique_elements=total_elements-not_unique
# similarity fraction, rounded to two decimal place
similarity=round((not_unique/unique_elements)*100,2)
print (f'The similarity score between the two is: {similarity}' )