lista_produto = []
lista_preco = []

if lista_produto:
    for i, prod in enumerate(lista_produto):
        print(f"{i + 1} - {prod}.............R${lista_preco[i]}")
else:
    print("\nNão tem produtos cadastrados!\n")

cont = ""

try:

    while cont != "N":

        produto = input("Digite o produto: ").lower()
        valor = float(input("Digite o valor do produto: R$"))

        # As linhas abaixo adiciona ao final da lista.

        lista_produto.append(produto)
        lista_preco.append(valor)

        cont = ""

        while cont != "N" and cont != "S":

            cont = input("Deseja continuar cadastrando? (S) Sim | (N) Não: \n").upper()
        
            if cont != "N" and cont != "S":
                print("Você só pode digitar (S) ou (N)\n")

except ValueError:
    print("O campo 'Preço do produto' só aceita números")



print("-"*30)
titulo = "PRODUTOS CADASTRADOS"
largura = 30
titulo_center = titulo.center(largura)
print(titulo_center)
print("-"*30)

# O enumerate vai numerar os itens dentro da lista, porem, quando realizamos isso no FOR 
# precisamos colocar uma variável que vai ser responsavel pelo indice.
# já que a lista começa na pocisão 0, vamos colocar na variavel "i" o +1 para a lista iniciar 
# do número 1.


if lista_produto:
    for i, prod in enumerate(lista_produto):
        print(f"{i + 1} - {prod}.............R${lista_preco[i]:.2f}")

else:
    print("Não tem produtos cadastrados")

try:

    posicao = int(input("\nDigite a posição do item: ")) -1 #para conseguir acessar o item correto
    # utilizando o indice apresentado no programa e não o indice original da lista que inicia em 0.

    alt_produto = input("\nDigite o produto: ")

    alt_preco = float(input("\nDigite o valor: R$"))

    lista_produto[posicao] = alt_produto
    lista_preco[posicao] = alt_preco

    print("-"*30)
    titulo = "PRODUTOS CADASTRADOS"
    largura = 30
    titulo_center = titulo.center(largura)
    print(titulo_center)
    print("-"*30)
    
    if lista_produto:
        for i, prod in enumerate(lista_produto):
            print(f"{i + 1} - {prod}.............R${lista_preco[i]:.2f}")

    else:
        print("Não tem produtos cadastrados")

except IndexError:
    print("Posição informada não existe na lista")

