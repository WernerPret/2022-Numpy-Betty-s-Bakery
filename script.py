# 1
import numpy as np

# 2
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

# 3
recipes = np.genfromtxt('recipes.csv', delimiter=',')

# 4
print(recipes)

# 5
eggs = recipes[:,2]
# print(eggs)

# 6
one_egg = eggs == 1
# print(one_egg)

# 7
cookies = recipes[2,:]
# print(cookies)

# 8
double_batch = cupcakes*2
# print(double_batch)

# 9
grocery_list = cookies + double_batch
print(grocery_list)




