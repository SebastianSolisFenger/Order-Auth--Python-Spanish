USUARIO_PRIMER_NOMBRE = str()
USUARIO_APELLIDO = str()
USUARIO_CONTRASENA = str()

productos = [
    {
        "id": 0,
        "name": "hoodie",
        "price": 50,
    },
    {
        "id": 1,
        "name": "tshirt",
        "price": 25,
    },
    {
        "id": 2,
        "name": "cap",
        "price": 20,
    },
    {
        "id": 3,
        "name": "sneakers",
        "price": 100,
    },
    {
        "id": 4,
        "name": "socks",
        "price": 5,
    },
]


# ---</MAINPAGE>---


def mostrarPaginaPrincipal():
    while True:
        # AUTENTICACION
        # LEER ARCHIVO DE USUARIOS
        authArchivo = open("./autenticacion.txt", "r")
        autLineasArchivo = authArchivo.readlines()
        estaLogeado = autLineasArchivo[0].split(" ")[1].startswith("T")

        # CARRITO
        carritoArchivoCrud = open("./carrito.txt", "r+")

        productosEnCarritoCantidad = len(carritoArchivoCrud.readlines())

        print(
            "\n|================|-------|================|\n|================| SHOPPY |================|\n|==============|           |==============|"
        )

        if estaLogeado:
            nombreUsuario = autLineasArchivo[1].split(" ")[1].rstrip()
            print(
                f"|================| Bienvenido {nombreUsuario} |================|\n|================|           |================|"
            )
        else:
            print(
                "|================| Bienvenido, por favor inicie sesion O Seleccione una opcion |================|\n|================|           |================|"
            )

        print("1. Productos")

        if productosEnCarritoCantidad == 0:
            print("2. Carrito")
        else:
            print(f"2. Carrito ({productosEnCarritoCantidad})")

        if productosEnCarritoCantidad > 0:
            print("3. Ordenar")

        if estaLogeado == False and productosEnCarritoCantidad > 0:
            print("4. Registrarse")
            print("5. Iniciar Sesion")

        if estaLogeado == False and productosEnCarritoCantidad == 0:
            print("4. Registrarse")
            print("5. Iniciar Sesion")

        if estaLogeado and productosEnCarritoCantidad == 0:
            print("4. Cerrar Sesion")

        if estaLogeado and productosEnCarritoCantidad > 0:
            print("5. Cerrar Sesion")

        print("0. Salir")

        ## ---</MENU>---

        opcion = input("Seleccione una opcion >> ")

        if opcion == "1":
            mostrarProductos()
            return
        elif opcion == "2":
            mostrarCarrito()
            return
        elif opcion == "3":
            if productosEnCarritoCantidad == 0:
                if estaLogeado:
                    mostrarCerrarSesionPanel()
                    return
                else:
                    mostrarRegistrarsePanel()
                    return

            mostrarOrdenarPanel("LandingPage")

        elif opcion == "4":
            if estaLogeado:
                mostrarCerrarSesionPanel()
                return
            else:
                if productosEnCarritoCantidad == 0:
                    mostrarIniciarSesionPanel()
                    return
                else:
                    mostrarRegistrarsePanel()
                    return
        elif opcion == "5" and estaLogeado == False:
            mostrarIniciarSesionPanel()
            return
        elif opcion == "0":
            shutDown()
        else:
            print("\n[!] Ingresaste un caracter invalido")
            continue

        break

    # ---</MAINPAGE>---


# ---<EXIT>---
def shutDown():
    print("\n----------------------------------------")
    print("Hasta Luego!")
    print("----------------------------------------\n")
    exit()


# ---</EXIT>---


# ---<PRODUCTOS>---


def mostrarProductos():
    while True:
        print(
            "|================|-------|================|\n|================| SHOPPY |================|\n|==============|           |==============|"
        )
        print("\n----Productos----")
        print("+. Agregar producto")
        print("`. Atras")
        print("0. Salir")

        for i in range(len(productos)):
            print(f'|<>| {productos[i]["name"]} -> {productos[i]["price"]}$')

        opcion = input("Seleccione una opcion >> ")

        if opcion == "+":
            mostrarAgregarProductoPanel()
            return
        if opcion == "0":
            print("Nos vemos!")
            exit()
        elif opcion == "`":
            mostrarPaginaPrincipal()
            return
        else:
            print("\n[!] Ingresaste un caracter invalido")

    # ---</PRODUCTOS>---

    # ---<AGREGAR PRODUCTO>---


