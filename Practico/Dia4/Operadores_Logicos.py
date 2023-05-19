#seria lo más facil
mi_bool =4 < 5 < 6
print(mi_bool)

#utilizamos el operador logico

mi_bool = 4 < 5 and 5 < 6
mi_bool2 = 4 < 5 and 5 > 6
print(mi_bool)
print(mi_bool2)

mi_bool = 4 < 5 and 5 == (2+3)
print(mi_bool)

mi_bool = 4 < 5 or 5 == 55
print(mi_bool)

texto ="esta frase es breve"
my_bool ='frase' in texto
print(my_bool)

my_bool =('frase' in texto) and ('python' in texto)
print(my_bool)

mi_bool = not ('a' == 'a')
print(mi_bool)

mi_bool = not ('a' != 'a')
print(mi_bool)

texto ="Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
mi_bool = not ('exito' in texto) and ('tecnología' in texto)
palabra1 ='exito'
palabra2 ='tecnología'
mi_bool2 =  not palabra1 in texto or palabra2 in texto
print(mi_bool2)