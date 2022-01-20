def linha():
    print('-' * 15)

def calculo(nota, contagem, media_minima):
    pont_max = media_minima * contagem
    resto = pont_max - nota
    restante = contagem - 1
    if restante == 0:
        restante +=1
        fim = resto / restante   
        return fim     
    else:
        fim = resto / restante
        return fim

boletim = {}
todas_notas = []
soma = 0


nome = input('Digite o nome do aluno: ')
boletim['Aluno'] = nome
linha()
aprovacao = int(input('Qual a media para aprovação da instituição? '))
linha()

while True:
    periodo = input('Sua escola divide as notas anuais em bimestral, trimestral ou semestral?  ')
    periodo.lower()
    linha()
    if periodo == 'bimestral':
        duracao = 4   
        break  
    elif periodo == 'trimestral':
        duracao = 3
        break
    elif periodo == 'semestral':
        duracao = 1
        break     
    else:
        print('Digite apenas uma das palavras chaves forneciadas a seguir: bimestral, trimestral ou semestral')
        linha()

while True:
    materia = input('digite o nome da materia ou fim para exibir a media: ')
    materia.lower
    if materia == 'fim':
        linha()
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
desejo = calculo(media, duracao, aprovacao)

if media < aprovacao:
    print('Sua media não atende os requisitos minimos de aprovação')
    linha()
    if periodo == 'bimestral':
        print('Situação: Bimestre reprovado')
        linha()
    elif periodo == 'trimestral':
        print('Situação: Trimestre reprovado')
        linha()
    else:
        print('Situação: Semestre reprovado')
        print('Você foi reprovado nesse semestre, pois faltaram: {:.2f} pontos para atingir a media '.format(desejo))
        linha()
else:
    print('Muito bem! você superou os requisitos minimos de aprovação')
    linha()
    if periodo == 'bimestral':
        print('Situação: Bimestre Aprovado') 
        linha()
    elif periodo == 'trimestral':
        print('Situação: Trimestre aprovado')
        linha()
    else:
        print('Situação: Semestre aprovado')
        if desejo < 1:    
            print('Mantenha-se na media {} nos proximos semestres para ser constantemente aprovado!'.format(aprovacao))
            linha()

for e in boletim:
    print(f'{e}: {boletim[e]}')

linha()
print('Média: {:.2f}'.format(boletim['media']))
linha()

if periodo == 'bimestral':
    print('Você precisará manter a seguinte nota nos proximos bimestres para ser aprovado no ano letivo: {:.2f}'.format(desejo))
    print('Terminando nossos serviços...')
elif periodo == 'trimestral':
    print('Você precisará manter a seguinte nota nos próximos trimestre para ser aprovado no ano letivo atual: {:.2f}'.format(desejo))
    print('Teminando nossos serviços...')
else:
    print('Terminando nossos serviços...')
    








