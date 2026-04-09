"""Paso1: Debe tener
1)Obsiones Administrativas
2)Opciones de Usuario
3)Salir


#Opciones Administrativas
debe proporcionar clave de adceso-debe ser generada y guardada en (acceso.txt)
(Menú Administrativo):
4) Gestión de marcas de aviones
5)Gestión de tipos de aviones
6)Gestión de aerolíneas
7)Gestión de vuelos
8)Consultar historial de reservaciones
9)Estadisticas de vuelo
10)Regresar al menú principal
###almenos debe terner 3 credenciales de adceso(formato)usuario;clave  EJM;pperez;123


#Gestión de marcas de aviones
#debe permitir incluir,eliminar o modificar modelos de aviones, adémas de mostrarlos.L información se debera almacenar por modelo de avión: descripción modelo, marca de avión
(lista de marcas registradas en el sistema previamente),Cantidad de asientos clase ejecutiva,cantidad de asientos turista y cantidad de asientos economico. no pueden existir 2 modelos con la misma descripción y
no pueden eliminarse modelos que hayan sido asociados a algun avión.
varchivo:modeloAviones;  Airbus-,16;30;24

#Gestión de aerolíneas
Debe permitir dar mantenimiento a la aerolíneas,se debe #incluir,3eliminar o # modificar aerolineas, además de mostrarlas.
La información que se debe almacenar por aerolínea 
será el nombre y centro de operaciones. No pueden existir aerolíneas con el mismo nombre y no 
pueden eliminarse aerolíneas que hayan sido asociados algún avión. 
El archivo debe llamarse aerolineas.txt y este sería un ejemplo de su contenido: 
COPA; Ciudad de Panama PTY, SJO

#Gestión de aviones por aerolíneas
El sistema debe permitir dar mantenimiento de los aviones que poseen las aerolíneas, se debe 
permitir incluir, eliminar o modificar aviones, además de mostrarlos. La información que se debe 
almacenar por avión será: matrícula, marca, modelo (lista filtrada por marca seleccionada), año y 
aerolínea (lista seleccionable). 
No pueden existir dos aviones con la misma matrícula y no pueden eliminarse aviones que estén 
registrados en vuelos. 
El archivo debe llamarse avionesAerolineas.txt y este sería un ejemplo de su contenido: 
N101;Airbus;A320;2020;COPA

#Gestión de vuelos
El sistema debe permitir registrar vuelos, se debe permitir incluir, eliminar, modificar y mostrar 
vuelos. La información que se debe almacenar por vuelo será: número de vuelo (generado 
automáticamente), código de aeropuerto de ciudad salida, fecha y hora salida, código de 
aeropuerto de ciudad de arribo, fecha y hora arribo, aerolínea y la matrícula del avión (lista filtrada 
por la aerolínea seleccionada), monto asiento clase ejecutiva, monto clase turista y monto clase 
económica, todo esto en dólares. 
El archivo debe llamarse vuelos.txt y este sería un ejemplo de su contenido:
AV250;SJO;06/04/2026;14:50;MIA;06/04/2026;20:10;COPA;N101;600;350;250


#Consultar historial de reservaciones
Muestra una lista de las reservaciones generadas en el sistema. Por cada reservación debe mostrar 
lo siguiente: identificador de la reserva, nombre de la persona que reserva, número de vuelo, fecha 
y hora de la reservación, aerolínea, avión, lugar y fecha salida, lugar y fecha arribo, cantidad de 
asientos reservados en clase ejecutiva, clase turista y clase económica, monto de reservación.  
Se debe permitir filtrar la información por rango de fecha de salida, rango de fecha de llegada, 
rango de fecha de la reservación, lugar de arribo y salida.


#Estadisticas de vuelo
Se debe seleccionar un vuelo y mostrar el siguiente detalle:  
Número de vuelo, aerolínea, avión, lugar y fecha salida, lugar y fecha arribo, cantidad de asientos 
reservados y disponibles (por cada tipo), costo por boleto ejecutivo, turista y económico, monto 
recaudado por vuelo.


#Opciones generales
Para acceder a estas funcionalidades el usuario deberá ingresar por medio del Menú Principal y se 
deben habilitar las siguientes funcionalidades (Menú General): 
(11) Consulta de vuelos 
(12) Reservación de vuelo 
(13) Cancelación de reservación 
(14) Regresar al menú principal


#Consulta de vuelos
Muestra una lista de los vuelos. Por cada vuelo debe mostrar lo siguiente: número de vuelo, ciudad 
salida, fecha y hora salida, ciudad de arribo, fecha y hora arribo, aerolínea y avión, monto clase 
ejecutiva, monto clase turista y monto clase económica.  
Se debe poder filtrar la información por #aerolínea, #lugar salida, #lugar de arribo, #rango de fecha de 
salida y rango de #fecha de llegada.


#Reservación de vuelo
Cuando se hace la reservación debe seleccionarse el vuelo (mostrar información de número de 
vuelo, aerolínea, salida, arribo y fechas), la cantidad de espacios a reservar en clase ejecutiva, turista 
y económica.  
Se deberá reservar al menos un asiento en total. Se le entregará un comprobante (se mostrará en 
pantalla, no debe exportarse ni imprimir) al cliente con la siguiente información: identificador de la 
reserva (generado automáticamente), nombre de la persona que reserva (debe indicarlo al 
reservar), fecha y hora de la reservación, aerolínea, avión, lugar y fecha salida, lugar y fecha arribo, 
cantidad de asientos reservados en clase ejecutiva, clase turista y clase económica, monto de 
reservación. 
Debe validar que para la cantidad de asientos reservados en cada categoría existan espacios 
disponibles. Esta funcionalidad es la que “alimenta” el registro de reservaciones que se consulta en 
la sección Administrativa. 
El archivo debe llamarse reservas.txt


#Cancelición de reserva
Cuando se hace la cancelación se debe indicar el identificador de la reserva y se debe eliminar el 
sistema la reservación.


#Salir
Finaliza el programa. Al seleccionar esta opción se debe generar un mecanismo (manejo de archivos) 
para que los datos sean persistentes. La información se debe mantener para los siguientes usos del 
programa.  """
#Inicio de menú
def menu():
   print("Digite 1; para Obciones de usuario, Digite 2;Para Opciones administrativas,Digite 3; Para salir de la pagina")
   try:
      eleccion=input('Digite su opción')
      eleccion=int(eleccion)#pasandolo a int
      if not isinstance(eleccion,int):
         print('Solo puedes elegir opciones con números')
         return menu()
   except:
      print('Como no utilizo números le retornare denuevo al menú')
      return menu()
   if eleccion>3 or eleccion<1:#verificas que solo tenga esa obciones
      print(" no dijitaste una eleccion valida")
      return menu() 
   if eleccion==1:#abre ese archivo en especifico y lo lee
       return acceso()#mandarlo a estos función que desarrollare más tarde
   if eleccion==2:
      lecturaDatos="acceso.txt"
      return acceso(lecturaDatos)#esto sera la parte de usuario
   if eleccion==3:
       exit()# Para salirme de la pagina
