# Desenvolvendo um Software para controle de estoque.
# Controle de entrada e saáda de materiais.

estoque = []

def add_item(item_id, nome, quantidade, preço): 
    item = {'id': item_id, 'nome': nome, 'quantidade': quantidade, 'preço': preço} 
    estoque.append(item)

def remove_item(item_id): 
    global estoque
    for item in estoque:
        if item['id'] == item_id: 
            estoque.remove(item) 
            break

def view_estoque(): 
    for item in estoque: 
        print( 
            f"ID: {item['id']}, Nome: {item['nome']}, Quantidade: {item['quantidade']}, Preço: {item['preço']}" 
        )

add_item(item_id='0001', nome='camiseta', quantidade=50, preço=150.50)


while True:

    print("1. Adicionar item") 
    print("2. Remover item") 
    print("3. Atualizar quantidade") 
    print("4. Exibir estoque") 
    print("5. Sair.\n") 
    opcao = input("Digite a escolha:") 
    # manipular escolhas... 
    if opcao == '5': 
        break
    else: 
        print("Escolha inválida. Tente novamente.\n")