"""
Exercice 11

integer array of length n 
height
n
liste de chiffres qui représentent différentes barres 
Exemple 1 
1 8 6 2 5 4 8 3 7

8+6+2+5+4+8+3+7 = 49 
Donc on a la 2ème valeur et la 9ème valeur 
8*7 = 49 
car 8 > 7 donc 8 => 7 ; 7 *7 =49
valeur 1 * valeur 2 
si valeur 1 > valeur 2 alors valeur 1 = valeur 2
valeur 1 * valeur 2

Le 7 vient de la distance entre i valeur 1 et i valeur 2
8 = 1
7 = 8 
8 - 1 = 7 
valeur 1 > valeur 2 donc valeur_height = valeur 2
valeur_height * difference = notre calcul 
reprenons avec 8 et 8 
8 = 2ème place 
8 = 7ème place 
valeur_height = 8 
difference = 5 
8 * 5 = 40 
faire passer les valeurs 
commencé avec les plus grandes valeurs => len(s) max 
height - 1 pour repartir sur la base 

"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            difference = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, current_height * difference)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_water

print(Solution().maxArea(height=[1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea(height=[1,8,6,2,5,4,8,3,7,2,4,6,8]))
