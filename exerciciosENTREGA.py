# python-blueedtech
Atividades do módulo 1 do curso da Blue Edtech
#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado 
   # da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


soma = 0
mult = 0
divInt = 0
maior = 0
parImpar = 0
md = 0
while True:
   n1 = int(input('Primeiro numero: '))
   n2 = int(input('Segundo numero: '))
   soma = n1+n2
   print(f'\n-> A soma entre {n1} + {n2} = {soma}')
   mult = n1*n2
   print(f'-> A multiplicação entre {n1} X {n2} = {mult}')
   divInt = n1//n2
   print(f'-> A divisão inteira entre {n1} // {n2} = {divInt}')
   if n1>n2:
      print(f'-> Entre {n1} e {n2} o maior é {n1}')
   elif n1<n2:
      print(f'-> Entre {n1} e {n2} o maior é {n2}')
   if mult%2==0:
      print(f'-> A multiplicação entre {n1} e {n2} resulta em um número PAR')
   elif mult%2!=0:
      print(f'-> A multiplicação entre {n1} e {n2} resulta em um número IMPAR')
   if n1>n2:
      print(f'-> Entre {n1} e {n2} o maior número é {n1}')
   elif n1<n2:
      print(f'-> Entre {n1} e {n2} o maior número é {n2}')
   if divInt != 0 and mult>40:
      if mult>40:
         md=mult/divInt
         print(f'-> Como {mult} é maior que 40 -> {mult}/{divInt} = {md}')
   elif mult<40:
      print(f'-> A multiplicação entre {n1} e {n2} deu {mult}, que é menor do que 40.')    
   elif divInt == 0 and mult > 40:
      print(f'-> Como {mult} é maior que 40 -> {mult}/{divInt} = 0')




#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada 
# pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u 
# e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input('Digite uma frase:  ').lower()

a=0
e=0
i=0
o=0
u=0

for letra in frase:
    if letra == 'a':
        a+=1
    if letra == 'e':
        e+=1
    if letra == 'i':
        i+=1
    if letra == 'o':
        o+=1
    if letra == 'u':
        u+=1
        
print(f'A: {a}')
print(f'E: {e}')
print(f'I: {i}')
print(f'O: {o}')
print(f'U: {u}')

nova = frase.replace('a','')
nova1 = nova.replace('e','')
nova2 = nova1.replace('i','')
nova3 = nova2.replace('o','')
nova4 = nova3.replace('u','')
print(f'Esta é a frase sem nenhuma vogal: {nova4}')

   

   


#03 - Utilizando estruturas de repetição com teste lógico, 
# faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, após entrar 
# dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
# onde o computador vai “pensar” em um número entre 0 e 10. O jogador 
# vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite 
# do usuário diga a ele se o número escolhido pelo computador é maior ou 
# menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.



from time import sleep
from random import randint
senha = '123abc'
entrada = ' '
numComp = 0
numUser = 0
contador = 0
while entrada != senha:
   entrada = str(input('Digite sua senha: '))
   if entrada == senha:
      print('Senha aceita!')
   #   sleep(1)
      print('Seja muito bem vindo!')
   #   sleep(1)
      print('Este é o jogo da adivinhação.')
    #  sleep(1)
      print('O computador vai pensar em um número entre 0 e 10.')
    #  sleep(2)
      print('Sua missão será adivinhar o número que o computador pensou.')
    #  sleep(2)
      numComp = randint(0,10)
      while True:
         numUser = int(input('Escolha um número entre 0 e 10: '))
         contador += 1
         if numComp == numUser:
            print('Parabéns, você acertou!')
            print(f'Foram necessárias {contador} tentativas.')
            print('Fim do programa!')
            break
         elif numComp != numUser:
            print('Humm! Ainda não, mas tente novamente!')
            if numComp > numUser:
               print('O número é MAIOR do que o que você digitou.')
            elif numComp < numUser:
               print('O número é MENOR do que o que você digitou.')
  



#04 - Utilizando funções e listas faça um programa que receba uma data 
# no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso 
# de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

