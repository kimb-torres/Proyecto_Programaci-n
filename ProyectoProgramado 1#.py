
#Inicio de menú

def menu():
#libreria de fecha actual
   print("###################################################################################################################################")
   print("")
   print("   (1)Obciones de usuario")
   print("")
   print("   (2)Opciones administrativas")
   print("")
   print("   (3)Salir de la pagina")
   print("")
   print("   (4) Menú general")
   print("###################################################################################################################################")
   try:
      eleccion=input('Digite su opción;')
      eleccion=int(eleccion)#pasandolo a int
      if not isinstance(eleccion,int):
         print('Solo puedes elegir opciones con números')
         return menu()
   except:
      print('Como no utilizo números le retornare denuevo al menú')
      return menu()
   
   if eleccion>4 or eleccion<1:#verificas que solo tenga esa obciones
      print(" no dijitaste una eleccion valida")
      return menu()
   
   if eleccion==1:#abre ese archivo en especifico y lo lee
       return usuario()#mandarlo a estos función que desarrollare más tarde

      
   if eleccion==2:
      return acceso()#esto sera la parte de usuario
   if eleccion==3:
       exit()# Para salirme de la pagina
       
   if eleccion==4:
      return Menugeneral()

   
def acceso():#contraseña para administrativos
   lecturaDatos="acceso.txt"
   try: 
      usuario=input('Digite su usuario')

      
      contraseña=input('Digite su contraseña')#genera la contraseña para el acceso administrativo
      if usuario=="":
         print("ERROR: Usuario vacio")
         return acceso()
      
      elif contraseña=="":
         print("ERROR:Contraseña vacia")
         return acceso()

   
      leer=open(lecturaDatos)#esa "r" significa leer
      contenido=leer.read().split()#si funciona, read line solo lee la primera fila, si le pongo un numero solo lee la cantidad de letras
      if contenido==[]:
         print("No hay elementos en el archivo")
         return menu()
      
      leer.close()
      i=0
      USPAS=[]
      parar=";"
      
      for contar in contenido:
         cambianteLinea=contenido[i]#leee el primer dato de la lista y lo gace str
         lectorL=cambianteLinea.split(parar) #lee ese str y lo parte en una lista de 2 cuando encuentra el caracter
         USPAS=USPAS+ lectorL#va sumando los 2 modulos a una nueva lista
         i+=1
         ###############################Funciones
         
      largo=0#aqui mismo i ==3
      conta=0
      copia=[]
      m=1
      copia=copia+USPAS# aqui se mantendran los datospara seguir evaluando

      
      while USPAS!=[]:#medira el largo de la lista para el siguiente paso
         largo+=1
         USPAS=USPAS[1:]
      pass #cuando USPAS SALE de qui sale vacia

      encontrado=0
   #################################################
   #LECTOR CONTRASEÑA POR FIIIIIIIIN Y SIN VER VIDEOS JAJAJJA LA EZQIZO
      #100% funcional
      while m<largo:
         if copia[m]==contraseña and copia[conta]==usuario:
            encontrado+=1
         m+=1
         conta+=1
      pass
      if encontrado>=1:
         return OpcionesAdministrativas()
      else:
         print("contraseña o usuario incorrecto")
         return acceso()
   except :
      print("Ocurrio un error, retornare a acceso")
      return acceso()
      
def textoOpcionesAdministrativas():
   print("###################################################################################################################################")
    

   print(" (1)Gestión de marcas de aviones")
    
   print(" (2)Gestión de tipos de aviones")
    
   print(" (3)para Gestión de aerolinea")
    
   print(" (4) para Gestión de avion por aviones")
    
   print(" (5) para Gestión de vuelos")
    
   print(" (6) para Consultar historial de reservaciones")
    
   print(" (7) para Estadisticas de vuelo")
    
   print(" (8) Registros del menu principal")

    
   print("###################################################################################################################################")
