#Lançamento de foguete.!!!
#O que fazer: Faça um programa que exiba uma contagem regressiva 
#para o lançamento de um foguete, indo de 10 até 0, 
#e termine exibindo a mensagem: "BUM! Decolar!".
#Foco: Lembrar de diminuir 1 a cada rodada (contador -= 1).

contador = 10

while contador >= 0:
    print(contador)
    contador = contador - 1 

print("BUM! Decolar!")

#-----------------------------------------------------------

#Crie um programa que fique pedindo números para o usuário. 
# Ele deve somar todos os números digitados. 
# O programa só para de pedir números quando o usuário digitar o número 0. 
# No final, mostre a soma total.
#Foco: O while deve continuar rodando enquanto o número digitado for diferente de zero (while numero != 0:).


contagem = 0 

numero = int(input('Digite um valor:'))

while numero != 0:
    contagem = contagem + numero
    numero = int(input("Digite outro valor:"))

print(f"A soma de todos os numeros digitados é {contagem}")
print("FIM!!!")

#-----------------------------------------------------------------

# O Nome não pode ter menos que 3 letras.
# A Idade tem que estar entre 0 e 120 anos.
# Se o usuário digitar um nome curto demais ou uma idade impossível, 
# o programa deve exibir uma mensagem de erro e pedir os dados novamente, 
# até que tudo esteja correto.

nome = input("Digite um nome: (mínimo 3 letras) ")
idade = int(input("Digite uma idade entre 0 a 120"))

while len(nome) < 3 or idade < 0 or idade > 120:
    print('Erro, nome curto demais ou idade fora do padrão estipulado.')
    
    nome = input("Digite um nome: (mínimo 3 letras) ")
    idade = int(input("Digite uma idade entre 0 a 120"))


print('Cadastro realizado com sucesso')

#-----------------------------------------------------------------------

#Defina um número secreto (ex: numero_secreto = 42).
#Crie uma variável para controlar as chances: tentativas = 3.
#Use o while True: para iniciar o jogo.
#Dentro do loop, peça o palpite do usuário e gaste uma tentativa (tentativas -= 1).
#Se o palpite for igual ao número secreto, dê os parabéns e pare o programa usando a palavra-chave break.
#Se o palpite estiver errado, diga se o número secreto é maior ou menor que o palpite dele.
#Se as tentativas chegarem a 0, 2use o break para encerrar o jogo e diga que ele perdeu.

numero_secreto = 42
tentativas = 3

print("=== JOGO DE ADIVINHAÇÃO === ")
print(f'Você tem {tentativas} tentativas para acertar o número secreto:')

while True:
    palpites = int(input('Digite o valor do seu palpite:'))
    tentativas = tentativas - 1

    if palpites == numero_secreto:
        print("Meus parabéns, você acertou!!!")
        break

    if tentativas == 0:
        print("Game over, suas chances acabaram!")
        break


    if palpites < numero_secreto:
        print(f"Seu palpite de {palpites} é menor que o número secreto")
    
    else:
        print(f'Seu palpite de {palpites} é maior que o número secreto')

