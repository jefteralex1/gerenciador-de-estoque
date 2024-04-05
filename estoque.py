import csv

# Definindo a lista de estoque antes de chamar a função para carregar os dados
estoque = []

# Função para carregar os dados do estoque de um arquivo CSV
def carregar_estoque():
    try:
        with open('estoque.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                estoque.append({'nome': row['nome'], 'quantidade': int(row['quantidade']), 'preco': float(row['preco'])})
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Começando com estoque vazio.")

# Função para salvar os dados do estoque em um arquivo CSV
def salvar_estoque():
    with open('estoque.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['nome', 'quantidade', 'preco'])
        writer.writeheader()
        for item in estoque:
            writer.writerow({'nome': item['nome'], 'quantidade': item['quantidade'], 'preco': item['preco']})

# Função para adicionar um novo item ao estoque
def adicionar_item():
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade do item: "))
    preco = float(input("Digite o preço do item: "))
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print("Item adicionado ao estoque.")

# Função para atualizar a quantidade de um item no estoque
def atualizar_estoque():
    nome = input("Digite o nome do item que deseja atualizar: ")
    for item in estoque:
        if item["nome"] == nome:
            nova_quantidade = int(input("Digite a nova quantidade: "))
            item["quantidade"] = nova_quantidade
            print("Estoque atualizado.")
            return
    print("Item não encontrado no estoque.")

# Função para remover um item do estoque
def remover_item():
    nome = input("Digite o nome do item que deseja remover: ")
    for item in estoque:
        if item["nome"] == nome:
            estoque.remove(item)
            print("Item removido do estoque.")
            return
    print("Item não encontrado no estoque.")

# Função para exibir o estoque atual
def exibir_estoque():
    print("Estoque atual:")
    for item in estoque:
        print(f"Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: {item['preco']}")
    print()

# Função para calcular o valor total do estoque
def calcular_valor_total():
    total = 0
    for item in estoque:
        total += item["quantidade"] * item["preco"]
    print(f"O valor total do estoque é: R$ {total:.2f}")

# Antes do loop principal, carregue os dados do estoque do arquivo CSV
carregar_estoque()

# Loop principal do programa
while True:
    print("----- Controle de Estoque -----")
    print("1. Adicionar Item")
    print("2. Atualizar Estoque")
    print("3. Remover Item")
    print("4. Exibir Estoque")
    print("5. Calcular Valor Total do Estoque")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        atualizar_estoque()
    elif opcao == "3":
        remover_item()
    elif opcao == "4":
        exibir_estoque()
    elif opcao == "5":
        calcular_valor_total()
    elif opcao == "6":
        salvar_estoque()
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
