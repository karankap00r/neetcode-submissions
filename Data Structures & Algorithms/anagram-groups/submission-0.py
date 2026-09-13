class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for word in strs:
            mapping[word] = "".join(sorted(word))
        strs.sort(key=lambda x: mapping[x])

        idx = 0
        result = []
        while idx < len(strs):
            current_set = [strs[idx]]
            idx += 1
            
            while idx < len(strs) and mapping[strs[idx]] == mapping[strs[idx-1]]:
                current_set.append(strs[idx])
                idx += 1
            result.append(current_set)

        return result

        