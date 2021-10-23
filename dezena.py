num = int(input("Digite um número inteiro: "))
a = num // 1 % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10

print ("O dígito da unidade é:", a)
print ("O dígito das dezenas é", b)
print ("O dígito da centena é", c)
print ("O dígio do milhar é", d)
