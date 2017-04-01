codigo1, numero1, valor1 = raw_input().split()
codigo2, numero2, valor2 = raw_input().split()

codigo1 = int(codigo1)
codigo2 = int(codigo2)
numero1 = int(numero1)
numero2 = int(numero2)
valor1 = float(valor1)
valor2 = float(valor2)

print "VALOR A PAGAR: R$ %.2f" %((numero1 * valor1) + (numero2 * valor2))
