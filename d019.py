import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
#alunosorteado = random.choice(alunos)
alunosorteado = alunos
random.shuffle(alunosorteado)
print('O aluno sorteado para apagar o quadro é o {}.'.format(alunosorteado))