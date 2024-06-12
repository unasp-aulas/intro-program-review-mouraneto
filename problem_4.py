valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não altera


# 
while True:
  valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
  salario = float(input("Qual é o salário? "))  # Não alterar
  anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar


  prestacao = valor_casa / (anos_pagar * 12)
  if prestacao < salario * 0.30:
    print("Aprovado")
    break
  else:
    print('Reprovado')
    break

