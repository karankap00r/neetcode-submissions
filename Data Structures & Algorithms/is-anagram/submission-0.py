class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}
        for ch in s:
            s_chars[ch] = s_chars.get(ch, 0) + 1

        for ch in t:
            t_chars[ch] = t_chars.get(ch, 0) + 1

        return s_chars == t_chars