# Print characters from a string that are present at an even index number
# Exercise 3

# pseudocode

# Creating a starting code for print
#for name in names
word = input('Insert what you want sheesh ')
print("Original String:", word)

# get the length of a string
size = len(word)

# Creating a code that will print the index_number
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index_number[", i, "]", word[i])
    