sentinela = True
idade = 100

while sentinela == True:
    novoNome = str(input('Escreva o nome: '))
    if novoNome.lower == 'stop':
        sentinela = False
    else:
        novaIdade = int(input('Escreva a idade: '))
        if novaIdade < idade:
            idade = novaIdade
            nome = novoNome

print(f'{nome} é a pessoa mais nova com {idade} anos')