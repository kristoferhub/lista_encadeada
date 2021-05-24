"""
Nome: Kristofer R.K
Trabalho sobre lista duplamente encadeada
Algoritimos 2.

"""

# Importando a classe LinkedList, classe na qual tem os métodos para manipulação da lista a ser criada.
from list import LinkedList

# ======================================================================================================================
# Testando

# Criando e adicionando elementos ao final da lista.
lista = LinkedList()
lista.append(7)
lista.append(80)
lista.append(56)
lista.append(32)

# Métodos da classe:

# Mostrar o elemento conforme o índice
#print(lista[2])
# Mostrar o índice conforme o elemento digitado
#print(lista.index(80))
# Inserindo elemento e tornando o primeiro.
#lista.insert(0, 98)

# Métodos para mostrar os elementos

# Lista na ordem normal
lista.get_lista()
print('\n')
# Lista na ordem inversa
lista.get_lista_inversa()
# ======================================================================================================================

# Função menu para administrar os métodos da class LinkedList
"""
def menu():
    lista = LinkedList()
    while True:
        print('\n')
        print(f'Criando sua Lista! \n'
              f'Digite 0 para finalizar o programa \n'
              f'Digite 1 para cadastrar elementos no final da sua lista \n'
              f'Digite 2 para descobrir o índice do elemento \n'
              f'Digite 3 para saber o elemento no seu índice \n'
              f'Digite 4 para inserir um elemento no índice da sua escolha \n'
              f'Digite 5 para modificar um elemento no índice selecionado \n'
              f'Digite 6 para listar todos os elementos da sua lista \n'
              f'Digite 7 para listar todos os elementos da sua lista só que na ordem inversa')
        try:
            r = int(input('Digite... '))
        except ValueError:
            print('O número digitado tem que ser um inteiro')
        if r == 0:
            break
        elif r == 1:
            print('\n')
            print('Cadastrando elementos no final da lista!')
            x = 'S'
            while x != 'N':
                s = input('Digite o elemento: ')
                lista.append(s)
                x = input('Digite S para continuar cadastrando ou N para finalizar o cadastro: ').upper()
        elif r == 2:
            print('\n')
            print('Descobrir o índice do elemento')
            k = input('Digite o elemento: ')
            print(f'Índice: {lista.index(k)}')

        elif r == 3:
            print('\n')
            while True:
                try:
                    print('Saber o elemento no seu índice')
                    k = int(input('Digite o índice: '))
                except ValueError:
                    print('O Índice deve ser um número inteiro')
                else:
                    print(f'O elemento é: {lista[k]}')
                    break
        elif r == 4:
            print('\n')
            while True:
                try:
                    print('Inserir um elemento no índice da sua escolha')
                    k = int(input('Digite o índice: '))
                except ValueError:
                    print('O Índice deve ser um número inteiro')
                else:
                    s = input('Digite o elemento: ')
                    lista.insert(k, s)
                    break
        elif r == 5:
            print('\n')
            print('Modificar um elemento no índice selecionado')

        elif r == 6:
            print('\n')
            print('Listar todos os elementos da sua lista')
            lista.get_lista()

        elif r == 7:
            print('\n')
            try:
                print('Listar todos os elementos da sua lista só que na ordem inversa')
                lista.get_lista_inversa()
            except AttributeError:
                pass


menu()
"""

