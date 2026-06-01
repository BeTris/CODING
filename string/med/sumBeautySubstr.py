'''he beauty of a string is defined as the difference between the frequency of the most frequent character and the least frequent character (excluding characters that do not appear) in that string.



Given a string s, return the sum of beauty values of all possible substrings of s.


Example 1

Input: s = "xyx"

Output: 1

Explanation: The substrings with non-zero beauty are:

- "xyx" → frequencies: x:2, y:1 → beauty = 2 - 1 = 1

- "xy" → x:1, y:1 → beauty = 0

- "yx" → y:1, x:1 → beauty = 0

- "x" or "y" → beauty = 0

Total sum = 1 (from "xyx") = 1

Example 2

Input: s = "aabcbaa"

Output: 17

Explanation: Various substrings such as "aabc", "bcba", etc., have non-zero beauty values. Summing all gives 17.

Constraints

1 <= s.length <= 500
s consists of only lowercase English letters ('a' to 'z')'''