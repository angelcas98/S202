class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} está ministrando uma aula sobre o assunto {assunto}')


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print(f'O aluno {self.nome} está presente')


class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        if alunos is None:
            self.alunos = []
        else:
            self.alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f'O aluno {aluno.nome} está presente')

    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        print(", ".join([aluno.nome for aluno in self.alunos]))


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos", [aluno1, aluno2])
aula.listar_presenca()
