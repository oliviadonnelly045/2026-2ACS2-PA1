#my_schedule = open("schedule.txt") #by default opens in read mod, can open on write or append mode

#my_schedule = open("schedule.txt", "w") #write mode...

#my_schedule.write("Changing content!") #...overwrites all files contents.

my_schedule = open("schedule.txt", "a") #append mode...
my_schedule.write("\nAdding content!") #...adds to the end of the file contents.

'''
To create a new file in Puthon, just open one that doesn't exist in an edit mode or x mode.
'''

new_file = open("new_file.txt", "w") #just creatses new file
new_file.write("HI")

"""#write a while loop that looks for "Mod 2"
#Then write a for loop that prints out Mod 2 schedule

line = my_schedule.readline() #control variable for while loop

while line != "Mod: 2\n":
    line = my_schedule.readline() #advances cursor until we find Mod: 2

print(line) #print the Mod 2 label

for i in range (3): #now we are at the right place so
    print(my_schedule.readline()) #print the next 3 lines"""