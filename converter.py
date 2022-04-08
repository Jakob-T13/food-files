import json

#open files
foodf = open("foods.txt", "rt")
fiberf = open("highfiber.txt", "rt")
fatf = open("lowfat.txt", "rt")
glyf = open("low-glycemic-index.txt", "rt")

#read file contents into lists
foodlst = foodf.readlines()
fiberlst = fiberf.readlines()
fatlst = fatf.readlines()
glylst = glyf.readlines()

#close files since we're done with them
foodf.close()
fiberf.close()
fatf.close()
glyf.close()

#combine the lists into one big iterable list
biglst = [foodlst, fiberlst, fatlst, glylst]


#clean the data
for i in range(4):
    biglst[i].pop(30)     #blank line
    biglst[i].pop(12)     #junk data
    for j in range(len(biglst[i])):
        entry = biglst[i][j]    #write to var for optimization
        entry = entry.title()   #convert to Title Case
        entry = entry.strip()   #strip whitespace and newlines
        biglst[i][j] = entry    #write cleaned entry back to the list


print(biglst)
