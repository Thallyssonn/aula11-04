products = {
    'banana': 2.50,
    'maçã': 3.00,
    'laranja': 2.75,
    'abacaxi': 4.50,
    'manga': 3.50
}

#imprimir o preço de uma maçã.
print(' O preço de uma maçã é: R$' + str(products['maçã']))

#Adicionar um novo produto
products['melancia'] = 6.00

#imprimir todos os produtos e seus preços.
for products, price in products.items():
    print(products + ': R$' + str(price))