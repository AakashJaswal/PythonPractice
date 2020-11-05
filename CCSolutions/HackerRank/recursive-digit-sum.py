# Problem:- https://www.hackerrank.com/challenges/recursive-digit-sum/problem
# TakeAway
# 1.sum of digit = number % 9 (if sum = 9 so result will be 0, take care of that)
# 2.concatenation num k times and multiplying num with k result in same sum of digits.

'''
the goal is to find the super digit, that's like sum of all the digit in the provided no.
@input n, k
we have to append n K times to form a no.
example n = 123 and k = 3
final number = 123123123
'''

''' The below solution should work fine, but is not time efficient 
def magic_num(num):
    if num <10:
        return num
    else:
        sum = 0
        for digit in str(num):
            sum+=int(digit)
        return magic_num(sum)

n,k = input().split(" ")
number = magic_num(int(n*int(k)))
print(number)
        
'''

# Best way to do it:-

n, k = map(int, input().split(" "))
res = n * k % 9
print(res if res else 9)
