class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        
        morse_words = set()
        for word in words:
            morse_word = ""
            for ch in word:
                morse_word += morse_map[ch]
            morse_words.add(morse_word)

        return len(morse_words)
