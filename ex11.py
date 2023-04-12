agenda = {}

while True:
    nome = input('Digite o nome da pessoa: ')
    if nome == '':
        break
        
    telefone = input('Digite o telefone: ')
    # Adiciona o telefone na agenda
    agenda[nome] = telefone
    
# Pesquisa um telefone na agenda
nome_pesquisa = input('Digite o nome para pesquisar: ')
if nome_pesquisa in agenda:
    print('telefone de', nome_pesquisa, ':', agenda[nome_pesquisa])
else:
    print('Nome não encontrado na agenda.BytesWarning')