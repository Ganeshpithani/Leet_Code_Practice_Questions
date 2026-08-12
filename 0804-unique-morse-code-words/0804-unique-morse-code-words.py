class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        result=set()
        for word in words:
            transformation=""
            for ch in word:
                transformation+=morse[ord(ch)-ord('a')]
            result.add(transformation)
        return len(result)