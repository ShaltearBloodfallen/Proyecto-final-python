# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    def nombre():
        n = input("Digite el numero por el cual desea multiplicar")
        name = "Franklin " * n
        print name
        
    def suma():
        n = input("Digite el numero")
        t = 0
        i = 0
        while i <= n:
            t = t + i
            i = i + 1
        print "el resultado de la suma es: ",t
        
    def imp():
        n = 0 
        while n <20:
            n = n + 1
            if n % 2 != 0:
              print n
              
   
    
    def impd():
        n = 20 
        while n > 0:
            n = n - 1
            if n % 2 != 0:
              print n
        
    
            
    def media():
        n1 = float(input("inserte el primer numero"))
        n2 = float(input ("inserte el segundo valor"))
        media2 = (2/(1/n1 + 1/n2))
        print media2
        
    
    
    def division():
        n = int(input("Digite un numero para buscar divisores perfectos"))
        if n > 0:
            print "El parametro introducido no es aceptable"
        
        for nt in range(1,n+1):
            if n % nt == 0:
             print nt
    
    def suma_sucesiva():
        producto = int(0)
        n1 = int(input("Ingrese el primer numero"))
        n2 = int(input("Ingrese el segundo numero"))
        if (n1 or n2 > 0):
            while n2 != 0:
            producto = producto + n1
            n2 = n2 - 1

            print("El producto es: " + str(producto))
        else:
            print("Los paramentros no son aceptables")
        
    
        
    def fibR(n):
        if n==1 or n==2:
            return 1
          return fibR(n-1)+fibR(n-2)

    print(fibR(1))
    print(fibR(2))
    print(fibR(3))
    print(fibR(4))
    print(fibR(5))
    print(fibR(6))
    print(fibR(7))
    print(fibR(8))
    print(fibR(9))
    print(fibR(10))
    print(fibR(11))
    print(fibR(12)) 
    
    def cinco_operaciones():
        n1 = int(input("Digite un valor"))
        n2 = int(input("Digite un valor"))
        n3 = int(input("Digite un valor"))
        n4 = int(input("Digite un valor"))
        n5 = int(input("Digite un valor"))
        n6 = int(input("Digite un valor"))
        n7 = int(input("Digite un valor"))
        n8 = int(input("Digite un valor"))
        n9 = int(input("Digite un valor"))
        n10 = int(input("Digite un valor"))

        suma = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
        sumacuadrados = (n1**2)+(n2**2)+(n3**2)+(n4**2)+(n5**2)+(n6**2)+(n7**2)+(n8**2)+(n9**2)+(n10**2)
        promedio = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)/10
        maximo =max(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)
        minimo =min(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)

        print("La suma de los numeros es: "+str(suma))
        print("La suma de los cuadrados de cada numero es: "+str(sumacuadrados))
        print("El promedio de los numeros es: "+str(promedio))
        print ("El valor maximo es: "+str(maximo))
        print("El valor minimo es: " + str(minimo))
        
    def resta_sucesiva():
        i = int(0)
        dividendo = int(input("Favor ingresar dividendo"))
        divisor = int(input("Favor ingresar el dividendo"))
        dividendo = dividendo - divisor

        while (dividendo >= 0):
            i = i + 1
            dividendo = dividendo - divisor

        print("La division por resta sucesiva es igual a: " + str(i)) 
        
    def salario():
        horas = int(input("Ingrese el numero de horas trabajadas"))
        salario = int(input("Ingerese el salario por hora"))
        salario_bruto = horas * salario
        print("Su salario bruto es: "+ str(salario_bruto))

        if (horas > 40):
            salario_bruto = ((1.5 * salario)* horas)
            print("Su salario bruto con horas extras es: "+str(salario_bruto))


        if salario_bruto <= 1100:
            print("Se le aplicara un 10% de retencion")
            salario_neto = salario_bruto - (salario_bruto*0.10)
            print("El salario neto es: "+str(salario_neto))

        elif salario_bruto >=1100 and salario_bruto <= 2600:
            print("Se le aplicara un 15% de retencion")
            salario_neto = salario_bruto - (salario_bruto * 0.15)
            print("El salario neto es: " + str(salario_neto))

        elif salario_bruto > 2600:
            print("Se le aplicara un 25% de retencion")
            salario_neto = salario_bruto - (salario_bruto * 0.25)
            print("El salario neto es: " + str(salario_neto))    
    
    import math
    def eqcuad(a,b,c):
        a = float(input("Ingerese el valor de a"))
        b = float(input("Ingrese el valor de b"))
        c = float(input("Ingrese el valor de c"))


        if a != 0:
            x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            print("Soluciones de la ecuacion: x1=%4.3f y x2=%4.3f " % (x1, x2))


        elif b != 0:
            x = -c / b
            print("Solucion de la ecuacion: x=%4.3f " % x)




        elif c != 0:
            print("La ecuacion no tiene solucion.")




        else:
            print("La ecuacion tiene infinitas soluciones. ")

    r = float(input("Ingrese el valor del radio"))
    def calcarea():

    area = 3.14*(r**2)
    print("El area del circulo es: "+str(area))

    def calcularcirc():
        longitud = float((2*3.14)*r)
        print("La longitud del circulo es: "+str(longitud))

    calcarea()
    calcularcirc()



    
    
    
    


        
   