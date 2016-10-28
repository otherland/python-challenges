"""
 An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.

You are given two words or phrase. Try to verify are they anagrams or not.

Input: Two arguments as strings.

Output: Are they anagrams or not as boolean (True or False)
"""

clean = lambda x: sorted(map(str.lower, filter(str.isalpha, x)))
verify_anagrams = lambda a, b: clean(a) == clean(b)


# not mine
verify_anagrams = lambda f, s, p = lambda x: sorted(x.lower().replace(" ","")) : p(f) == p(s)



assert verify_anagrams("Programming", "Gram Ring Mop") == True

assert verify_anagrams("Hello", "Ole Oh") == False

assert verify_anagrams("Kyoto", "Tokyo") == True

