class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'Á'
        elif strs == [""]:
            return ""
        final_str = ''

        for i, word in enumerate(strs):
            for char in word:
                if ord(char) != 0:
                    final_str += chr(ord(char) - 1)
                else:
                    final_str += chr(255)

            if i != len(strs) - 1:
                final_str += 'ñ'

        return final_str

    def decode(self, s: str) -> List[str]:
        if s == 'Á':
            return []
        elif s == "":
            return [""]
        lis = []
        decode_word = ''

        for char in s:
            if char == 'ñ':
                lis.append(decode_word)
                decode_word = ''
            elif ord(char) == 255:
                decode_word += chr(0)
            else:
                decode_word += chr(ord(char) + 1)

        lis.append(decode_word)

        return lis
            