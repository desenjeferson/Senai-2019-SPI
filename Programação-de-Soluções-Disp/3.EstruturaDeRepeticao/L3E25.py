# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Informe a quantidade de pessoas: '))
    if (quantidade <= 0):
        print('A quandidade deve ser positiva!')

soma = 0
for i in range(0, quantidade):
    idade = -1
    while (idade < 0):
        idade = int(input('Informe a idade da pessoa: '))
        if (idade < 0):
            print('A idade nao pode ser negativa')
    soma += idade

media = soma / float(quantidade)

if (media <= 25):
    print('A turma eh jovem')
elif (media <= 60):
    print('A turma eh adulta')
else:
    print('A turma eh idosa')
