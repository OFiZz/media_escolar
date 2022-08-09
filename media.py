def linha():
    print('-' * 15)


def calculo(nota, contagem, media_minima):
    pont_max = media_minima * contagem
    resto = pont_max - nota
    restante = contagem - 1
    if restante == 0:
        restante += 1
        fim = resto / restante
        return fim
    else:
        fim = resto / restante
        return fim


boletim = {'Aluno': input('Digite o nome do aluno: ').capitalize()}
sistema_media = {'bimestral': 4, 'trimestral': 3, 'semestral': 1}
todas_notas = []
soma = 0
linha()
aprovacao = int(input('Qual a media para aprovação da instituição? '))
linha()

while True:
    try:
        periodo = input('Sua escola divide as notas anuais em bimestral, trimestral ou semestral?  ').lower()
        duracao = sistema_media[periodo]
    except KeyError:
        print('Digite apenas uma das palavras chaves forneciadas a seguir: bimestral, trimestral ou semestral')
        linha()

    else:
        break

while True:
    materia = input('digite o nome da materia ou fim para exibir a media: ').lower()

    if materia == 'fim':
        linha()
        break
    linha()
    nota = float(input('digite uma nota para {}: '.format(materia.capitalize())))
    linha()
    todas_notas.append(nota)
    boletim[materia] = nota

for i in todas_notas:
    soma += i

media = soma / len(todas_notas)
boletim['media'] = media
desejo = calculo(media, duracao, aprovacao)

if media < aprovacao:
    print('Sua media não atende os requisitos minimos de aprovação')
    linha()
    print(f'Situação: {periodo.capitalize()} reprovado')
    linha()

else:
    print('Muito bem! você superou os requisitos minimos de aprovação')
    linha()

    print(f'Situação: {periodo} Aprovado')
    linha()

for e in boletim:
    from time import sleep
    sleep(1)
    print(f'{e}: {boletim[e]}')

linha()
print('Média: {:.2f}'.format(boletim['media']))
linha()

print(f'Você precisará manter a seguinte nota nos proximos {periodo} para ser aprovado no ano letivo: {desejo:.2f}')
print('Terminando nossos serviços...')
