#start

# This creates the text file word.text, which contains the list of names
f = open("words_input.txt", "w")
f.write("Data visualization using histogram allows one to find and show the basic frequency distribution of a set of data. It permits the assessment of the data for essential distribution and skewness. In a business setup, it is a portrayal of business data and it relates as just a single variable.")
f.close()

# words.txt text file contains a list of words, which are to be sorted without the built in functions 
with open('words.txt') as f: # reads the text file 
    words = f.read() 
    words_list = words.split(" ") # creats a list of strings in the text file

# The application of insertion sort method

for m in range(1, len(words_list)): 
    n = m-1
    next_word = words_list[m]

#While next_word is compared with each elament on its right untill a greater element is obtained
    while (words_list[n] > next_word) and (n >=0):

        words_list[n+1] = words_list[n]
        n = n-1

        words_list[n+1] = next_word
        # next_word is placed after the element greater than it

# this saves the sorted list to a output file called 'output_words.txt'        
f = open("output_words.txt", "a")
f.write(str(', '.join(words_list)))
f.close()

print(words_list) 
# sorted list  
#End