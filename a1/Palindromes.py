print("Enter the strings: ")
userinput = raw_input()                 
userList = [userinput]              # put first string into list

while userinput != "Done":          # get input
    userinput = raw_input()
    userList.append(userinput);     # put into list
userList.remove("Done")

paldict = {}                # create empty dictionary
compareList = userList[:]   # copy list into temporary variable to hold original input

i = 0
index = 0
print("The palindromes are: ")
while i < len(userList):    # iterate until reached length of list
    pal = userList[i]       # variable to hold original string
    compareList[i] = compareList[i].lower()     # put to lowercase
    compareList[i][::-1]                        # reverse
    compareList[i] = compareList[i].replace(" ","") # get rid of whitespace
    compare = compareList[i][::-1]                  # reverse again

    if(compare == compareList[i]):      # compare w/ all whitespace, lower and reversed
        paldict[index+1] = pal           # set key to value
        index = index + 1                 # increase index variable

    i = i + 1   # increment counter variable

print(paldict)      # print dictionary
exit()
