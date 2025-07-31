class Menu:
    def mcd(self, a, b):
        if b == 0:
            return 0
        else:
            return self.mcd(b, a % b)

    def palabraencadena(self, r):
        if r =="":
            return 0
        else:
            if r[0] == "":
             return 1
            else:
                self.palabraencadena(r[1:])
        return 1 + self.palabraencadena(r[1:])

    def calcudigi(self,n):
        if n == 0:
            return 0
        else:
            return n[-1] + self.calcudigi(n[-1])

    def cadenarepetida(self,n):
        if n == 0:
            return 1
        else:
            return n * self.cadenarepetida(n)


class menu:
    def __init__(self):
        self.prueba = Menu()
    def mostrar(self):
     while True:
      print("MENU")
      print("1.Calcular Mcd")
      print("2.Repetir una palabra")
      print("3.repetir palabras")
      print("4.convertir decimal a binario")
      print("5.calcular cuantos digitos tiene un numero")
      print("6.SALIR")

      op = int(input("Ingresa una opcion: "))

      if op == 1:
       t = int(input("Ingresa un numero: "))
       r = int(input("Ingresa otro numero: "))
       resultado = self.prueba.mcd(t,r)
       print(f"la respuesta es {resultado}")

      if op == 2:
       palabras = int(input("Ingresa una palabra: "))
       print(f"la palabra es {self.prueba.palabraencadena(palabras)}")

      if op == 3:
          n = input("Ingrese un texto: ")

      if op == 4:
          print("wena noche")

      if op == 5:
         dato = int(input("Ingrese el numero para calcular sus digitos: "))


      if op == 6:
          print("Hasta que nos volvamos a ver")

menu = menu()
menu.mostrar()