def dataExtenso(data_string):
   try:
      datetime.strptime(data_string, '%d/%m/%Y')
   except ValueError:
      print('Formato inválido, use DD/MM/AAAA')
      return None
   else:
      data_datetime = datetime.strptime(data_string, '%d/%m/%Y')
      return datetime.strftime(data_datetime, '%d de %B de %Y')

data =str(input('Insira a data no formato DD/MM/AAAA: '))
dataE = dataExtenso(data)
if dataE is not None:
   print(dataE)


#05 - Refatore o exercício 2, para que uma função receba a frase, 
# faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

frase = input('Digite uma frase:  ').lower()
c1 = frase.count('a')
c2 = frase.count('e')
c3 = frase.count('i')
c4 = frase.count('o')
c5 = frase.count('u')
c6 = c1+c2+c3+c4+c5



a=0
e=0
i=0
o=0
u=0

for letra in frase:
    if letra == 'a':
        a+=1
    if letra == 'e':
        e+=1
    if letra == 'i':
        i+=1
    if letra == 'o':
        o+=1
    if letra == 'u':
        u+=1
        
print(f'A: {a}')
print(f'E: {e}')
print(f'I: {i}')
print(f'O: {o}')
print(f'U: {u}')

nova = frase.replace('a','')
nova1 = nova.replace('e','')
nova2 = nova1.replace('i','')
nova3 = nova2.replace('o','')
nova4 = nova3.replace('u','')
print(f'Esta é a frase sem nenhuma vogal: {nova4}')
print(f'Foram removidas {c6} letras.')

#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

respostas = 0

lista = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']

pergunta1 = input(f'{lista[0]}   ').strip().upper()[0]
if pergunta1 == 'S':
    respostas += 1
elif pergunta1 == 'N':
    respostas += 0
else:
    print('Resposta inválida!')


pergunta2 = input(f'{lista[1]}   ').strip().upper()[0]
if pergunta2 == 'S':
    respostas += 1
elif pergunta2 == 'N':
    respostas += 0
else:
    print('Resposta inválida!')


pergunta3 = input(f'{lista[2]}   ').strip().upper()[0]
if pergunta3 == 'S':
    respostas += 1
elif pergunta3 == 'N':
    respostas += 0
else:
    print('Resposta inválida!')



pergunta4 = input(f'{lista[3]}   ').strip().upper()[0]
if pergunta4 == 'S':
    respostas += 1
elif pergunta4 == 'N':
    respostas += 0
else:
    print('Resposta inválida!')

pergunta5 = input(f'{lista[4]}   ').strip().upper()[0]
if pergunta5 == 'S':
    respostas += 1
elif pergunta5 == 'N':
    respostas += 0
else:
    print('Resposta inválida!')


if respostas == 0:
    print('Inocente')

elif respostas == 1:
    print('Inocente')

elif respostas == 2:
    print('Suspeita')

elif respostas == 3:
    print('Cumplice')

elif respostas == 4:
    print('Cúmplice')

elif respostas == 5:
    print('Assassino')

#07 - Crie um programa onde o usuário possa digitar sete valores numéricos 
# e cadastre-os em uma lista única que mantenha separados os valores pares 
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


lista = [[],[]]

for c in range(0,7):
   num = int(input('Digite um numero: '))
   if num %2 == 0:
      lista[0].append(num) 
      lista[0].sort()
   else:
      lista[1].append(num)
      lista[1].sort()

print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')

#08 - Crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também 
# o ano de contratação e o salário. Calcule e acrescente , além da idade, 
# com quantos anos a pessoa vai se aposentar. Considere que o trabalhador 
# deve contribuir por 35 anos para se aposentar.

dados = dict()
while True:
   dados['nome'] = str(input('Nome: '))
   anoN= int(input('Ano [Formato AAAA]: '))
   dados['ano nascimento']  = anoN
   dados['carteira de trabalho'] = int(input('Nº Carteira de trabalho [se não tiver digite 0]: '))
   if  dados['carteira de trabalho'] != 0:
      dados['ano contratacao'] = int(input('Ano de contratação: '))
      dados['salario']=float(input('Salário: '))
      dados['idade de aposentadoria'] = dados['ano contratacao']+35
   from datetime import datetime
   year = datetime.today().year
   idade = year - anoN
   dados['idade']=idade
   print(dados)
