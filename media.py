def linha():
    print('-' * 15)


boletim = {}
todas_notas = []
soma = 0

nome = input('Digite o nome do aluno:')
boletim['Aluno'] = nome
aprovacao = int(input('Qual a media para aprovação da instituição? '))

while True:
    materia = input('digite o nome da materia ou fim para exibir a media: ')
    materia.lower
    if materia == 'fim':
        break
    linha()
    nota = float(input('digite uma nota para {}: '.format(materia)))
    linha()
    todas_notas.append(nota)
    boletim[materia] = nota
    
for i in todas_notas:
    soma += i

media = soma / len(todas_notas)
boletim['media'] = media

if media < aprovacao:
    print('Sua media não atende os requisitos minimos de aprovação')
    linha()
    print('Situação: Reprovado')
else:
    print('Muito bem! você superou os requisitos minimos de aprovação')
    linha()
    print('Situação: Aprovado') 

print(boletim)











