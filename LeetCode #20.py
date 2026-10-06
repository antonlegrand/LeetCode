"""
Exercice 20
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Rechercher l'ordre de fermeture et vérifier s'il y a fermeture 
Même type doit être fermé 
Ordre de fermeture , inclus les uns dans les autres 
Si ouverture d'un des types , rechercher sa fermeture 
Prendre la taille de s 
si nombre impaire alors false dans tous les cas 
Si je prends le 1er symbole , en partant de la fin ou de la deuxième ? 
(){}[]
 
({}[)] false 
( -> { -> } -> [ -> ) 
sign_open
    if 'one of the three' 
        look into the next , if not closing 
            then continue and stock into sign_open the sign 

( -> { -> } -> [ -> ) -> ]
(
    { not ( -> sign_open = ( 
        } -> closing 
            [ -> open
                ) -> closing 
                    
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"
"""

class Solution:
    def isValid(self, s: str) -> bool:
        mapping_sign = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        open_signs = set(mapping_sign.keys())
        sign_open = []


        if len(s) % 2 != 0:
            return False

        for sign in s:
            if sign in open_signs:  
                sign_open.append(sign)
            else:  
                if not sign_open:
                    return False
                last_open = sign_open.pop()
                if mapping_sign[last_open] != sign:
                    return False

        return not sign_open
s = "({"+"}[" + ")" + "]"  
print(Solution().isValid(s))
print(Solution().isValid("()"))
print(Solution().isValid("()[]{"+"}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([])"))
print(Solution().isValid("([)]"))
