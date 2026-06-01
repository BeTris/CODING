'''Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.



Return a string with the words in reverse order, concatenated by a single space.


Example 1

Input: s = "welcome to the jungle"



Output: "jungle the to welcome"



Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing the order of these words gives "jungle", "the", "to", and "welcome". The output string should have exactly one space between each word.

Example 2

Input: s = " amazing coding skills "



Output: "skills coding amazing"



Explanation: The input string has leading and trailing spaces, as well as multiple spaces between the words "amazing", "coding", and "skills". After trimming the leading and trailing spaces and reducing the multiple spaces between words to a single space, the words are "amazing", "coding", and "skills". Reversing the order of these words gives "skills", "coding", and "amazing". The output string should not have any leading or trailing spaces and should have exactly one space between each word.'''
def revWords(s):
    s = s.strip(' ')
    stack = []
    wordStack = []
    res =""
    for ch in s:
        stack.append(ch)
    print(stack)
    while(stack!=[]):
        topch=stack.pop()
        print(stack,wordStack)
        if topch == ' ' :
            if(wordStack!=[]):
                while(wordStack!=[]):
                    ch = wordStack.pop()
                    if ch!=" ":
                        res += ch
                res += ' '
        else:
            wordStack.append(topch)
    while wordStack!=[]:
        res += wordStack.pop()
    print(res)
# revWords("  hello  I am ")

#opti approach 
#TC- O(n) , SC - O(1)
def reverse(s,l,r):
    if s == None or s == []:
        return s
    while(l<r):
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
    return s    
def revWordsOpti(s):
    listFromString = list(s)
    listFromString = reverse(listFromString,0,len(listFromString)-1)
    print(listFromString)
revWordsOpti("  Hello I  am ")