def acceso(lecturaDatos):#contraseña para administrativos
   try:
      usuario=input('Digite su usuario')
      contraseña=input('Digite su contraseña')#genera la contraseña para el acceso administrativo
      if usuario=="":
         print("ERROR: Usuario vacio")
         return acceso(lecturaDatos)
      elif contraseña=="":
         print("ERROR:Contraseña vacia")
         return acceso(lecturaDatos)

   
      leer=open(lecturaDatos)#esa "r" significa leer
      contenido=leer.readlines()#si funciona, read line solo lee la primera fila, si le pongo un numero solo lee la cantidad de letras
#"""metodo mio para obtener datos"""
      primero=contenido[0]#toma el primer usuario y contraseña,  todos salen como str
      segundo=contenido[1]#toma el segundo usuario y contraseña
      tercero=contenido[2]#toma el tercer usuario y contraseña
   #####################definiir usuarios
      usuario1=[]# en estos seccionare para la comparativas
      usuario2=[]
      usuario3=[]
      pasword1=[]
      pasword2=[]
      pasword3=[]
   ##################################Obtencion de usuarios
      parar=","# usare este metodo para separar usuario y luego agarrar la contrasela aparte
      usuario1=primero.split(parar)[0]# ese cero dice que se inicia desde base 0 y para cuando encuentra ese caracter
      usuario2=segundo.split(parar)[0]
      usuario3=tercero.split(parar)[0]
   ###################obtencion contraseñas
      resultado1=1# sin el 1 leerian la comilla
      resultado2=1
      resultado3=1
      for cont1 in usuario1:
         resultado1+=1
      resultado1
      for cont2 in usuario2:
         resultado2+=1
      resultado2
      for cont3 in usuario3:
         resultado3+=1
      resultado3
      pasword1=primero[resultado1:]# 1234, usare[inicio:fin] para saltarme la comilla y solo leer contraseña"""""Funciona bien"""""""
      pasword2=segundo[resultado2:]# admin
      pasword3=tercero[resultado3:]# pporras
   #################aun conservan el salto de linea usre otro fort y debo quitar el\n
      r1=0
      r2=0
      r3=0# estan contando bien la caantidad de digitos
      pasword1=str(pasword1)#'1234\n' haci lo da cuando lo paso
      pasword2=str(pasword2)#hacer esto genera el \n al final con los contadores lo voy a eliminar
      pasword3=str(pasword3)
      for con1 in pasword1:
         r1+=1
      r1-=1
      for con2 in pasword2:
         r2+=1
      r2-=1
      for con3 in pasword3:
         r3+=1
      r3-=1
      pasword1=pasword1[:r1]
      pasword2=pasword2[:r2]
      pasword3=pasword3[:r3]#aqui ya estan bien
   ##################################### verificacion
      if usuario1==usuario and pasword1==contraseña:
         return OpcionesAdministrativas()
      if usuario2==usuario and pasword2== contraseña:
         return OpcionesAdministrativas()
      if usuario3==usuario and pasword3==contraseña:
         return OpcionesAdministrativas()
      else:
         print("su usuario o contraseña es incorrecta, porfavor volver aintentar")
         return acceso(lecturaDatos)
   
      leer.close()
   except:
      print('A ocurrido un error porfavor intente denuevo')
      return acceso(lecturaDatos)
   
            
      
      
  

   
   



   
