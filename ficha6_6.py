'''
 Crie um jogo com 3 advinhas do tipo "Qual a cor do cavalo branco do 
Napoleão?", cada uma com 3 alternativas, apresentando o resultado final.

'''

resposta = str(input('Qual a cor do cavalo branco de Napoleão? Vermelho, verde ou branco? '))

if resposta.lower() == 'branco':
    print('Correto')
else:
    print('Errado, é branco')