def arquivoExiste(nome): #Verifica se um arquivo de texto existe tentando abrilo 
    
    try:
        a = open(nome, 'rt') #Tenta abrir o arquivo com 'rt' modo de leitura read text
        a.close()
    except FileNotFoundError: #Se der problema em abrir ou fechar o arquivo retorna False
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt = write text = escreve um arquivo de texto, o '+' é para caso não existir ele criar o arquivo
        a.close()
        
    except Exception as erro:
        print('Houve um erro na criação do arquivo!')
        print(f'ERRO: {erro}')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt') #abrindo o arquivo como leitura de arquivo texto
    except:
        print('Erro ao ler o arquivo!!!')
    else:
        print('-'*42)
        print('CADASTRO DE PESSOAS'.center(42))
        print('-'*42)

        for linha in a:
            dado = linha.split(';') #separa nome e idade em uma lista
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def escreveNoArquivo(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at') # at = append text, incluira coisas no arquivo com append
    except:
        print('ERRO ao tentar abrir o arquivo')
    else:
        try:
            a.write(f'{str(nome).capitalize()};{idade}\n') #Escreve dentro do arquivo
        except Exception as erro:
            print('Houve um erro ao tentar escrever os dados.')
            print(f'ERRO: {erro}')
        else:
            print(f'Novo registro de {nome} adicionado.')
        finally:
            a.close()