def mostrarAgregarProductoPanel():
    print("\n----Productos----")

    print("[1...] Agregar numero del producto para sumarlo al carrito")
    print("`. Atras")
    print("0. Salir")

    while True:
        for i in range(len(productos)):
            print(f'|{i + 1}| {productos[i]["name"]} -> {productos[i]["price"]}')

        opcion = input("Seleccione una opcion >> ")
        if opcion == "`":
            mostrarProductos()
            return
        if opcion == "0":
            print("Nos vemos!")
            shutDown()
        if int(opcion) > 0 and int(opcion) <= len(productos):
            carritoArchivoCrud = open("./carrito.txt", "r+")
            carritoArchivoLineas = carritoArchivoCrud.readlines()
            carritoArchivoLineas.insert(0, f'{productos[int(opcion) - 1]["name"]}\n')
            carritoArchivoCrud.seek(0)
            carritoArchivoCrud.writelines(carritoArchivoLineas)
            carritoArchivoCrud.close()

            print("\n[+] Producto agregado al carrito")
            mostrarPaginaPrincipal()
            return
        else:
            print("\n[!] Ingresaste un caracter invalido")

    # ---</REMOVER PRODUCTO>---


def mostrarRemoverProductoPanel():
    while True:
        carritoArchivoCrud = open("./carrito.txt", "r+")
        carritoArchivoLineas = carritoArchivoCrud.readlines()
        carritoArchivoLineasCantidad = len(carritoArchivoLineas)

        print("\n----Carrito----")

        print("[1...] Remover numero del producto para sumarlo al carrito")
        print("`. Atras")
        print("0. Salir")

        for i in range(carritoArchivoLineasCantidad):
            print(f"|{i + 1}| {carritoArchivoLineas[i].rstrip()}")

        opcion = input("Seleccione una opcion >> ")

        if int(opcion) > 0 and int(opcion) <= carritoArchivoLineasCantidad:
            carritoArhicvoLineasActualizado = (
                carritoArchivoLineas[: int(opcion) - 1]
                + carritoArchivoLineas[int(opcion) :]
            )
            carritoArchivoEscribir = open("./carrito.txt", "w")
            carritoArchivoEscribir.writelines(carritoArhicvoLineasActualizado)
            carritoArchivoEscribir.close()

            print("\n[+] Producto removido del carrito")
            continue
        elif opcion == "`":
            mostrarCarrito()
            return
        elif opcion == "0":
            print("Nos vemos!")
            shutDown()
        else:
            print("\n[!] Ingresaste un caracter invalido")
            continue


# ---</ CARRITO >---
def chequearCantidadTotalDeProductosEnCarrito():
    cantidadTotal = 0
    carritoArchivoLeer = open("./carrito.txt", "r")
    carritoArchivoLineas = carritoArchivoLeer.readlines()
    for line in carritoArchivoLineas:
        line = line.rstrip()
        cantidadTotal += chequearPrecioProducto(line)

    return cantidadTotal


def mostrarCarrito():
    while True:
        carritoArchivoCrud = open("./carrito.txt", "r+")
        carritoArchivoLineas = carritoArchivoCrud.readlines()
        carritoArchivoLineasCantidad = len(carritoArchivoLineas)

        print("\n----Carrito----")

        if carritoArchivoLineasCantidad != 0:
            print("1. Ordenar")
            print("-. Remover producto")

        print("`. Atras")
        print("0. Salir")

        if carritoArchivoLineasCantidad == 0:
            print("\n[!] Tu carrito esta vacio")

        if carritoArchivoLineasCantidad != 0:
            print("---- Productos en el carrito ----")
            for i in range(carritoArchivoLineasCantidad):
                print(f"<> {carritoArchivoLineas[i].rstrip()}")
            print(f"\nTotal: {chequearCantidadTotalDeProductosEnCarrito()}$")

        opcion = input("Seleccione una opcion >> ")

        if opcion == "0":
            print("Nos vemos!")
            shutDown()
        elif opcion == "`":
            mostrarPaginaPrincipal()
            return
        elif opcion == "1" and carritoArchivoLineasCantidad != 0:
            mostrarOrdenarPanel("carrito")
            return
        elif opcion == "-" and carritoArchivoLineasCantidad != 0:
            mostrarRemoverProductoPanel()
            return
        else:
            print("\n[!] Ingresaste un caracter invalido")


