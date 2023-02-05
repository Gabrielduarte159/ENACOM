from pulp import *

# Definir o problema dando um nome e o objetivo(Baseado em um que exista na Biblioteca)
prob = LpProblem("Knapsack Problem", LpMaximize)

# Itens à investir
itens = [1, 2, 3, 4, 5, 6, 7, 8]
# Custo e Retorno de cada um dos ítens 
peso = {1: 470, 2: 400, 3: 170, 4: 270, 5: 340, 6: 230, 7: 50, 8: 440}
valor = {1: 410, 2: 330, 3: 140, 4: 250, 5: 320, 6: 320, 7: 90, 8: 190}

# Variável que diz se o item está ou não na mochila
x = LpVariable.dicts("item", itens, 0, 1, LpInteger)

# Soma dos valores dos itens
prob += lpSum([valor[i] * x[i] for i in itens]), "Valor Total"

# Restrições do problema 
prob += lpSum([peso[i] * x[i] for i in itens]) <= 1000, "Limite de peso"
prob += x[1] + x[5] <= 1, "Restrição item 1 e 5"#Restringe fazendo com que apenas um deles possa ser 1, ou os dois serem 0
prob += x[2] + x[4] <= 1, "Restrição item 2 e 4"

# Utiliza o solve da biblioteca, que resolve o problema a partir do objetivo dado.
prob.solve()

#Resultados
print("Itens selecionados:")
for i in itens:
    if x[i].value() == 1.0:
        print("Item", i, "com peso", peso[i], "e valor", valor[i])
print("Valor total:", value(prob.objective))