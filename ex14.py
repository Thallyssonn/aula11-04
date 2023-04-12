students = {
    'João': {
        'idade': 18,
        'cidade': 'São Paulo',
        'notas': [7.5, 8.0, 9.0]
        
    },
    'Maria': {
        'idade': 19,
        'cidade': 'Rio de Janeiro',
        'notas': [6.5, 7.0, 8.5]
    
    },
    'Pedro': {
        'idade': 19,
        'cidade': 'Belo horizonte',
        'notas': [8.0, 8.5, 9.5]
        
    }
    
}
#Imprimir a idade de João
print('A idade de joão é: ' + str(students['João']['idade']))
#Adicionar uma nova nota para Maria.
students['Maria']['notas'].append(9.0)
#Imprimir todas as informaçoes dos alunos.
for students, info in students.items():
    print(students + ':')
    print('Idade: ' + str(info['idade']))
    print('cidade:' + info['cidade'])
    print('notas: ' + str(info['notas']))
    print('Media: ' + str(sum(info['notas']) / len(info['notas'])))