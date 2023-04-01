
#name = str(input("Ingrese nombre: "))
#password = str(input("Ingrese contraseña: "))

def login():
    intentos = 0
    while True:
        name = input("Ingrese nombre: ")
        password = input("Ingrese contraseña: ")
        if (name == "admin" and password == "admin123*"):
            print("Access")
            break
        else:
            intentos +=1
            print(f'Access deneged, Your number of attempts is: {intentos}')
            
login()


            



