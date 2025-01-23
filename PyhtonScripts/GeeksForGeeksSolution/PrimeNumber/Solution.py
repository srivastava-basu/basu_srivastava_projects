#User function Template for python3

### PROBLEM STATEMENT ###
# Given a number n, determine whether it is a prime number or not. 
#A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
class Solution:
    def isPrime(self, n):
        # code here
        flag = False
        if n == 1:
            print('Not Prime')
        else:
            for i in range(2, n):
                if n%i == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag == False:
                return False
            else:
                return True

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends
