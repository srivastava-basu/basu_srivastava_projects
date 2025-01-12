class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        stringLength = len(s)
        listSubStr = [] #list which holds all the words of distict Character
        subStr = "" #Temporary Sub string used within the loop
        finalOutput = "" #final sub string with distinct characters
        for i in range(0,stringLength): 
            if s[i] in subStr:
                if subStr[0] == s[i]: # if the recurring character is in the first place
                    subStr = subStr.lstrip(s[i]) #strip the first character
                    subStr = subStr + s[i]
                    listSubStr.append(subStr)
                else: #if the character is in the mid of the word
                    for j in range(0,len(subStr)):
                        if subStr[j] == s[i]:
                            listSubStr.append(subStr[0:j+1]) #split the word in two from the recurring character 
                            listSubStr.append(subStr[j:])
                    subStr = listSubStr[-1]
            else: 
                subStr = subStr + s[i]
                listSubStr.append(subStr)
        max_len = -1
        for subString in listSubStr: #loop to check the longest word in all the distinct words
            if len(subString) > max_len:
                max_len = len(subString)
                finalOutput = subString
        return len(finalOutput)
