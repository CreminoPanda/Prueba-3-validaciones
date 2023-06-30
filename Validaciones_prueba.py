
def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su Rut(Sin puntos ni digito verificador): "))
            if rut>=1000000 and rut<=99999999:
                return rut
            else:
                print("ERROR! DEBE INGRESAR UN RUT VALIDO ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_nombre():
    while True:
        nombre=input("Ingrese su nombre: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE VALIDO!")

def validar_s_nombre():
    while True:
        nombre2=input("Ingrese su segundo nombre: ")
        if len(nombre2.strip())>=3 and nombre2.isalpha():
            return nombre2
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE VALIDO!")

def validar_p_apellido():
    while True:
        apellido1=input("Ingrese su primer apellido: ")
        if len(apellido1.strip())>=3 and apellido1.isalpha():
            return apellido1
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE VALIDO!")

def validar_s_apellido():
    while True:
        apellido2=input("Ingrese su segundo apellido: ")
        if len(apellido2.strip())>=3 and apellido2.isalpha():
            return apellido2
        else:
            print("ERROR! DEBE INGRESAR UN NOMBRE VALIDO!")


def validar_correo():
    while True:
        correo=input("Ingrese su correo electronico: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INVALIDO, TIENE QUE INGRESAR UN CORREO QUE TENGA UN @!")


def validar_cantidad_personas():
    while True:
        try:
            cantidad=int(input("Ingrese cantidad de personas: "))
            if cantidad>=1 and cantidad<=99:
                return cantidad
            else:
                print("ERROR! DEBE INGRESAR UNA CANTIDAD ENTRE 1 PERSONA O 99!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_telefono():
    while True:
        try:
            telefono=int(input("Ingrese su número de telefono: "))
            telefono_str=str(telefono)
            if len(telefono_str)>=9:
                return telefono
            else:
                print("ERROR! DEBE INGRESAR UN NÚMERO DE TELEFONO CORRECTO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_opcion():
    while True:
        try:
            opcion=int(input("Ingrese la opción: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! DEBE INGRESAR UNA OPCIÓN VALIDA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")


def validar_genero():
    while True:
        genero=input("Ingrese su genero Masculino(M), Femenino(F), Otro(O): ")
        if genero.upper()=="M" or genero.upper()=="F" or genero.upper()=="O":
            return genero
        else:
            print("ERROR! DEBE INGRESAR UN GENERO ENTRE MASCULINO, FEMENINO U OTRO!")


            
