class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    seq = set()

    i = 0
    j = 0

    temp = 0
    longest = 0

    while j < len(s):
      while j < len(s) and s[j] not in seq:
        seq.add(s[j])
        j += 1

      temp = j - i

      if temp > longest:
        longest = temp

      while j < len(s) and s[i] != s[j]:
        seq.remove(s[i])
        i += 1
      
      temp = j - i

      seq.remove(s[i])
      i += 1

    return longest
