#! /usr/bin/env /usr/bin/python
def getbin(i):
        dig = []
    while i:
        i, rem = divmod(i, -2)
        if rem<0:
            i, rem = i+1, rem+2
        dig.insert(0, str(rem))
    dig = [int(i) for i in dig]
    dig.reverse()
    return dig
    
def solution(A):
        # write your code in Python 2.7
    entropy = 1
    val = A[0] * 1
    for i in range(1, len(A)):
        entropy *= -2
        val += (A[i] * entropy)
    val = ~val + 1
    
    return getbin(val)
