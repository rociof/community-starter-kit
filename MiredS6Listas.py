#Hola
#Ahora que ya conocemos como utilizar listas, podemos agregar una funcionalidad mucho mÃ¡s interesante
#a nuestra red social, y que nos hacÃ­a falta: administrar listas de amigos y de mensajes

#Hemos agregado dos valores nuevos para el perfil del usuario: una lista de amigos, y una lista de mensajes
#que llamaremos "muro"

#La lista de mensajes reemplazarÃ¡ a nuestro antiguo valor "num_amigos". Al conocer la lista de amigos,
#tambiÃ©n conoceremos la cantidad de amigos. Observa cÃ³mo leemos la lista de amigos en la funciÃ³n
#obtener_lista_amigos.
#Observa tambiÃ©n como se han modificado las funciones leer_archivo() y escribir_archivo()
#para ser concordantes con la nueva estructura de los archivos ".user"

#La segunda caracterÃ­stica serÃ¡ la publicaciÃ³n de un muro.
#En el archivo de cada usuario, luego de escribir su estado actual, agregaremos una lista de los mensajes
#que han sido publicados por sus amigos, de manera de formar una lista de mensajes que llamaremos "muro", o 'timeline',
#presente en casi todas las redes sociales.


#En este mÃ³dulo estÃ¡n todos las funciones  que hemos creado hasta ahora
import S6Red as Red


Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habÃ­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro = []

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
Red.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)
    elif opcion == 2:
        Red.mostrar_muro(muro)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado,muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar Mi Red. Â¡Hasta pronto!")

#Prueba este programa, e intenta enviar un mensaje a los amigos que pertenecen a tu lista.
#Te invitamos a ejecutar los siguientes desafÃ­os:
#1. Agrega una opciÃ³n que permita agregar un nuevo amigo a tu lista. En este caso no utilizaremos confirmaciÃ³n
#   de parte del destinatario, de manera que la relaciÃ³n de amistad puede perfectamente existir en un solo sentido.
#
#2. Agrega una opciÃ³n que permita mostrar los Ãºltimos estados de todos los amigos.
#   Ten en cuenta que esto no es equivalente a publicar los mensajes de tu muro, sino que necesitarÃ¡s
#   leer una lÃ­nea particular de los archivos de cada usuario en tu lista de amigos.
#
