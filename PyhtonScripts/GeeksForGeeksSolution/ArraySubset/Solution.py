#User function Template for python3
### AUTHOR: BASU SRIVATAVA ###
### DATE ATTEMPTED: 15-JAN-2024
### PROBLEM STATEMENT ###
#Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. 
#Both arrays are not sorted, and elements are distinct.

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        # Using set to remove duplicates from the array/list
        setA = set(a)
        setB = set(b)
        # Intersection of the list
        setCommon = setA & setB 
        #if the number of elements in the intersection is equal to length of set B, list B is subset of A
        if len(setB) == len(setCommon):
            return True
        else:
            return False
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
