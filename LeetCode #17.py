"""
Exercice 17 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]

stocker les combinaisons de chiffres et lettres 
2 = abc
3 = def
4 = ghi
5 = jkl 
6 = mno
7 = pqrs
8 = tuv
9 = wxyz
output doit être sous forme de liste 
maintenant , sortir toutes les combinaisons possible lors de la reconnaisance d'un chiffre 
input un chiffre ounombre 
identifier chaque chiffre de l'input 
23
list 2 = abc 
list 3 = def 
ad ae af bd be bf cd ce cf

"""
class Solution:
    def letterCombination(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = [""]
        for d in digits:
            letters = mapping.get(d, "")
            combinations = [
                prefix + letter
                for prefix in combinations
                for letter in letters
            ]

        return combinations

    def letterCombinations(self, digits: str) -> list[str]:
        return self.letterCombination(digits)

print(Solution().letterCombination("23"))
print(Solution().letterCombinations("2"))
