import modulo_triangulo

base = float(input("Digite o valor da area:"))
altura = float(input("Digite o valor da altura:"))

print(" ")

valor_area = modulo_triangulo.calculo_triangulo(base,altura)

print("O valor da area do triangulo escolhido é:",valor_area)
