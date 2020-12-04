# Exam 2 ReadMe

# PROBLEM 1. #
1. Minimum Falling Path Sum
    - Given a square matrix [[1,2,3], we can assume that we want store our path to end.
                             [4,5,6],
                             [7,8,9]]
      so we would want to essentially take the path lst[0][0] = 1 , lst[1][0] = 4, and lst[2][0] = 7 which sum = 12, the minimum path. we recursively want to keep track of the path to compare to the remaining paths to find the minimum
2. using a 2d array to compare paths to find the minimum value.
3. Using Duke 7 steps and IDEAL to try and solve this, I tried showing what is essentially the point of DP and storing sub sets of problems to solve the whole problem, I tried solving these subset problems to help solve the whole problem. I also wrote this down to see if it make sense in english. After trying to solve sub sets of the problem there is a point where you can see a patter. After checking by hand it does seem to make sense.

# PROBLEM 2. #
1. Palindromic Substrings
    - Given a string a way I could try and solve the subsets of problems would be to start by checking the middle of a string to see if it is a palindrome. For example, as we do not know the length of the string (only that it will not exceed 1000 character), we want to check "vaoav". If we start at 'o' we see that it is a palindrome, ok now we check the letters next to 'o' which would be "aoa" this is also a palindrome and continue etc. We also see from the given examples that we check for each letter, so this tells me we can start the count equal to the length of the string.
2. by solving each palindrome starting from the middle of the string, if it is valid we keep track of this and count then continue check the rest. I dont believe it is necessary to go letter by letter since we know our count will start at the lenght of the string.
3. Using Duke and IDEAL I noticed right away that the easiest subset of the problem that could be solved is each letter being a palindrom itself and then check from middle to out for the rest of the valid palindromes. After writing out an example and comfirming this should work out it was much clearer. It was also apparent of the patterns, especially since this is a palindrome which is essentially just a pattern in itself.