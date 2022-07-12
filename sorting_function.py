# START -
#  this program should sort a list from a text file, without using built in functions.
# This function bellow performs sorting function, using the insertion method
def sorting(array): 
    # loops from 1 to len(array_list)
    for i in range (1, len(array_list)): 

        key = array_list[i]

        j = i - 1

        # This moves elements in the array_list that are greater than key to the right 

        while j >= 0 and key < array_list[j]:
            array_list[j + 1] = array_list[j]
            j -=1
            
            array_list[j + 1] = key
            

# Opens the text file "Array.text" where the string list is located
# reads through the file, spliting the string where there is a ",".
# array_list is created where it will hold lists of strings to be sorted.

with open ("Array.txt", "w") as file:
    file.write("my name is ajay reddy and i like to code in python")


with open('Array.txt') as f: 
        array = f.read() 
        array_list = array.split(" ") 

# this initiates the code above to run
sorting(array)

# the ascending sorted list is a stored in a file called "output.text"
with open("output.txt", "w") as f:
    f.write(str(' '.join(array_list)))

# this prints the output.txt file on the terminal.
output = open("output.txt", "r")
print(output.read())
print()

# the ascending sorted list is printed out
# END
