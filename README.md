# Knapsack-Problem-With-BFS-and-DFS
This code solves a knapsack problem from given table by using Bredth First Search(BFS) and Depth First Search(DFS) algorithams for given constraints.  Maximum wight is 420

### Explanation of the problem

n this assignment we are trying to solve the Knapsack Problem. According to definition we have a product list with weight and benefit values for each product. We need to select products from the list which gives the highest benefit without exceeding givenmaximum weight limit. In our case we have 11 items in the list, so we have X = {X1, X2, X3, ... , X11} for our products. For Xnwe have domain of {0,1}.According to this definition we may have a solution like {0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1}.


### Objective Function

In this problem we want to maximize total benefit of the items in the knapsack. If Xbnis equal to benefit of Xnthen we have following function. 

![image](https://user-images.githubusercontent.com/41572446/122053237-dc78ab80-cde6-11eb-8c77-36459a9e919d.png)


### Restrictions

Given problem has the restrictions for range of Xn and total weight of products in knapsack. So the problem has following restrictions.

Restriction for weight:

![image](https://user-images.githubusercontent.com/41572446/122053581-29f51880-cde7-11eb-988e-7ba596a516f3.png)

Restriction for Xn:

![image](https://user-images.githubusercontent.com/41572446/122053678-3ed1ac00-cde7-11eb-92ca-c39f07950ce6.png)

### Time complexity:

TheBFSalgorithm for 11 element Knapsack problem executed in58.7 ms (0.0587 seconds)in google collab notebook. BesidesDFSalgorithm executer in68 ms (0.068 seconds) in same notebook.

### Memory complexity:
Given Knapsack Problem is used 0.4 mb of memory when we used BFS algorithm to find solution. For the same problem we can also use BFS algorithm uses 0.1 mb of memory



