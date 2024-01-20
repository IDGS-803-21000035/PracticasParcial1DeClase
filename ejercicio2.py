
class ejercicio2:
    'Declaracion de propiedades de clase'
    num = 0
    
    'Declaración de propiedades de clase'
    def __init__(self, a):
        self.num = a
        

    'Declaracion de propiedades de métodos'
    'Si la función está dentro de la clase poner self'
    def lista(self):      
        lista = [] 
        pares = []
        impares = []

        for n in range(self.num):
            numeros = int(input('Ingresa el numero '))
            lista.append(numeros)
            #print(lista)
            
        lista.sort()
        print("ordenados: ", lista)

        for n in lista:
            if self.par(n):
                pares.append(n)
            else:
                impares.append(n)

        print("pares:", pares)
        print("impares:", impares)

        noRepetido = set(lista)

        for n in noRepetido:
            num = lista.count(n)
            
            if num != 1:
                print("El {} se repite: {}".format(n,num))

            
    def par(self, n):
        return n % 2 == 0
        
        '''self.comprobarLista(lista)
            
    def par(self, n):
        return n % 2 == 0

    def comprobarLista(self, lista):
        for n in lista:
            if not self.par(n):
                return False
        return print('cierto')'''

'No forma parte de la clase'
def main():
    obj = ejercicio2(int(input("¿Cuántos números quieres ingresar?: ")))


    'referencia a la operación'
    obj.lista()

if __name__ == "__main__":
    main()
