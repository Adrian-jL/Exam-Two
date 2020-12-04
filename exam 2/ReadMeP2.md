# Exam 2 ReadMe

# PROBLEM 2. #
1. Palindromic Substrings
    - Given a string a way I could try and solve the subsets of problems would be to start by checking the middle of a string to see if it is a palindrome. For example, as we do not know the length of the string (only that it will not exceed 1000 character), we want to check "vaoav". If we start at 'o' we see that it is a palindrome, ok now we check the letters next to 'o' which would be "aoa" this is also a palindrome and continue etc. We also see from the given examples that we check for each letter, so this tells me we can start the count equal to the length of the string.
2. by solving each palindrome starting from the middle of the string, if it is valid we keep track of this and count then continue check the rest. I dont believe it is necessary to go letter by letter since we know our count will start at the lenght of the string.
3. Using Duke and IDEAL I noticed right away that the easiest subset of the problem that could be solved is each letter being a palindrom itself and then check from middle to out for the rest of the valid palindromes. After writing out an example and comfirming this should work out it was much clearer. It was also apparent of the patterns, especially since this is a palindrome which is essentially just a pattern in itself.