def OpcionesAdministrativas():#falta hacer la validación de contraseña
    print('Digite 1 para gestión de marcas de aviones')
    print('Digite 2 para gestión de tipos de aviones')
    print('Digite 3 para gestión de aerolinea')
    print('Digite 4 para gestión de avion por aviones')
    print('Digite 5 para gestión de vuelos')
    print('Digite 6 para consultar historial de reservaciones')
    print('Digite 7 para estadisticas de vuelo')
    print('Digite 8 registros del menu principal')
    try:#verificador de solo números
        eleccion=input('Digite la gestion que decea realizar')
        eleccion=int(eleccion)#como dara problemas si esta haci lo voy a meter en tyr except y usaremimini verificador
        if not isinstance(eleccion,int):
           print("Solo existen opciones a elegir con números, vuelva a intentar")
           return OpcionesAdministrativas()
    except:
      print("Solo se aceptan números de los tipos de gestiones que decea realizar")
      return OpcionesAdministrativas()
    if eleccion>8 or eleccion<1:
       print('Solo tenemos 8 opciones a elegir')
       return OpcionesAdministativas()
    elif eleccion==1:
       return Marcas_De_Aviones()#despues defino que va hay
    elif eleccion==2:
       return Gestion_De_Tipos_De_Aviones()#despues defino que va
    elif eleccion==3:
       return Gestion_De_Aerolinea()
    elif eleccion==4:
       return Gestión_De_Avion_Por_Aviones()
    elif eleccion==5:
       return Gestion_De_Vuelos()
    elif eleccion==6:
       return Consultar_Historial_De_Reservaciones()
    elif eleccion==7:
       return Estadisticas_De_Vuelo()
    elif eleccion==8:
       return menu()
#Esto es parte de las administrativas despues veo los procesos de texto
def Marcas_De_Aviones():
   m=1
   
def Gestion_De_Tipos_De_Aviones():
   s=0
   
def Gestion_De_Aerolinea():
   a=1
def Gestión_De_Avion_Por_Aviones():
   b=2
def Gestion_De_Vuelos():
   c=3
def Consultar_Historial_De_Reservaciones():
   s=m
   
def Estadisticas_De_Vuelo():
   m=0