def chequearPrecioProducto(productoNombre):
    for producto in productos:
        if producto["name"] == productoNombre:
            return producto["price"]


#  </ CART >

#  < ORDENAR >


def mostrarOrdenarPanel(redireccionadoDesde):
    while True:
        print("\n----Ordenar----")
        print(f"Cantidad total: {chequearCantidadTotalDeProductosEnCarrito()}$")
        print("Estas seguro/a que quieres ordenar?")

        print("1. Ordenar")
        print("2. Cancelar")
        print("`. Atras")
        print("0. Salir")

        opcion = input("Seleccione una opcion >> ")

        if opcion == "1":
            # LIMPIAR CARRITO
            carritoArchivoEscribir = open("./carrito.txt", "w")
            carritoArchivoEscribir.writelines("")
            carritoArchivoEscribir.close()

            print("--------------------------------------")
            print("\n[+] Orden realizada con exito")
            print("Muchas gracias por su compra! Tu compra sera entregada en 3 dias")
            print("--------------------------------------\n")
            mostrarPaginaPrincipal()
            return
        elif opcion == "2" or "`":
            if redireccionadoDesde == "carrito":
                mostrarCarrito()
                return
            if redireccionadoDesde == "paginaPrincipal":
                mostrarPaginaPrincipal()
                return
        elif opcion == "0":
            print("Nos vemos!")
            shutDown()
        else:
            print("--------------------------------------")
            print("\n[!] Ingresaste un caracter invalido")
            print("--------------------------------------\n")

    #  </ ORDENAR >


def mostrarRegistrarsePanel():

    usuariosArchivoCrud = open("./users.txt", "r+")
    usuariosArchivoLineas = usuariosArchivoCrud.readlines()

    primerNombre = str()
    apellido = str()
    email = str()
    password = str()

    print("\n-----SignUp-----")
    print("`. Back")
    print("0. Exit")

    for i in range(4):
        while True:
            if i == 0:
                primerNombre = input("Enter first name >> ")

                if primerNombre == "`":
                    mostrarPaginaPrincipal()
                    return
                if primerNombre == "0":
                    shutDown()

                break
            elif i == 1:
                apellido = input("Enter last name >> ")

                if apellido == "`":
                    mostrarPaginaPrincipal()
                    return
                if apellido == "0":
                    shutDown()

                break
            elif i == 2:
                email = input("Enter email >> ")

                if email == "`":
                    mostrarPaginaPrincipal()
                    return
                if email.count("@") == 0 or email.count(".") == 0:
                    print("\n[!] Invalid email format. Try again.")
                    continue
                if email == "0":
                    shutDown()

                # check if email is not busy
                isEmailBusy = False
                for j in range(len(usuariosArchivoLineas)):
                    if usuariosArchivoLineas[j].startswith("user"):
                        if usuariosArchivoLineas[j + 3].split(" ")[1].rstrip() == email:
                            print("\n[!] This email is busy. Type another email.")
                            isEmailBusy = True
                            break

                if isEmailBusy:
                    continue
                else:
                    break
            else:
                password = input("Enter password >> ")

                if password == "`":
                    mostrarPaginaPrincipal()
                    return
                if password == "0":
                    shutDown()
                if len(password) < 5:
                    print("\n[!] Password has to be at least 7 characters long.")
                    continue

                break

    # check how many users are signed
    userCount = int()
    if len(usuariosArchivoLineas) == 0:
        userCount = 0
    else:
        userCount = (
            int(
                usuariosArchivoLineas[0].rstrip()[5 : len(usuariosArchivoLineas[0]) - 2]
            )
            + 1
        )

    usuariosArchivoLineas.insert(0, "----------------------------------------\n")
    usuariosArchivoLineas.insert(0, f"--password {password} \n")
    usuariosArchivoLineas.insert(0, f"--email {email}\n")
    usuariosArchivoLineas.insert(0, f"--lastName {apellido}\n")
    usuariosArchivoLineas.insert(0, f"--firstName {primerNombre}\n")
    usuariosArchivoLineas.insert(0, f"user[{userCount}]\n")

    usuariosArchivoCrud.seek(0)
    usuariosArchivoCrud.writelines(usuariosArchivoLineas)
    usuariosArchivoCrud.close()

    print("\n----------------------------------------")
    print("SUCCES")
    print("You've signed up. Now it's time to log in.")
    print("----------------------------------------\n")
    mostrarIniciarSesionPanel()


