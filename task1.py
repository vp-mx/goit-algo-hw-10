import pulp as pl

# Create a linear programming problem.
problem = pl.LpProblem("Production_Optimization", pl.LpMaximize)

# Define decision variables
x = pl.LpVariable("Lemonade", lowBound=0, cat='Integer')
y = pl.LpVariable("FruitJuice", lowBound=0, cat='Integer')

# Maximize the total production (x + y)
problem += x + y, "Total_Production"

# Set limits.
problem += 2 * x + 1 * y <= 100, "Water"
problem += x <= 50, "Sugar"
problem += x <= 30, "Lemon_Juice"
problem += 2 * y <= 40, "Fruit_Puree"
problem.solve()

# Print the results
print("Status:", pl.LpStatus[problem.status])
print("Optimal Lemonade production:", x.varValue)
print("Optimal Fruit Juice production:", y.varValue)
print("Total production:", pl.value(problem.objective))
