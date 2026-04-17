#Vista de prova.
#Exercicio 01:

#1. Resolver o exercício 31, gravando todos os valores num arquivo. Deve-se fazer um procedimento
#para gravação e caso o arquivo já exista, ele deve ser descartado e gravado do início novamente

#Algoritmo Lt01.31.

import os;

def main():

   quadrado()

#Fim.

def quadrado():

   #Declarar variáveis locais.
   num : int = 0
   quadrado : int = 0

   print("Quadrado dos números entre 10 e 150: ")

   for num in range(11, 150):
      quadrado = num**2
      print(quadrado)
      escreveArq(quadrado, num)

   #Fim-para;

#Fim-segue.

def escreveArq(q, cont):

    #Variaveis locais:
    dir : str = ''
    arq : str = ''
    txt : str = ''
    linha : str = ''
    file: str = ''
    tipo: str = ''
    enc: str = ''

    dir = '/tmp/exercicios/'
    arq = 'ex31.txt'

    if not (os.path.exists(dir)):
        #Criando o diretorio.
        os.mkdir(dir)
        os.makedirs(dir, exist_ok = True)
        os.chmod(dir, 0o744) #Autorizacao de criacao, leitura e alteracao para o primeiro usuario, leitura para os demais.

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        txt = dir + arq
        enc = 'utf-8'
        linha = str(q)+'\n'

        if (os.path.exists(txt)) and (cont != 11):
            tipo = 'a'

        with open (txt, tipo, encoding=enc) as file:
            file.write(linha)

    else:
        print("Diretorio invalido")

    #Fim-se.
#Fim-segue.

if __name__ == '__main__':
   main()
#Fim-se.