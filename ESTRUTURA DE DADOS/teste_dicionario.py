
def acessa(dicionario, chave, default):
    return dicionario.get(chave,default)

def mostra_dependencias(dicionario, materia):

    print('\ndicionario: ', dicionario)
    print('\nMateria: ', materia, '\n')

    dependencias = dicionario[materia]

    print('\nDependencias: ', dependencias, '\n')

    dic = {}
    for teste in dependencias:
        dic[teste] = dependencias
        
    print('\ndic: ', dic, '\n')

    for chave in dependencias:
        print(chave)
    print('\n',acessa(dic, dependencias[0], 'nada'))
    if acessa(dic, dependencias[0], 'nada') != 'nada':
        print('\nFunc: ', dependencias, dependencias[0])
        mostra_dependencias(dic, dependencias[0])


simples = {'calculo3' : ['calculo2', 'vetores'],'calculo2' : ['calculo1']}

mostra_dependencias(simples, 'calculo3')