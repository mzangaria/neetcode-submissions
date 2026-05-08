class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = {}
        for ch in s: 
            if ch in sLetters:
                sLetters[ch] += 1
            else:
                sLetters[ch] = 1
        
        tLetters = {} 
        for ch in t: 
            if ch in tLetters:
                tLetters[ch] += 1
            else:
                tLetters[ch] = 1
        
        for key in tLetters: 
            if (key not in sLetters) or (sLetters[key] != tLetters[key]):
                return False

        for key in sLetters: 
            if (key not in tLetters) or (tLetters[key] != sLetters[key]):
                return False
        
        return True