def OpcionesAdministrativas():
    print(textoOpcionesAdministrativas())
   #esto funciona el problema es en el while de acceso, ya no molesta amenos que haya un error
    eleccion=input("Digite su obcion a elegir,debe ser número")

    if eleccion=="":
       print("No existen opciones Vacias")
       return OpcionesAdministrativas()
    elif  eleccion=="1":
       return Marcas_De_Aviones()#despues defino que va hay
 
      
    elif eleccion=="2":
       return Gestion_De_Tipos_De_Aviones()#despues defino que va

      
    elif eleccion=="3":
       return Gestion_De_Aerolinea()

      
    elif eleccion=="4":
       return Gestión_De_Avion_Por_Aviones()

      
    elif eleccion=="5":
       return Gestion_De_Vuelos()

      
    elif eleccion=="6":
       return Consultar_Historial_De_Reservaciones()

      
    elif eleccion=="7":
       return Estadisticas_De_Vuelo()

      
    elif eleccion=="8":
       return menu()
    else:
       print("su elección no esta en nuestro sistema,vuelva a intentar")
       return OpcionesAdministrativas()
####################################################################################
def textoOpcionesenavione_aux():
   print("###################################################################################################################################")
   print("###################################################################################################################################")
   print("")
   print("   (1)Ver los modelos de Aviones")
   print("")
   print("   (2)Incluir modelos de aviones")
   print("")
   print("   (3)Eliminar  o modificar Marca de Avión")
   print("")
   print("   (4) Regresar al menú Principal")
   print("###################################################################################################################################")
   print("###################################################################################################################################")
   
#Esto es parte de las administrativas despues veo los procesos de texto
def Marcas_De_Aviones():#aqui se debe poder agregar y modificar nada más es el paso mas sencillo
   print(textoOpcionesenavione_aux())
   print("")
   opcion=input("Ingrese su elección")
# Ya funciona correctamente
   if opcion=="":
      print("No existen esta Opcion")
   elif opcion=="1":
      return Modelos()
   elif opcion=="2":
      return Incluir()
   elif opcion=="3":
      return Modificar()
   elif opcion=="4":
      return menu()
   else:
      print("Su opcion no se encuentra")
      return OpcionesAdministrativas()

 ################################################################CORREGIR  


   
def Modelos():
   marcas="aviones.txt"
   M=open(marcas)
   c=M.read()
   M.close()
   print("")
   print("Modelos de aviones actualmente")
   print("")
   print(c)# despues de eto nos manda denuevo ala opciones
   print("")
   volver=input("Digite cualquier cosa,para volver a Gestion de aviones")
   if 1==1:
      return Marcas_De_Aviones()



   
def Incluir():# Ya sirve
   try:
     marcas="aviones.txt"
     modelo="modeloAviones.txt"
     entrar=open(marcas)
     archivo=entrar.read().split()#['Airbus','Boeing','Embraser']
     entrar.close()

   
     print(archivo)
     print("")
     print("Marcas actuales")
     print()
     print("")
   
     inclusion=input("escriba el nombre dela Marca de que desea incluir")
     if inclusin=="":
        print("No podemos Incluir un vacio")
        return Incluir()
   
    # voy a crear 3 opciones haci se divide mejor

      # i ahorita vale como 12
      
     AbriendoEnAgregar=open(marcas,"a")   
     for m in archivo:#inclusion recorre el archivo buscando aver si esta s no esta se agrega
        if inclusion==m:
           print("Esta marca ya ha sido asociada, la returnare ala pajina principal")
           return Marcas_De_Aviones()
     pass
     print(inclusion,file=AbriendoEnAgregar)#AGREGA ALA LISTA Y LO AGREGA CON SALTO DE LIENA :>>>>>>>
     
     AbriendoEnAgregar.close()
     print("Se incluyo su marca exitosamente")
     return Marcas_De_Aviones()
   except Exception as e:
      print("ERROR: en Incluir:",e)
      return Marcas_De_Aviones()
      
      


