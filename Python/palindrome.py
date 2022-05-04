# A basic palindrone checker

from pythonds.basic import Deque


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


#print(palchecker("lsdkjfskf"))
#print(palchecker("radar"))

###
###
###
"Found Elsewhere, https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/"
#reverse the string, and check to see if they are equal
def isPalindrome(s):
    return s == s[::-1]
  #### go note: this reverses using the splice as a negative stepper,
  ####  so [begin:end:step]
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
####################
# OR
def isPalindrome2(str):
 
    # Run loop from 0 to len/2 
    for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome2(s)
 
if (ans):
    print("Yes")
else:
    print("No")