#Constraints:
#1 <= txt.size(),pat.size() <= 1000
#Function to locate the occurrence of the string x in the string s.
class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        #converting the strings to lower case
        txt = txt.lower() 
        pat = pat.lower()
        tmpSubStr = ''
        for i in range(0,len(txt)):
            for j in range(i,i+len(pat)):
                # to ensure index out of bounds is not encountered
                if i+len(pat) > len(txt):
                    break
                #making chunks of substrings equivalent to the length of the pattern
                else:
                    tmpSubStr = tmpSubStr + txt[j]
            if tmpSubStr == pat:
                loc = i
                break
            else:
                loc =-1
                tmpSubStr = ""
        return loc

#{ 
 # Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        s = input()
        p = input()
        ob = Solution()
        print(ob.firstOccurence(s, p))

        print("~")

# } Driver Code Ends
