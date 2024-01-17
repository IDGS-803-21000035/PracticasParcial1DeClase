class ejercicio1:
    'Declaracion de propiedades de clase'
    num1 = 0

    'Declaracion de propiedades de constructor'
    def __init__(self, a):
        self.num1 = a
        
    'Declaracion de propiedades de métodso'
    'Si la funcuion esta dentro de la clase poner self'
    def piramide(self):

        while self.num1 > 0:
            print(self.num1)
            self.num1 -= 1
        

'No forma parte de la clase'
def main():
    obj = ejercicio1(int(input("Dame un número: ")))

    'referencia a la operacopm'
    obj.piramide()

if __name__ == "__main__":
    main()