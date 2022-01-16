boletim = {}
calculadora = []
soma = 0


while True:
    materia = input('digite o nome da materia ou 0 para exibir a media: ')
    if materia == '0':
        break
    nota = int(input('digite uma nota para {}: '.format(materia)))
    calculadora.append(nota)
    boletim[materia] = nota
    
for i in calculadora:
    soma += i

media = soma / len(calculadora)
boletim['media'] = media


print(boletim)









