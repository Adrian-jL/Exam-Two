# Exam 2 ReadMe

# PROBLEM 5. #
1. Maximum Length of Pair Chain
    [[1,2],
     [2,3],
     [3,4]]
    -   By using a variable count we can try and keep count of the 2-D array and compare the values that correspond to the lst[.][-1] and the value in the next array to it.
    If given values (a, b) and (c, d) we need to check if b < c, if it is there is a chance it can chain. If it does chaing we need to compare the next values which would be if (a,b)(c,d) are ordered and the count would be set to 2. we can check each pair by comparing pairs[i][1] (this would be checking the second column Ex. first 2 in the given array above) < pairs[j][0] (this would be checking the first column) if it is we want to check if it is then ordered, if it is we raise the count.
2. If we can compare from columns we will be able to see if the numbers next to it are ordered by comparison of less than to greater, if it is we store this value in a new array and when paired we increase the count.
3. Using Duke and IDEAL I saw a pattern that displayed of checking through each column. after this writing down an example and comparing for example if we used the values 
[[1,2],
[2,3]] we can see when pairs[i] = 0 we get pairs [0][1] compared to pairs[j] = 1 we get pairs[1][0] and when check if first pair is less than [2] < [2] which would be false making that pair not a chain.
