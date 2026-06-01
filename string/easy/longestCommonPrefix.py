#DONE
'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.



If there is no common prefix, return an empty string "".


Example 1

Input : str = ["flowers" , "flow" , "fly", "flight" ]

Output : "fl"

Explanation :

All strings given in array contains common prefix "fl".

Example 2

Input : str = ["dog" , "cat" , "animal", "monkey" ]

Output : ""

Explanation :

There is no common prefix among the given strings in array.
'''

def longCommonPrefix(s_list):
    #find the length of smallest word in the list and let it be n
    # n = 3
    #find the smallest word in the list and let it be smallest_word
    smallest_word = min(s_list, key=len)
    n = len(smallest_word)
    commPrefix = ""
    for i in range(0,n):
        for s in s_list:
            if s[i]!=smallest_word[i]:
                return commPrefix
        commPrefix += s[i]
    return commPrefix

print(longCommonPrefix(["flowers" , "flow" , "fly", "flight" ]))