clientes = []

faturamento = []

pedidos = []


cliente_atual = ""
itens_atual = []
preço_atual = []

itens = ["X-burguer", "S-salada", "Fritas"]

preços = [18.50, 21.00, 9.00]

while True:
    for i in range(len(itens)):
        print (itens[i], preços[i])
    cliente_atual = input(f"Digite o nome do cliente N°{len(clientes)+1}: ")
    

