"""Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele, lendo o nome dos
alunos e escrevendo na tela o nome do escolhido."""

from random import choice

Aluno1 = str(input('Primeiro Aluno: '))
Aluno2 = str(input('Segundo Aluno: '))
Aluno3 = str(input('Terceiro Aluno: '))
Aluno4 = str(input('Quarto Aluno: '))

lista = [Aluno1, Aluno2, Aluno3, Aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}!'.format(escolhido))
