vocales = ['a', 'e', 'i', 'o', 'u',
           'á', 'é', 'í', 'ó', 'ú',
           'A', 'E', 'I', 'O', 'U',
           'Á', 'É', 'Í', 'Ó', 'Ú',
           'ü', 'Ü']

texto = input('Introduce un texto > ')

total = 0
for car in texto:
  if car in vocales:
     total += 1

print(f'El texto contiene {total} vocales')
