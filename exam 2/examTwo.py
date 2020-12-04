# Exam 2 
# Adrian Lopez

def minFallingPathSum(lst):

    for i in range(len(lst)):
        for j in range(i):
            return

    return


def palindromicSubString(string):
    res = 0
    strlen = len(string)
    #base case: empty string
    if string <= 0:
        return string
    #base case: single char string
    if strlen == 1:
        res += 1
    #check for substrings greater than 1
    i = 2
    for i in range(strlen):
        return
    return

def arithmeticSlices(lst):
    newlst = [len(lst)] #new array to keep track of true difference
    res = 0
    for i in range(len(lst)):
        if lst[i] - lst[i-1] == lst[i-1] - lst[1-2]: #checking if differences are equal through list
            # newlst[i] = 1 + 
            res += newlst[i]

    return res
 
def maxLengthPairChain(lst):

    count = 0
    for i in range(len(lst)):
        for j in range(i):
            if lst[i][1] < lst[j][0]:
                # 
                #count +=1
                break
    return 

def perfectSquares(n):
    #base case
    if n <= 3:
        return n
    nSquared = n * n
    nTrack = n
    for i in range(1, n+1):
        if nSquared > n:
            break
        else:
            nTrack = min(n, perfectSquares(n - nSquared))
    return nTrack