# INICIAR SECION PANEL
def mostrarIniciarSesionPanel():

    email = str()
    password = str()
    correctPassword = str()
    usuarioLineaIndiceEnUsuariosArchivo = int()

    print("\n----Iniciar Sesion----")
    print("`. Atras")
    print("0. Salir")

    for i in range(2):
        while True:
            if i == 0:
                email = input("Ingrese su email >> ")

                if email == "`":
                    mostrarPaginaPrincipal()
                    return
                if email == "0":
                    print("Nos vemos!")
                    shutDown()

                # BUSCANDO EMAIL EN LA BASE DE DATOS (EN USUARIOS.TXT)

                emailEncontrado = False

                usuariosArchivoLeer = open("./usuarios.txt", "r")
                usuariosArchivoLineas = usuariosArchivoLeer.readlines()

                for j in range(len(usuariosArchivoLineas)):
                    if usuariosArchivoLineas[j].startswith("--email"):
                        if usuariosArchivoLineas[j].rstrip().split(" ")[1] == email:
                            correctPassword = (
                                usuariosArchivoLineas[j + 1].rstrip().split(" ")[1]
                            )
                            emailEncontrado = True
                            usuarioLineaIndiceEnUsuariosArchivo = j - 3

                usuariosArchivoLeer.close()

                if emailEncontrado:
                    break
                else:
                    print("\n[!] Email no encontrado")
                    continue

            else:
                while True:
                    password = input("Ingrese su password >> ")

                    if password == "`":
                        mostrarPaginaPrincipal()
                        return
                    if password == "0":
                        print("Nos vemos!")
                        shutDown()

                    if password != correctPassword:
                        print("\n[!] Password incorrecto, intente de nuevo")
                        continue
                    else:
                        break

            # GUARDAR DATA SOBRE EL USUARIO LUEGO DE INICIAR SESION

            usuariosArchivoLeer = open("usuarios.txt", "r")
            usuariosArchivoLineas = usuariosArchivoLeer.readlines()

            USUARIO_PRIMER_NOMBRE = (
                usuariosArchivoLineas[usuarioLineaIndiceEnUsuariosArchivo + 1]
                .rstrip()
                .split(" ")[1]
            )
            USUARIO_APELLIDO = (
                usuariosArchivoLineas[usuarioLineaIndiceEnUsuariosArchivo + 2]
                .rstrip()
                .split(" ")[1]
            )
            USUARIO_EMAIL = (
                usuariosArchivoLineas[usuarioLineaIndiceEnUsuariosArchivo + 3]
                .rstrip()
                .split(" ")[1]
            )
            USUARIO_CONTRASENA = (
                usuariosArchivoLineas[usuarioLineaIndiceEnUsuariosArchivo + 4]
                .rstrip()
                .split(" ")[1]
            )

            # CAMBIAR STATUS EN EL ARCHIVO DE AUTENTICACION (AUTH)

            autenticacionArchivoEscribir = open("./autenticacion.txt", "w")
            autenticacionArchivoEscribir.write(
                f"estaLogueado True\n--primerNombre {USUARIO_PRIMER_NOMBRE}\n--apellido {USUARIO_APELLIDO}\n--email {USUARIO_EMAIL}\n--password {USUARIO_CONTRASENA}\n"
            )
            autenticacionArchivoEscribir.close()

            print("\n----------------------------------------")
            print("\n[+] Inicio de sesion exitoso")
            print("----------------------------------------\n")

            mostrarPaginaPrincipal()
            return


# CERRAR SESION PANEL


def mostrarCerrarSesionPanel():
    while True:
        print("\n----Cerrar Sesion----")
        print(" Estas seguro que quieres cerrar sesion?")

        print("1. Cerar sesion")
        print("2. Cancelar")
        print("`, Atras")
        print("0. Salir")

        opcion = input("Tu seleccion >> ")

        if opcion == "1":
            autenticacionArchivoEscribir = open("./autenticacion.txt", "r+")
            autenticacionArchivoEscribir.write("estaLogueado False")
            autenticacionArchivoEscribir.close()

            print("\n----------------------------------------")
            print("\n[+] Sesion cerrada con exito")
            print("----------------------------------------\n")

            mostrarPaginaPrincipal()
            return

        if opcion == "2" or "`":
            mostrarPaginaPrincipal()
            return

        else:
            print("\n[!] Opcion invalida, intente de nuevo")


#  FIN DE AUTENTICACION

#  MENU PRINCIPAL

mostrarPaginaPrincipal()
