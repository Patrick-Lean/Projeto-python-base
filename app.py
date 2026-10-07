import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza suprema','categoria':'Italiano','ativo':True},
                {'nome':'Cantina','categoria':'Italiano','ativo':False}
                ]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_op():
    '''
    Exibe as operações que o programa faz.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def cadastrar_novo_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante.

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo resturante na lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes \n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}:  ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_do_restaurante,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso \n')
    voltar_ao_menu()

def listar_restaurantes():
    '''
    Exibe os resturantes armazenados na lista
    '''
    exibir_subtitulo('Lista de restaurantes \n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'  {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
        
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    print('\n')
    voltar_ao_menu()

def voltar_ao_menu():
    '''
    A função retorna o programa para o menu.
    '''
    input('Digite uma tecla para voltar ao menu principal ')
    main()

def alternar_estado_do_restaurante():
    '''
    A função altera o estado do restaurante para ativo ou desativado

    Input:
    - Nome do restaurante

    Output:
    - Muda o status do restaurante

    '''
    exibir_subtitulo('Alterando estado do restaurante \n')
    nome_do_restaurante = input('Digite o nome do restaurante para alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso \n' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso \n'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    '''
    Exibe um texto embelezador no terminal
    '''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcoes():
    '''
    A função pede uma entrada e retorna a função que representa aquela entrada.
    '''
    try:
        #O valor armazenado na variável abaixo era uma str. Utilizando o int(), o input é forçado a pegar um intero. 
        opcao_escolhida=int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    
    #os.system('clear')#Usando a biblioteca os e chamando a função system, a limpeza da to terminal é possivel.
    #print('Finalizando o app')
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    print('Opção inválida! \n')
    voltar_ao_menu()
    
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_op()
    escolher_opcoes()


if __name__ == '__main__' :
    main()