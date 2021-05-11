def area(n1=0,n2=0):

    """
    Esta funcao calcula area de um retangulo
    """
    area = (n1*n2)
    print(f'A área de um terreno {n1} X {n2} é de {area}m²')



l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))

area(l,c)



help(area)


