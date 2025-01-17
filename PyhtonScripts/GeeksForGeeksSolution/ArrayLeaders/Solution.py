### PROBLEM STATEMENT ###
#You are given an array arr of positive integers. 
#Your task is to find all the leaders in the array.
#An element is considered a leader if it is greater than or equal to all elements to its right. 
#The rightmost element is always a leader.

class Solution:
    def leaders(self, arr):
        # code here
        maxValue = arr[-1] # Right most element is always a leader, hence assigning it to max value.
        finalList = [maxValue] # add the max value to finalList
        for i in range(len(arr) - 2, -1, -1): # Navigating the list from right to left
            if arr[i] >= maxValue: # If any element is greater than the max value backward navigation, it becomes the max value and is added to the list
                maxValue = arr[i]
                finalList.append(maxValue)
        finalList.reverse() # Reversing the list as per the requirement in problem statment.
        return finalList

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends
