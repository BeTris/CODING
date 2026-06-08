'''A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.'''

#TC - O(N*L) N is number of words, L is length of each word. lookup takes constant time
#SC - set 0(N), queue O(N) . so O(N) time 
def ladderLength( beginWord, endWord, wordList) -> int:
        #graph problem
        queue = [(beginWord,1)]
        wordSet = set(wordList)#convert to set for O(1) lookup
        while(queue):
            word,level = queue.pop(0)
            print(word,level)
            # orig_word = word
            if word == endWord:
                return level
            for i in range(len(word)):
                # word  = orig_word 
                for ch in range(ord('a'), ord('z') + 1):
                    next_word=word[:i]+chr(ch)+word[i+1:]
                    # print(next_word)
                    if next_word in wordSet:    
                        queue.append((next_word,level+1))
                        wordSet.remove(next_word)
        return 0
                        
ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])

                        
