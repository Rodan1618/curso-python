#Operadores de Comparações
# = Um ingual é atribição
# == Dois iguais é uma comparação Booleano -- True ou False
#!= Exclamação e igual, busca se uma diferença. Se for diferente é True, se for igual é False
#<>
#>=
#=<

# print(2==3)
# print(7==7)

# x=8
# y=5
# print(x == y) #False
# print(x != y) #True
# print(x > y) #False
# print(x < y) #True
# print(x <= y) #True
# print(x >= y) #False

# x = "doce"
# y = "chocolate"
# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x <= y)
# print(x >= y)

#LEXICOGRAFIA
# x = "ab"
# y = "ac"
# print(x > y)
# print(x < y)
# print(len(x)) #len... faz a STR virar Numero
# print(len(y))

# a = len("chocolate") #len transforama uma srt (string) em int (número), conta as letras da palavras e transforma em número
# b = len("doce")
# print(a, b)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a <= b)
# print(a >= b)

#proceço de decisão em um softwer (if e else)

#Parte 3 — Operadores Lógicos
# idade = 20
# tem_carteira = True
# #AND: Ambas as condições precisam ser verdadeiras
# print(idade >= 18 and tem_carteira)
# #OR: Uma das Condições precisa ser verdadeira
# print(idade >= 18 or tem_carteira)
# #NOT: Inverte um valor
# print(not tem_carteira)

# idade = 10
# tem_carteira = True
# #AND: Ambas as condições precisam ser verdadeiras
# print("and: ", idade >= 18 and tem_carteira)
# #OR: Uma das Condições precisa ser verdadeira
# print("or: ", idade >= 18 or tem_carteira)
# #NOT: Inverte um valor (Contrário do que está propondo)
# print("not: ", not tem_carteira)

#Parte 4 — Condicionais (if, elif, else)
#Condicionais
# nota = 4

# if nota >= 7: #false
#     print("Aprovado") # BLOCO de código do if 
#     print("Aprovado") # BLOCO de código do if 
#     print("Aprovado") # BLOCO de código do if 
#     #if: O if Precisa de uma Verdade (True) para funcionar. if é o GUARDIÃO do Código
#     #if = SE
# elif nota >= 5:
#     print("recuperação")
# else: #Else = Se não
#     print("reprovado") 
# print(";p")


# note = float(input("digite sua nota: ")) #Aqui tem um Bug
# print(type(note))
# if note >= 7: #false
#     print("Aprovado")
# elif note >= 5:
#     print("recuperação")
# else:
#     print("reprovado") 

# numero = int(input("Digite um numero: "))
# print(numero * 2)

print("=== Mini Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Mutiplicação")
print("4 - Divisão")

operacao = input("Escolha uma operação (1 a 4)")
numero_1 = float(input("Digite o primeiro número"))
