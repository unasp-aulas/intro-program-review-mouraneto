def main(cargo, valor):
  try:
      taxa = [1.15, 1.26, 1.34]
      valor = float(valor)

      if cargo == 'junior':
          resultado = (valor * taxa[0])
      elif cargo == 'pleno':
          resultado = (valor * taxa[1])
      elif cargo == 'senior':
          resultado = (valor * taxa[2])

      else:
         resultado = -1


      return resultado

  except:
      -1

#commit