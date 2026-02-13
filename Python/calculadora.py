#Aluna 5 mini calculadoora
print("=== calculadora interativa ====")
print("escolhas as opções abaixo")
print("1 - soma")
print("2 - Subtração")
print("3 - Mutiplicação")
print("4 - Divisão")

operacao = input("Digite um número (1 a 4): ")
numero_um = float(input("Digite o primeiro número: "))
numero_dois = float(input("Digite o segundo número: "))

if operacao == "1": # pra todo if temos um elf
    print(numero_um + numero_dois)
elif operacao == "2":
    print(numero_um - numero_dois)
elif operacao == "3":
    print(numero_um * numero_dois)
elif operacao == "4":
    if numero_dois != 0:
        print(numero_um / numero_dois)
    else:
        print("operação invalida. número 0")
else:
    print("Opção inválida.")
       
