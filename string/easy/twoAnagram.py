#DONE
'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.



An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1

Input : s = "anagram" , t = "nagaram"

Output : true

Explanation :

We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.

Example 2

Input : s = "dog" , t = "cat"

Output : false

Explanation :

We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.'''
from collections import defaultdict

def func(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq_map = defaultdict(int)
    for i in  range(0,len(s1)):
        freq_map[s1[i]]+=1
        freq_map[s2[i]]-=1
    print(freq_map)
    for val in freq_map:
        if freq_map[val]!=0:
            return False
    return True
print(func("cat","tac"))

# tc -O(n)	SC -> O(k) WHERE K IS UNIQUE CHARACTERS