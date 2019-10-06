database = {}
database['ALUNO'] = []

database['ALUNO']= [{'id': 29, 'nome': 'cicero'}, {'id': 28, 'nome': 'lucas'}]

print('\n', database, '\n')

print('\n', len(database['ALUNO']), '\n')


for aluno in database['ALUNO']:
    if aluno['id'] == 28:
        
        database['ALUNO'].pop(database['ALUNO'].index(aluno))

print('\n', len(database['ALUNO']), '\n')
print('\n', database, '\n')
