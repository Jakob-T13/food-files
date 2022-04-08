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

#remove the erroneous lines
