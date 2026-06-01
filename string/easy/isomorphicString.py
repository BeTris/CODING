#DONE
'''Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.



All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1

Input : s = "egg" , t = "add"

Output : true

Explanation :

The 'e' in string s can be replaced with 'a' of string t.

The 'g' in string s can be replaced with 'd' of t.

Hence all characters in s can be replaced to get t.

Example 2

Input : s = "apple" , t = "bbnbm"

Output : false

Explanation :

Strings are matched index by index.

At index 0, 'a' maps to 'b'.

At index 1, 'p' also maps to 'b'.

This is invalid because two different characters (a and p) cannot map to the same character (b) in a one-to-one mapping.

Therefore, no valid mapping exists and the output is false.'''
#tc O(N) , SC O(N)
def isIso(s1,s2):
    if len(s1)!=len(s2):
        return False
    map_iso = {}
    mapped_values = set()#good catch SEE THIS REVISE
    for i in range (0,len(s1)):
        if s1[i] in map_iso:
            if s2[i] != map_iso[s1[i]]:
                return False
        else:
            if s2[i] in mapped_values:
                return False
            map_iso[s1[i]] = s2[i]
            mapped_values.add(s2[i])
    return True

print(isIso("egg","adb"))

            