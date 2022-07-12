def similarity_cal(first_submission, second_submission):
    
    
    for word in first_submission:
	
	    if word not in filtered_first_submission:
        # removes  duplicate words in the first submission list
		    filtered_first_submission.append(word)

            
    for word in second_submission:
	
	    if word not in filtered_second_submission:
         # filters the duplicate words in the second submission and appends to a new list
		    filtered_second_submission.append(word)

            
    similar_words = 0
    # takes count of the words which are similar
    for word in filtered_first_submission:

        if word in filtered_second_submission:
            similar_words +=1
        

    elements_in_first_submission = len( filtered_first_submission ) 
    # number of words in the filtered_first_submission

    elements_in_second_submission = len( filtered_second_submission )
    # number of words in the filtered_second_submission

    total_words = elements_in_first_submission + elements_in_second_submission
    #  total number of words when duplicates are removed 


    unique = total_words - similar_words

    similarity = round(( similar_words / unique ) * 100 , 2 )
    #similarity computation
    return (f'The similarity score between the two is: {similarity} %' )


filtered_first_submission = []
filtered_second_submission = []

first_submission = str.lower(str(input('Enter the first submission:  ').split()))
second_submission = str.lower(str(input('Enter the second submission:  ').split()))
similarity = similarity_cal(first_submission, second_submission)


print (similarity)