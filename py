#Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.
#The length of the list can be less than 4 also.

#lex_auth_0127135811649044481146

def find_nine(nums):
    #Remove pass and write your code here
	result = False
	for i in nums:
	    if i == 9:
	        result = True
	        return result

nums=[1,9,4,5,6]
print(find_nine(nums))
