class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # find delimiter after length
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # string starts after "#"
            start = j + 1
            end = start + length

            result.append(s[start:end])

            i = end

        return result