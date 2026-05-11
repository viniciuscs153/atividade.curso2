clientes = []

faturamento = 0

pedidos = []
pedido_atual = ""
cliente_atual = ""


itens_atual = []
preço_atual = []

itens = ["X-burguer", "S-salada", "Fritas"]

preços = [18.50, 21.00, 9.00]

while True:
    print("CARDAPIO")
    for i in range(len(itens)):
        print (itens[i], preços[i])

    cliente_atual = input(f"Digite o nome do cliente N°{len(clientes)+1}: ")

    if cliente_atual == "fim":
        break
    clientes.append(cliente_atual)

    while True:
        pedido_atual = int(input("Digite o numero do seu produto:"))

        if pedido_atual == 0:
            break
    
        print (itens[pedido_atual-1], preços [pedido_atual-1])
        itens_atual.append(itens[pedido_atual-1])
        preço_atual.append(preços[pedido_atual-1])
    


    print (f"pedido de {cliente_atual}")
    for i in range(len(itens_atual)):
        print (f"-{itens_atual[i]}, {preço_atual[i]}")
    
    print(f"TOTAL R${sum(preço_atual)}")

    faturamento += sum(preço_atual)

    itens_atual = []
    preço_atual = []

print (f"""
       tatal de clientes atendidos: {len (clientes)}
        nome dos clientes atendidos: {clientes}
        item mais caro do cardapio: {max(preços)}
        item mais barato do cardapio: {min(preços)}
        faturamento total do dia {faturamento}
       
       """)