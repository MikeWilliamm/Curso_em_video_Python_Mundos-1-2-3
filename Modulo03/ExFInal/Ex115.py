import modulo
from Arquivo import *
from time import sleep

arq = r'C:\Users\lucas\Desktop\Mike\python\Curso Guanabara\Modulo03\ExFInal\Arquivo\registros.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso.')
else: 
    print('Arquivo não encontrado.')
    criarArquivo(arq)

while True:
    modulo.menu(['Ver pessoas cadastradas.', 'Cadastrar nova pessoa.', 'Sair do sistema.'])
    resp = modulo.leiaINT()
    
    if resp == 1:
        modulo.cabecalho('OPÇÃO 1')
        lerArquivo(arq)
    elif resp == 2:
        modulo.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = modulo.leiaINT(True)
        escreveNoArquivo(arq, nome, idade)
    elif resp == 3:
        modulo.cabecalho('\033[;1mSaindo do sistema... Até logo!.\033[m')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção valida!\033[m')
        
    sleep(2)