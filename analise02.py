import json

#pegar nome dos alunos no dados.json

with open('dados.json', 'r') as file:
    data = json.load(file)
    nomes_alunos = [aluno['aluno'] for aluno in data]
    for i, nome in enumerate(nomes_alunos, 1):
        print(f"{i}. {nome}")








