from collections import Counter
class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the minimum frequency counter with the first word
        min_freq = Counter(words[0])
        
        # Iterate over the rest of the words and update the minimum frequency counter
        for word in words[1:]:
            word_freq = Counter(word)
            for char in min_freq:
                if char in word_freq:
                    min_freq[char] = min(min_freq[char], word_freq[char])
                else:
                    min_freq[char] = 0
        
        # Build the result based on the minimum frequencies
        result = []
        for char in min_freq:
            result.extend([char] * min_freq[char])
        
        return result