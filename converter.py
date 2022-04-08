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

#cosmetic stuff
foodlst[0] = "Name"     #better column header name
foodlst[15] = "salmon"  #erroneous '2' in original row

#close files since we're done with them
foodf.close()
fiberf.close()
fatf.close()
glyf.close()

#combine the lists into one big iterable list
biglst = [foodlst, fiberlst, fatlst, glylst]


#clean the data
for i in range(4):
    biglst[i].pop(30)       #remove blank line
    biglst[i].pop(25)       #remove duplicate entry
    biglst[i].pop(12)       #remove junk data
    for j in range(len(biglst[i])):
        entry = biglst[i][j]    #write to var for optimization
        entry = entry.title()   #convert to Title Case
        entry = entry.strip()   #strip whitespace and newlines
        biglst[i][j] = entry    #write cleaned entry back to the list

#create output file
outfile = open("foods.json", "wt")

#generate dictionaries, convert them to json, and put them in the output file
for i in range(1,len(biglst[0])):
    dict_entry = {
        biglst[0][0] : biglst[0][i],        #food name
        biglst[1][0] : biglst[1][i],        #high fiber
        biglst[2][0] : biglst[2][i],        #low fat
        biglst[3][0] : biglst[3][i]         #low glycemic index
    }
    json_entry = json.dumps(dict_entry)     #convert dictionary to json
    outfile.write(json_entry+"\n")               #add json entry to output file
    
outfile.close()