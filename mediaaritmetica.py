#CARLA PRISCILA - ATIVIDADE 02

media = 0
while media < 6:
    nota1 = float(input('Digite a 1ª nota: '))
    while nota1 < 0 or nota1 > 10:
        if nota1 < 0:
            print('Número inválido')
        if nota1 > 10:
            print('Número inválido')
        nota1 = float(input('Digite a 1ª nota: '))

    nota2 = float(input('Digite a 2ª nota: '))
    while nota2 < 0 or nota2 > 10:
        if nota2 < 0:
            print('Número inválido')
        if nota2 > 10:
            print('Número inválido')
        nota2 = float(input('Digite a 2ª nota: '))
    
    media = (nota1 + nota2 ) / 2
    print('A média do aluno é: ', media)

    if media < 6: 
        print('Reprovado')
else:
     print('Aprovado')