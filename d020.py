import random
#
aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
#
alunoSorteados = random.sample(alunos, 4)
#
print('A ordem dos alunos para a apresentação é: {}, {}, {}, {}'.format(alunoSorteados[0], alunoSorteados[1],
                                                                        alunoSorteados[2], alunoSorteados[3]))
