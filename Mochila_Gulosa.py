def mochila_gulosa(itens, peso, valor, capacidade):
    # ordenar itens por relação valor/peso
    itens_ordenados = sorted(itens, key=lambda i: valor[i]/peso[i], reverse=True)
    mochila = []
    valor_total = 0
    peso_total = 0
    
    for i in itens_ordenados:
        if peso[i] + peso_total <= capacidade:
            if (i==5 and 1 in mochila)or(i==4 and 2 in mochila)or(i==1 and 5 in mochila)or(i==2 and 4 in mochila):
                continue
            mochila.append(i)          
            valor_total += valor[i]
            peso_total += peso[i]   
    
    return mochila, valor_total, peso_total

# definir itens disponíveis
itens = [1, 2, 3, 4, 5, 6, 7, 8]

# pesos e valores de cada item
#peso = {1: 470, 2: 400, 3: 170, 4: 270, 5: 340, 6: 230, 7: 50, 8: 440}
#valor = {1: 410, 2: 900, 3: 140, 4: 320, 5: 320, 6: 320, 7: 90, 8: 190}
peso = {1: 470, 2: 400, 3: 170, 4: 270, 5: 340, 6: 230, 7: 50, 8: 440}
valor = {1: 410, 2: 330, 3: 140, 4: 250, 5: 320, 6: 320, 7: 90, 8: 190}

mochila, valor_total, peso_total= mochila_gulosa(itens, peso, valor, 1000)

print("Itens selecionados:", mochila)
print("Valor total:", valor_total*1000)
print("Peso total:", peso_total*1000)


