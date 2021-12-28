from typing import Match
import pandas as pd
import psycopg2
import time
def conexao():
    connection_data = psycopg2.connect(host = 'localhost', database = 'testedb', user = 'postgres', password = '154878', port = 5432) 

    cur = connection_data.cursor() 
    return connection_data, cur
def registra():
    connection_data, cur = conexao()

    while True:
        lista = []
        aux = []
        contador = 0

        aux.append(contador)
        aux.append(str(input('Nome: ')))
        aux.append(float(input('Nota 1: ')))
        aux.append(float(input('Nota 2: ')))

        lista.append(aux[:])
        aux.clear()

        resp = int(input('[1] registrar um novo boletim \n[2] Inserir os registro digitados no DB\nOpção: '))
        while resp != 1 and resp != 2:
            print('Digito errado!!!')
            resp = int(input('[1] registrar um novo boletim \n[2] Inserir os registro digitados no DB\nOpção: '))
        
        if resp == 2:
            break
        else:
            contador+=1

    print('-='*30)
    print('Inserindo dados no DB...')
    print('-='*30)
    print(f'{"No.":<4}{"Nome":<10}{"Média":>10}')
    print('-'*24)
    for p in lista:
        print(f'{p[0]:<4}{p[1]:<10}{(p[2] + p[3])/2:>10}')
    print('-='*30)

    # df = pd.DataFrame(lista, columns= ['id', 'nome', 'nota1', 'nota2'])
    # print(df)


    
    time.sleep(0.5)
    for p in lista:
        sql = f"INSERT INTO boletim (id, nome, nota1, nota2)  VALUES ('{p[0]}', '{p[1]}', {p[2]}, {p[3]});" + ' '
            
        cur.execute(sql)
        connection_data.commit()
    print("Dados inseridos no DB com SUCESSO!")

def visualiza():
    connection_data, cur = conexao()

    sql = f"select * from boletim"
    # while True:
    #     id = int(input('Deseja ver as notas de qual aluno? [ID] '))

    #     contador = verificar = 0
    #     for i in lista:
    #         if i[0] == id:
    #             print(f'As notas do {i[1]} são {i[2]} e {i[3]}')
    #             verificar = 1
    #         elif contador == len(lista)-1 and verificar == 0:
    #             print('ID invalido!!!')
    #         contador += 1
        
    #     resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    #     while resp != 'S' and resp != 'N':
    #         print('Digito errado!!!')
    #         resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
            
        
def main():
    print(f'{"-="*10:<10} SISTEMA ESCOLAR {"=-"*10:>10}')
    resp = int(input('''[1] Registra alunos e notas.
[2]Visualizar registros.
Opção: '''))
    if resp == 1:
        registra()

main()