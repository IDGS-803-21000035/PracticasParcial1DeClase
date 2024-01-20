class ejercicio1:
    'Declaracion de propiedades de clase'
    num1 = 0

    'Declaracion de propiedades de constructor'
    def __init__(self, a):
        self.num1 = a
        
    'Declaracion de propiedades de métodos'
    'Si la función está dentro de la clase poner self'
    def piramide(self):
        i = 1  
        while i <= self.num1:
            print('*' * i)
            i += 1            

'No forma parte de la clase'
def main():
    obj = ejercicio1(int(input("Dame un número: ")))

    'referencia a la operación'
    obj.piramide()

if __name__ == "__main__":
    main()