def Modificar():
   
    try:
        marcas = "aviones.txt"
        modelos = "modeloAviones.txt"

        # Leer marcas
        archivo = open(marcas)
       
        lista_marcas = archivo.read().split()
        if lista_marcas==[]:
           print("Error. El archivo esta vacio")
           return Marcas_De_Aviones()
        archivo.close()

        listaMarcasFinal=[]
        listaMarcasFinal=lista_marcas
        listaMarcas= []
        listaMarcas=lista_marcas
        

        # Leer modelos 
        archivo = open(modelos)
        
        lista_modelos = archivo.read().split()# salen conservando el salto de linea
        if lista_modelos==[]:
           print("Error. El archivo esta vacio")
           return Marcas_De_Aviones()
        archivo.close()

        print("Marcas actuales:")
        print(lista_marcas)
        eliminar = input("Digite la marca que desea eliminar:")
        parar=";"
        NuevaListaModelos=[]

        if eliminar=="":
           print("no se puede eliminar el vacio")
           return OpcionesAdministrativas()
         
        for m in lista_modelos:#aqui sale ['A320', 'Airbus', '16', '50', '130', '737', 'Boeing', '16', '30', '150', 'E170', 'Embraer', '66', '70', '15']
          Variable=m.split(parar)#aqui todo sale en tuqitos
          NuevaListaModelos=NuevaListaModelos+Variable
        print(NuevaListaModelos)
         
        encontrado=0#haci verificare si se encuentra o no, si quedara en 0 no se encontro y si queda en 1 se enconytro
        copia_modelos=[]
        copia_modelos=NuevaListaModelos
        listaEliminacion=[]
        

        
# segun mi razonamiento si se encuentra en modelos es porque fue asociado a un avion y no se debe modificar
        while  NuevaListaModelos!=[]:# aqui lo que hare es contar si tambien se encuentra aqui el elemneto
           if eliminar== NuevaListaModelos[0]:#cuenta si sale o no sale
              
              encontrado+=1# YA SE CORRIGIO ENTOCES A ENCONTRADO SI SE LE SUMA

           NuevaListaModelos=NuevaListaModelos[1:]# el ENCONTRADO DE AQUI ES PARA SABER SI ESTA EN 1 O EN OTRO
           
        encontrado2=0
        # aqui contare si salio anteriormente si sale qui tambien##SI NO LO ENCONTRO EN MODELOS VIENE AQUI
        while lista_marcas!=[]:#LISTA_MARCAS ESTA COMPLETA
            if eliminar==lista_marcas[0]:
               encontrado2+=1# AHORA CADA QUE LO ENCUENTRA SUMA
            lista_marcas=lista_marcas[1:]
   

               # si si salio procedere a eliminarlo
               
        if encontrado2==0 :
           print("El dato a eliminar no existe")
           return Marcas_De_Aviones()
         
        elif encontrado>0 and encontrado2>0:
           print("No se puede borrar este modelo, esta vinculado a modelo de aviones")
           return Marcas_De_Aviones()
        i=0
        ########################## ELIMINADOR DE ALGO EN ESPECIFI
        if encontrado2>0 and encontrado==0:
           abriendoParaEliminar=open(marcas,"w")#Hace el tecto en blanco
           abriendoParaEliminar.close()
           while listaMarcasFinal!=[]:
              if eliminar!=listaMarcasFinal[0]:
                 listaEliminacion=listaMarcasFinal[0]
                 abriendo_Agregar=open(marcas,"a")
                 print(listaEliminacion,file=abriendo_Agregar)
                 abriendo_Agregar.close()
                 print("Borrado con exito")
              listaMarcasFinal=listaMarcasFinal[1:]# cuando salga de esto hare una borracion

         
                 
           
           
            
                                 
    except Exception as e:
      print("ERROR: en Modificar:",e)
      return Marcas_De_Aviones()
      
        

      








   
   
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


   
def menugeneral():
   print("###############################################################################################################################################################")
   print("")
   print("   (1) Consulta de vuelos")
   print("")
   print("   (2)Reservaciones de vuelo")
   print("")
   print("   (3)Cancelación de reservacion")
   print("")
   print("   (4)Regresar al menú principal")
   print("###############################################################################################################################################################")
   elige= input("Elija el número de su tramite")
   if elige=="":
      print("No existe opcion vacia")
      return menugeneral()
   
   elif elegir=="1":#abre ese archivo en especifico y lo lee
       return consultaVuelos()#mandarlo a estos función que desarrollare más tarde
   elif elegir=="2":
      return ReservacionesVuelos()#esto sera la parte de usuario
   elif elegir=="3":
       return CancelarReservacion()# Para salirme de la pagina
   elif elegir=="4":
      return menu()
   else:
      print(" no dijitaste una eleccion valida")
      return menugeneral() 


   
def usuario():
   m=0
