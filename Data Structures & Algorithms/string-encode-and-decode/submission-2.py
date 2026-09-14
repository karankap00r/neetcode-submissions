class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        result = []
        for word in strs:
            result.append(str(len(word))+",")
            result.append(word)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return []

        length = 0
        is_len = True
        is_str = False
        current_word = []
        result = []
        for char in s:
            if char.isdigit() and is_len:
                length = length*10 + (ord(char) - ord('0'))
            elif is_len and char == ',':
                is_len = False
                is_str = True
            elif is_str and length > 0:
                current_word.append(char)
                length -= 1
            elif is_str and length == 0:
                is_len = True
                length = (ord(char) - ord('0'))
                result.append("".join(current_word))
                current_word = []

            # print(length, current_word, s)
            
        result.append("".join(current_word))
        return result

            
