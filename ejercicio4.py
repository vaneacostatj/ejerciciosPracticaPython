

ancho = int(input('٩(˘◡˘)۶ Ingrese el ancho del rectangulo: '))
largo = int(input('٩(˘◡˘)۶ Ingrese la altura del rectangulo: '))

area = lambda itemAncho, itemLargo:  itemAncho * itemLargo
perimetro = lambda itemAncho, itemLargo:  2 * (itemAncho + itemLargo)

resultArea = area(ancho, largo)
resultPerimetro = perimetro(ancho, largo)

print(f'el area del rectangulo es {resultArea}')
print(f'el perimetro del rectangulo es {resultPerimetro}')

init = 0 

while init <= largo:
    print(' * ' * ancho)
    init += 1
