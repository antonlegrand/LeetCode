"""
Exercice 12
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. 
Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, 
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, 
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

D'après l'exemple 1 
J'ai 3749 
donc 
on a d'abord 3000 = 3 * 1000
3749
si je dis que tant que c'est pas inférieur à 0 , tu stockes les lettres 
donc 

3749 - 1000 = 2749 donc > 0 donc string_in_roman = M
2749 - 1000 = 1749 donc > 0 => string = MM
1749 - 1000 = 749 donc > 0 => string = MMM
749 - 1000 < 0 donc faux 
749 - 500 = 249 => string MMMD
249 - 500 = -251 donc faux 
249 - 100 = 149 => string = MMMDC
149 - 100 = 49 => string = MMMDCC
49 - 100 = -51 donc faux 
comme on a un 4 alors 

Boucle qui interroge la 1 ère valeur du chiffre à chaque calcul 
Si first_digit = 4 or 9 
Prendre la lettre et y ajouter un I devant sinon continuer la boucle comme faite 
Cette condition doit s'appliquer à chaque passage 
ou stocker les valeurs 400,900,40,90,4 et 9 directement
Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 


"""


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []
        for value, symbol in zip(values, symbols):
            while num >= value:
                result.append(symbol)
                num -= value

        return "".join(result)


# Tests
print(Solution().intToRoman(3749))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
print(Solution().intToRoman(4))
print(Solution().intToRoman(9))