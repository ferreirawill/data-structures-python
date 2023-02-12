import multiprocessing
import os
import random
import string
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process, pool
from time import time, sleep


def timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func

# classessJson = {
#    "draw":"1",
#    "recordsFiltered":37,
#    "recordsTotal":37,
#    "data":[
#       {
#          "Id":12649,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"6º A",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12649' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12649' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12649' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12649&turmaNome=6º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12649&turmaNome=6º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12649&turmaNome=6º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12649&turmaNome=6º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12649' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12649' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12649' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12685,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"6º B",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12685' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12685' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12685' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12685&turmaNome=6º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12685&turmaNome=6º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12685&turmaNome=6º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12685&turmaNome=6º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12685' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12685' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12685' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12686,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"7º A",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12686' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12686' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12686' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12686&turmaNome=7º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12686&turmaNome=7º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12686&turmaNome=7º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12686&turmaNome=7º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12686' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12686' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12686' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12687,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"8º A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12687' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12687' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12687' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12687&turmaNome=8º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12687&turmaNome=8º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12687&turmaNome=8º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12687&turmaNome=8º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12687' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12687' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12687' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12688,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"8º B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12688' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12688' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12688' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12688&turmaNome=8º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12688&turmaNome=8º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12688&turmaNome=8º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12688&turmaNome=8º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12688' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12688' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12688' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12689,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"9º A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12689' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12689' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12689' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12689&turmaNome=9º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12689&turmaNome=9º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12689&turmaNome=9º A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12689&turmaNome=9º A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12689' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12689' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12689' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12690,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"9º B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12690' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12690' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12690' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12690&turmaNome=9º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12690&turmaNome=9º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12690&turmaNome=9º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12690&turmaNome=9º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12690' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12690' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12690' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12691,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"6º C",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12691' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12691' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12691' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12691&turmaNome=6º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12691&turmaNome=6º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12691&turmaNome=6º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12691&turmaNome=6º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12691' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12691' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12691' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12692,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"6º D",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12692' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12692' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12692' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12692&turmaNome=6º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12692&turmaNome=6º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12692&turmaNome=6º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12692&turmaNome=6º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12692' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12692' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12692' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12693,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"7º B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12693' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12693' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12693' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12693&turmaNome=7º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12693&turmaNome=7º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12693&turmaNome=7º B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12693&turmaNome=7º B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12693' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12693' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12693' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12694,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"7º C",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12694' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12694' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12694' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12694&turmaNome=7º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12694&turmaNome=7º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12694&turmaNome=7º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12694&turmaNome=7º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12694' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12694' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12694' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12695,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"8º C",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12695' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12695' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12695' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12695&turmaNome=8º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12695&turmaNome=8º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12695&turmaNome=8º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12695&turmaNome=8º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12695' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12695' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12695' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12696,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"8º D",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12696' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12696' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12696' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12696&turmaNome=8º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12696&turmaNome=8º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12696&turmaNome=8º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12696&turmaNome=8º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12696' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12696' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12696' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12697,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"9º C",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12697' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12697' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12697' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=12697&turmaNome=9º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=12697&turmaNome=9º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=12697&turmaNome=9º C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=12697&turmaNome=9º C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=12697' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12697' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12697' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":16778,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"7º D",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/16778' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/16778' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/16778' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=16778&turmaNome=7º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=16778&turmaNome=7º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=16778&turmaNome=7º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=16778&turmaNome=7º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=16778' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/16778' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/16778' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":16779,
#          "Unidade":"E M Celestino Filho",
#          "Turma":"9º D",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/16779' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/16779' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/16779' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=421&turmaId=16779&turmaNome=9º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=421&turmaId=16779&turmaNome=9º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=421&turmaId=16779&turmaNome=9º D' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=421&turmaId=16779&turmaNome=9º D' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=421&IdTurma=16779' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/16779' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/16779' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12666,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"1º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12666' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12666' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12666' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12666&turmaNome=1º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12666&turmaNome=1º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12666&turmaNome=1º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12666&turmaNome=1º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12666' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12666' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12666' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12667,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"1º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12667' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12667' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12667' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12667&turmaNome=1º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12667&turmaNome=1º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12667&turmaNome=1º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12667&turmaNome=1º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12667' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12667' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12667' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12668,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"2º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12668' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12668' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12668' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12668&turmaNome=2º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12668&turmaNome=2º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12668&turmaNome=2º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12668&turmaNome=2º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12668' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12668' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12668' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12669,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"2º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12669' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12669' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12669' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12669&turmaNome=2º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12669&turmaNome=2º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12669&turmaNome=2º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12669&turmaNome=2º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12669' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12669' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12669' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12670,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"3º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12670' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12670' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12670' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12670&turmaNome=3º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12670&turmaNome=3º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12670&turmaNome=3º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12670&turmaNome=3º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12670' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12670' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12670' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12671,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"3º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12671' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12671' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12671' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12671&turmaNome=3º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12671&turmaNome=3º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12671&turmaNome=3º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12671&turmaNome=3º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12671' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12671' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12671' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12672,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"4º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12672' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12672' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12672' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12672&turmaNome=4º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12672&turmaNome=4º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12672&turmaNome=4º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12672&turmaNome=4º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12672' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12672' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12672' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12673,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"4º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12673' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12673' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12673' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12673&turmaNome=4º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12673&turmaNome=4º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12673&turmaNome=4º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12673&turmaNome=4º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12673' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12673' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12673' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12674,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"6º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12674' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12674' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12674' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12674&turmaNome=6º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12674&turmaNome=6º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12674&turmaNome=6º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12674&turmaNome=6º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12674' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12674' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12674' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12675,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"6º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12675' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12675' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12675' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12675&turmaNome=6º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12675&turmaNome=6º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12675&turmaNome=6º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12675&turmaNome=6º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12675' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12675' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12675' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12676,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"7º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12676' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12676' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12676' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12676&turmaNome=7º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12676&turmaNome=7º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12676&turmaNome=7º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12676&turmaNome=7º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12676' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12676' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12676' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12677,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"7º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12677' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12677' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12677' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12677&turmaNome=7º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12677&turmaNome=7º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12677&turmaNome=7º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12677&turmaNome=7º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12677' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12677' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12677' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12678,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"8º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12678' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12678' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12678' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12678&turmaNome=8º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12678&turmaNome=8º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12678&turmaNome=8º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12678&turmaNome=8º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12678' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12678' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12678' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12679,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"8º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12679' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12679' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12679' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12679&turmaNome=8º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12679&turmaNome=8º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12679&turmaNome=8º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12679&turmaNome=8º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12679' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12679' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12679' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12680,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"9º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12680' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12680' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12680' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12680&turmaNome=9º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12680&turmaNome=9º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12680&turmaNome=9º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12680&turmaNome=9º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12680' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12680' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12680' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12681,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"5º ANO B",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12681' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12681' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12681' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12681&turmaNome=5º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12681&turmaNome=5º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12681&turmaNome=5º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12681&turmaNome=5º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12681' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12681' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12681' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12682,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"5º ANO A",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12682' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12682' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12682' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12682&turmaNome=5º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12682&turmaNome=5º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12682&turmaNome=5º ANO A' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12682&turmaNome=5º ANO A' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12682' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12682' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12682' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"6º ANO C",
#          "AnoInicio":2022,
#          "AnoFim":2022,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12683' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12683' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12683' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12683&turmaNome=6º ANO C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12683&turmaNome=6º ANO C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12683&turmaNome=6º ANO C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12683&turmaNome=6º ANO C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12683' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12683' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12683' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":12684,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"JARDIM II",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/12684' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/12684' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/12684' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=12684&turmaNome=JARDIM II' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=12684&turmaNome=JARDIM II' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=12684&turmaNome=JARDIM II' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=12684&turmaNome=JARDIM II' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=12684' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/12684' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/12684' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":16780,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"9º ANO B",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/16780' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/16780' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/16780' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=16780&turmaNome=9º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=16780&turmaNome=9º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=16780&turmaNome=9º ANO B' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=16780&turmaNome=9º ANO B' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=16780' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/16780' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/16780' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       },
#       {
#          "Id":16781,
#          "Unidade":"E M Eudóxio de Figueiredo",
#          "Turma":"5º ANO C",
#          "AnoInicio":2023,
#          "AnoFim":2023,
#          "Ativo":"Ativo",
#          "Opcoes":"<a href='/Turma/Details/16781' data-toggle='tooltip' class='btn btn-info btn-circle btn-icon la la-folder kt-font-size-1-8rem' title='Detalhes'></a>\r\n                             <a href='/Turma/Edit/16781' data-toggle='tooltip' class='btn btn-success btn-circle btn-icon la la-pencil kt-font-size-1-8rem' title='Editar'></a>\r\n                             <a href='/Turma/Delete/16781' data-toggle='tooltip' class='btn btn-danger btn-circle btn-icon la la-trash kt-font-size-1-8rem' title='Apagar'></a>\r\n                             <a href='/Turma/FuncionarioTurma?idUnidade=422&turmaId=16781&turmaNome=5º ANO C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-share-alt kt-font-size-1-8rem' title='Vínculo Funcionários'></a>\r\n                             <a href='/Turma/AlunoTurma?idUnidade=422&turmaId=16781&turmaNome=5º ANO C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-user-plus kt-font-size-1-8rem' title='Vínculo Aluno'></a>\r\n                             <a href='/Turma/AtividadeTurma?idUnidade=422&turmaId=16781&turmaNome=5º ANO C' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-group kt-font-size-1-8rem' title='Vínculo Atividade'></a>\r\n                             <a href='/Turma/SalaTurma?idUnidade=422&turmaId=16781&turmaNome=5º ANO C' data-toggle='tooltip' class='btn btn-primary btn-circle btn-icon la la-connectdevelop kt-font-size-1-8rem' title='Vínculo Sala Turma'></a>\r\n                             <a href='/Turma/TurmaAlunos?idUnidade=422&IdTurma=16781' data-toggle='tooltip' class='btn btn-warning btn-circle btn-icon la la-random kt-font-size-1-8rem' title='Reenturmar aluno'></a>\r\n                             <a href='/Turma/LimparProcessos/16781' data-toggle='tooltip' class='btn btn-dark btn-circle btn-icon la la-times-circle kt-font-size-1-8rem' title='Limpar Processos'></a>\r\n                             <a href='/Turma/Reprocessar/16781' data-toggle='tooltip' class='btn btn-reciclar btn-circle btn-icon la la-refresh kt-font-size-1-8rem' title='Reprocessar'></a>",
#          "IdUnidade":0
#       }
#    ],
#    "refresh":False
# }
# classessJsonData =classessJson["data"]
#
# enrollClass = next((studentClass for studentClass in classessJsonData if studentClass["Turma"] == "9º D"),None)

def work_log(work_data):
   print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
   sleep(int(work_data[1]))
   print(" Process %s Finished." % work_data[0])

@timer
def measuringForeach(myList):
   for item in myList:
      work_log(item)

@timer
def callMultiprocess(myList):
   processPool = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())
   for process in processPool.map(work_log, myList):
      work_log(process)


@timer
def otherWay(myList):
   processPool = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())
   processPool.map(work_log, myList,chunksize=multiprocessing.cpu_count()*4)





randList = [[random.choice(string.ascii_uppercase),random.randint(1,2)] for i in range(1000)]
randList.sort()

#print("Starting foreach")
#measuringForeach(randList)
#sleep(5)

#print("Starting multiprocessing")
otherWay(randList)



