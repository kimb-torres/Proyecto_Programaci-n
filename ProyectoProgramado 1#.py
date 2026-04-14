
#Inicio de menú

def menu():
#libreria de fecha actual
   print("###################################################################################################################################")
   print("")
   print("   (1)Opciones de usuario")
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
         return menugeneral()

   
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
    
   print(" (4) para Gestión de avion por aerolinea")
    
   print(" (5) para Gestión de vuelos")
    
   print(" (6) para Consultar historial de reservaciones")
    
   print(" (7) para Estadisticas de vuelo")
    
   print(" (8) Registros del menu principal")

    
   print("###################################################################################################################################")
def OpcionesAdministrativas():
    textoOpcionesAdministrativas()
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
       return Gestion_De_Aerolinea()#lista pro quiero mejorarla

      
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


##############################################3INCLUIR
   
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
     if inclusion=="":
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
     return OpcionesAdministrativas()
   except Exception as e:
      print("ERROR: en Incluir:",e)
      return Marcas_De_Aviones()
      
      
######################################################MODIFICAR

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
      
        

      


############################################################################################
   #NUEVA FUNCIONADMINISTRATIVA


   
############################################################################NUEVO MODLULO
def portadaDeGestionDeAviones():
   print("###################################################################################################################################")
   print("")
   print("   (1)EliminarModelo")
   print("")
   print("   (2)ModificarModelo")
   print("")
   print("   (3)Salir")
   print("###################################################################################################################################")
   
def Gestion_De_Tipos_De_Aviones():
   portadaDeGestionDeAviones()
   modelo="modeloAviones.txt"
   
   archivo=open(modelo)
   if archivo=="":
      print("No puede haber archivos vacios")
      return OpcionesAdministrativas()
   contenido_modelos=archivo.read().split()#['A320;Airbus;16;50;130', '737;Boeing;16;30;150', 'E170;Embraer;66;70;15']
   archivo.close()

   aviones="aviones.txt"
   archivo1=open(aviones)
   if archivo1=="":
      print("No puede haber archivos vacios")
      return OpcionesAdministrativas()
   contenido_aviones=archivo1.read().split()#['Airbus', 'Boeing', 'Embraer']
   archivo1.close()
   

   
#variables que llegaremos a usar
   print("")
   print(" Escriba el número la opcion de lo que desea realizar")
   eligio=input("ESCRIBA EL NUMERO:")
   if eligio=="":
      return Gestion_De_Tipos_De_Aviones()
   elif eligio=="1":
      return eliminar_modelo()
   elif eligio=="2":
      return incluir_modelo()
   elif eligio=="3":
      return OpcionesAdministrativas()
   else:
      print("")
      print("Su eleccion se sale del rango")
      print("")
      return Gestion_De_Tipos_De_Aviones()
###########################################################################################################################
   #ELIMINAR
###############################################################################################
   
def eliminar_modelo():
   try:
      modelos="modeloAviones.txt"
      aviones="aviones.txt"

      
      archivo=open(modelos)
      contenido=archivo.read().split()#['A320;Airbus;16;50;130', '737;Boeing;16;30;150', 'E170;Embraer;66;70;15']
      archivo.close()
      
      
      if archivo=="":
         print("Archivo de modelos vacio")
         return Gestion_De_Tipos_De_Aviones()

      
      print("modelos de aviones")
      print("")
      print(contenido)
      print("")
      
      archivo1=open(aviones)
      contenido1=archivo1.read().split()#['Airbus', 'Boeing', 'Embraer']
      archivo1.close()
      
      if archivo1=="":
         print("Archivo de Marcas vacio")
         return Gestion_De_Tipos_De_Aviones()
      
      # hare que escriba el modelo en especifico a eliminar
      print(contenido)
      print("")
      print("solo pon el modelo a modificar ejemplo: A320, y haci se modificara todo, almenos que este en aviones")
      eliminar=input("Modeloa eliminar:")#ESTA ES LA INICIAL DEL INPUT
      if eliminar=="":
         print("No se puede eliminar un modelo vacio")
         return Gestion_De_Tipos_De_Aviones()
      
      
      ###############Inicio funciones
      nuevalista=[]
      parar=";"
      #COPIAAAAA
      copia_modelos=contenido
      
      for m in contenido:#eso vale nueva lista
         tucos=m.split(parar)#['A320', 'Airbus', '16', '50', '130', '737', 'Boeing', '16', '30', '150', 'E170', 'Embraer', '66', '70', '15']
         nuevalista=nuevalista+tucos#De aqui saldra en pedasos de 1 en 1 que luego comparare}

      #COPIAAAAAAAAAAS
      copiaNuevalista=nuevalista
      # creare un while para recorer para saber si el modelo coincuda
      contador=0
      verificador_modelos=0
      copiaModelos=nuevalista
      #################
      while nuevalista!=[]:
         if eliminar!=nuevalista[0]:
            contador+=1
         if eliminar==nuevalista[0]:
            verificador_modelos+=1
            break
         nuevalista=nuevalista[1:]
      #################A CONTADOR LE AGREGARE 1 PARA QUE ME E EL MODELO
      contador+=1
     # print(contador)# esta valiendo 1
      #print(copiaNuevalista[contador])#  da lo que es
      
      # otro para ver si ese modelo en especifico existe en aviones
      verificador_marcas=0
      while contenido1!=[]:
         if copiaNuevalista[contador]==contenido1[0]:
            verificador_marcas+=1
         contenido1=contenido1[1:]
         
     # print(verificador_modelos)# se enconto
     # print(verificador_marcas)# se encontro
      
      #COMFIRMABA SI ESTABA EN MODELOS Y SI ESTBA EN AVIONES
      if verificador_modelos>0 and verificador_marcas>0:
         print("ESTE MODELO NO SE PUEDE BORRAR , ESTA VINCULADO A AVIONES")
         return Gestion_De_Tipos_De_Aviones()
      
      if verificador_modelos==0:
         print("El modelo a buscar no existe")
         return Gestion_De_Tipos_De_Aviones()
      encontrado=0
      if verificador_modelos>0 and verificador_marcas==0:
         for recorrer  in copiaModelos:#A COPIA MODELOS NO LE PASO NADA, TODOD BIEN
            c=recorrer.split(parar)
            while c!=[]:
               if eliminar!=c[0]:
                  encontrado+=1#A ENCONTRADO LE VOY APLICAR DIVISION ENTERA HACI SABER CUAL DEBO ELIMINAR Y CUAL NO
               if eliminar==c[0]:
                  break
               c=c[1:]

#modelos="modeloAviones.txt"
 #     aviones="aviones.txt"
         #copiaModelos==['A320', 'Airbus', '16', '50', '130', '737', 'Boeing', '16', '30', '150', 'E170', 'Embraer', '66', '70', '15', 'AS7', 'SELVA', '33', '9', '9', 'J7', 'smn', '1', '2', '4']

         copiaMode_aux=contenido# son iguales entre comillas
         copias=contenido
############################### ya funciona
         #33333333333333333333333333333333333333333333333
         encontrado//=5#posicion donde se debe eliminar
         abriendo_eliminar=open(modelos,"w")# me lo esta devolviendo en cascade
         abriendo_eliminar.close()
         print(copiaMode_aux[encontrado])
         while copias!=[]:
            if copias[0]!=copiaMode_aux[encontrado]:
               listaTexto=copias[0]
               abrirAgregar=open(modelos,"a")
               print(listaTexto,file=abrirAgregar)
               abrirAgregar.close()
            if copias[0]==copiaMode_aux[encontrado]:
               pass# no lo agrega si ya esta
            copias=copias[1:]




      
   except Exception as e:
      print("ERROR: en ELIMINAR MODELO:",e)
      return Gestion_De_Tipos_De_Aviones()
   
      


#############################################################################################################################
   #INCLUSION
###########################################################################


#############################
   ########################DEBE MEJORARSE
   #########################################################
   
def incluir_modelo():
   try:
      modelos="modeloAviones.txt"
      print("")
      print("Digite el codigo de su modelo")
      modelo=input("Codigo de su modelo")
      print("")
      print("Digite la marca del avion")
      print("")
      marca=input("Digite la marca")
      print("Digite la cantidad de asientos primera clase")
      print("")
      claseAlta=input("Primeraclase:")
      print("Digite la cantidad de asientosclase turista")
      print("")
      turista=input("Asientos clase turista:")
      print("Digite la cantidad de asientos,Clase economica")
      print("")
      economico=input("Asientos clase economica")
      print("")
      claseAlta=int(claseAlta)
      turista=int(turista)
      economico=int(economico)
      
      if modelo=="":
         print("La opcion no puede estar vacia")
         return Gestion_De_Tipos_De_Aviones()
      if claseAlta=="":
         print("La opcion no puede estar vacia")
         return Gestion_De_Tipos_De_Aviones()
      if turista=="":
         print("La opcion no puede estar vacia")
         return Gestion_De_Tipos_De_Aviones()
      if economico=="":
         print("La opcion no puede estar vacia")
         return Gestion_De_Tipos_De_Aviones()
      claseAlta=str(claseAlta)
      turista=str(turista)
      economico=str(economico)
      
      #concatenare para luego comparar
      
      nuevo=modelo+";"+marca+";"+claseAlta+";"+turista+";"+economico
      nuevoLista=[nuevo]
      copia=nuevoLista##LISTA COMPLETAAAAAAA
      abrir=open(modelos)
      contenido=abrir.read().split()
      abrir.close()
      if abrir=="":
         print("El documento esta vacio")
         return Gestion_De_Tipos_De_Aviones()

      
      copiaC=contenido+copia#LISTA COMPLETAAAAAAA
      
      repetido=0
      
      
      while contenido!=[]:
         if contenido[0]==copia[0]:
            repetido+=1
         contenido=contenido[1:]

         
      if repetido>0:
         print("Este modelo ya se encuentra registrado")
         return Gestion_De_Tipos_De_Aviones()
      if repetido==0:
         borrar=open(modelos,"w")
         borrar.close()
         while copiaC!=[]:
            can=copiaC[0]
            agregar=open(modelos,"a")
            print(can,file=agregar)
            agregar.close()
            copiaC=copiaC[1:]
         print("Se agrego el avion con exito")
         return Gestion_De_Tipos_De_Aviones()
            
   except Exception as e:
      print("ERROR: en INCLUIR MODELO:",e)
      print(" no digito numero de asientos")
      return OpcionesAdministrativas()
            
      
   
   
#########################################################################################################3
   #NUEVA FUNCION
#########################################################################################################3
def poratadaGestionAerolinea():
   print("###################################################################################################################################")
   print("")
   print("(1)Incluir Aerolinea")
   print("")
   print("(2)Eliminar Aerolinea")
   print("")
   print("(3)Salir")
   print("###################################################################################################################################")

   
def Gestion_De_Aerolinea():
   print(poratadaGestionAerolinea())
   c=input("Digite su eleccion")
   if c=="":
      print("No existe opcion vacia intente de nuevo")
      return Gestion_De_Aerolinea()
   elif c=="1":
      return IncluirAerolinea()
   elif c=="2":
      return eliminarAeroline()
   elif c=="3":
      return OpcionesAdministrativas()
   else:
      print("La opcion que digitaste no existe")
      return OpcionesAdministrativas()
   
def eliminarAeroline():########USAR AVIONESAEROLINEAS.TXT
   
   try:
      aviones="aviones.txt"
      aerolinea="aerolineas.txt"

      
      abrir=open(aviones)
      contenido=abrir.read().split()
      abrir.close()

      
      if abrir=="":
         return Gestion_De_Aerolinea()

      
      abre=open(aerolinea)
      contenido1=abre.read()

      
      abre.close()
      abra=open(aerolinea)
      contenido2=abra.read().split()
      abra.close()
      copia=contenido2
      
      AF="Embraer"
      COPA="Boeing"
      LACSA="Airbus"
      ##Lacsa es
      marca1="AF"
      marca2="COPA"
      marca3="LACSA"
      print("Aerolines a Eliminar")
      print(contenido1)
      print()
      avion=input("Escriba Correctamente la aerolinea que decea eliminar:")
      if avion=="":
         print("El modelo no puede estar vacio")
         return Gestion_De_Aerolinea()
      copiaAvion=avion
      parar=";"
      listaavion=copiaAvion.split(parar)#['LACSA', 'Sanjose costarrica CMD', 'SJO']
      print(listaavion)
      Guardar=[]
      if listaavion[0] ==marca1:
         Guardar=AF
      elif listaavion[0]==marca2:
         Guardar=COPA
      elif listaavion[0]==marca3:
         Guardar=LACSA
      
         
###Aqui sabre la posicion del que voy a comparar
      encontrado=0
      for recorrer in contenido:
         if recorrer==Guardar:
            encontrado+=1
      #Haci me da la posicion
      if encontrado>0:
         print("Nose puede borrar esta aerolinea porque esta vinculado ala marca")
         return Gestion_De_Aerolinea()
            
      contador=0#cuenta perfecto
      KILL=[]
      if encontrado==0:
         for m in copia:
            if copiaAvion!=m:
               contador+=1
            else:
               KILL=m
               break
      borrar=open(aerolinea,"w")
      borrar.close()
      while copia!=[]:
         if copia[0]!=KILL:
            m=copia[0]
            a=open(aerolinea,"a")
            print(m,file=a)
            a.close()
         else:
            pass
         copia=copia[1:]
      print("Borrado con exito")
      return OpcionesAdministrativas()
            
            





      
   except Exception as e:
      print("ERROR: en ELIMINAR AEROLINE:",e)
      return eliminarAeroline()
######################################################################################
   
def IncluirAerolinea():
   try:
      print("ingrese la aeroLinea:")
      aerolinea=input("aerolinea:")
      print("")
      print("ingrese el destino; ejm: CiudadDePanama;CDP")
      destino=input("Ingrese el destino")
      if aerolinea=="":
         print("La aerolinea no puede estar vacia")
         return Gestion_De_Aerolinea()
      elif destino=="":
         print("El destino no puede estar en blanco")
         return Gestion_De_Aerolinea()

      
      coca=aerolinea+";"+destino
      cocaLista=[coca]#DIGNO DE UN MEME

      
      ar="aerolineas.txt"
      
      abre=open(ar)
      contenido=abre.read().split()#['LACSA;SanjoseCostarricaCDM;SJO', 'COPA;CiudaddePanamaPTY;MSJ', 'AF;Francia;MDT;(DMS)']
      abre.close()
      
      if abre=="":
         returnGestion_De_Aerolinea()
      trouve=0
      for n in contenido:
         if coca==n:
            trouve+=1
            
      if trouve>0:
         print("No se puede agregar una aerolinea, con todo repetid0")
         return Gestion_De_Aerolinea()

      nueva=contenido+cocaLista
      
      if trouve==0:
         o=open(ar,"w")
         o.close()
         while nueva!=[]:
            c=nueva[0]
            m=open(ar,"a")
            print(c,file=m)
            m.close()
            nueva=nueva[1:]
         print("Aerolinea agregada")
         return Gestion_De_Aerolinea()
         
         
      
   except Exception as e:
      print("ERROR: en INCLUIR AEROLINEA:",e)
      return IncluirAerolinea()






   
#################################################################################################3
def Gestión_De_Avion_Por_Aviones():#Gestion de avion por aerolinea###($$$$$$$$$44444444444444)
   print("############################################################################################################################")
   print("")
   print("(1)Incluir aviones")
   print("")
   print("(2)Eliminar aviones")
   print("")
   print("(3)Salir")
   print("")
   print("############################################################################################################################")
   ele=input("DIGITE SU ELECION")
   if ele=="1":
      return Incluir_Avion()
   if ele=="2":
      return eliminar_Avion()
   if ele=="3":
      return OpcionesAdministrativas()
   else:
      return Gestion_De_Avion_Por_Aviones()


def Incluir_Avion():
   try:
      avero="avionesAerolineas.txt"
      aviones="Aviones.txt"
      vuelos="vuelos.txt"
      
      abrir=open(avero)
      contenido=abrir.read()
      abrir.close()
      
      abre=open(aviones)
      contenido1=abre.read()
      abre.close()
      
      abra=open(vuelos)
      contenido2=abra.read().split()
      abra.close()
      parar=";"
      listaAerolinea=[]
      x=open(avero)
      dentro1=x.read().split()
      x.close()
      for p in dentro1:
         c=p.split(parar)
         listaAerolinea=listaAerolinea+c
      f=4
      listaAerea=[]
      conta=0
      for b in listaAerolinea:
         conta+=1
      while f<conta:
         if listaAerolinea[f]!=[]:
            listaAerea=listaAerea+[listaAerolinea[f]]
         else:
            pass
         f+=5
         
      
         
      
      print("Nuestros aviones por aerolinea son")
      print(contenido)
      print("")
      print("Matricula del avion que decea incluir")
      matricula=input("Matricula")
      print("")
      print("Ingrese el modelo de avion, modelos actuales son:")
      print(contenido1)
      avion=input("Tipo de avion a agregar:")
      print("")
      print("Digite el modelo de avion:")
      modelo=input("modelo:")
      print("")
      print("Digite el año de fabricacion")
      fecha=input("Año:")
      print("")
      print(listaAerea)# me sa solo las aerolineas
      print("Digite la aerolinea")
      aerolinea=input("Digite la aerolinea:")
      if matricula=="":
         print("Matricula Vacia")
         return Incluir_Avion()
      elif avion=="":
         print("modelo avion vacio")
         return Incluir_Avion()
      elif modelo=="":
         print(" modelo esta vacio")
         return Incluir_Avion()
      elif fecha=="":
         print(" EL año de fabricacion esta vacio")
         return Incluir_Avion()
      elif aerolinea=="":
         print("La aerolinea esta vacia")
         return Incluir_Avion()
      ##########AVIONES
      f=open(aviones)
      dentroAviones=f.read().split()
      f.close()
      
      m=open(avero)
      dentro=m.read().split()#['MSN001;Airbus;A320;2006;LACSA', 'N804AM;Boeing;737;2020;COPA', 'LOT;Embraer;E1170;2002;AF']AvionesAerolineas
      m.close()

      nuevalista=[]
      Regarder=0
      for u in listaAerea:
         if aerolinea ==u:
            Regarder+=1
      if Regarder==0:
         print("La aerolinea que desea agregar no esta en nuestros registros")
         return Gestión_De_Avion_Por_Aviones()

      for r in dentro:
         c=r.split(parar)
         nuevalista=nuevalista+c#['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF
#['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF']
#matricula aparece cada5
         ###CONTADOR
      contador=0
      i=0
      Lista=nuevalista
      largo=0
      for l in nuevalista:
         largo+=1
#verificar que matricula no se repita
      while i<largo:
         if nuevalista[i]==matricula:
            contador+=1
         i+=5
      if contador>0:
         print("la matricula que menciono ya esta vinculada a un modelio de avion,vuelva a intentar")
         return Incluir_Avion()
      enAvion=0
      if contador==0:#Osea si la matricula no es igual se verifica esto
         for t in dentroAviones:
            if avion==t:
               enAvion+=1
      if enAvion==0:
         print("El avion que deceas agregar no existe en nuestro registro")
         return Gestión_De_Avion_Por_Aviones()
      elif enAvion>0:
         nuevoModelo=matricula+";"+avion+";"+modelo+";"+fecha+";"+aerolinea
         dentro=dentro+[nuevoModelo]
         borrar=open(avero,"w")
         borrar.close()
         for s in dentro:
            a=open(avero,"a")
            print(s,file=a)
            a.close()
         print("Gestion de aerolinea agregada con exito,este nuevo modelo")
         return Gestión_De_Avion_Por_Aviones()
   except Exception as e:
      print("ERROR: en INCLUIR GESTION:", e)
      return Gestión_De_Avion_Por_Aviones()
      








      

#######################################################################################################################33
   #ELIMINACION DE MODELOS NO INCLUIDOS

###########################################################################################################################

def eliminar_Avion():
   try:
      avero="avionesAerolineas.txt"
      aviones="Aviones.txt"
      vuelos="vuelos.txt"
      
      abrir=open(avero)
      contenido=abrir.read()
      abrir.close()
      
      abre=open(aviones)
      contenido1=abre.read()
      abre.close()
      
      abra=open(vuelos)
      contenido2=abra.read().split()
      abra.close()
      parar=";"
      listaAerolinea=[]
      
      x=open(avero)
      dentro1=x.read().split()
      x.close()
      listaModelos=[]
  
      for p in dentro1:
         c=p.split(parar)
         listaAerolinea=listaAerolinea+c
      
      datos = dentro1
      e=4
      listaAerea=[]
      u=open(avero)
      wao=u.read().split()
      u.close()
      datos = dentro1
      largo=0
      MU=[]
      for n in wao:
         s=n.split(parar)
         MU=MU+s

      
      for u in MU:
         largo+=1
      
      
      while e<largo:
         listaAerea=listaAerea+[MU[e]]
         e+=5
         if e>largo:
            break

         
      listaModelos = []
      

      while datos != []:
          linea=datos[0]
          partes=linea.split(parar)

          if partes != []:
             try:
             
                listaModelos=listaModelos + [partes[2]]
             except:
                 pass

          datos = datos[1:]
       
      print("Nuestros aviones por aerolinea son")
      print(contenido)
      print("")
      print("Matricula del avion que decea ELIMINAR")
      matricula=input("Matricula")
      print("")
      print("Ingrese el modelo de avion, modelos actuales son:")
      print(contenido1)
      avion=input("Tipo de avion a ELIMINAR:")
      print("")
      print("Digite el modelo de avion:")
      print(listaModelos)
      modelo=input("modelo:")
      print("")
      print("Digite el año de fabricacion")
      fecha=input("Año:")
      print("")
      print(listaAerea)
      print("Digite la aerolinea")
      aerolinea=input("Digite la aerolinea:")
      if matricula=="":
         print("Matricula Vacia")
         return eliminar_Avion()
      elif avion=="":
         print("modelo avion vacio")
         return eliminar_Avion()
      elif modelo=="":
         print(" modelo esta vacio")
         return eliminar_Avion()
      elif fecha=="":
         print(" EL año de fabricacion esta vacio")
         return eliminar_Avion()
      elif aerolinea=="":
         print("La aerolinea esta vacia")
         return eliminar_Avion()
      
      ##########AVIONES
      f=open(aviones)
      dentroAviones=f.read().split()#AVIONS SALEN TUQIADOS
      f.close()


      volar=open(vuelos)
      dentroVolar=volar.read().split()
      volar.close()
      listaVuelo=[]

      for j in dentroVolar:
         t=j.split(parar)
         listaVuelo=listaVuelo+t#['MSN001', 'CDM', 'SJO', 'COPA', 'A30', '16', '50', '130']#VUELOS

           
      m=open(avero)
      dentro=m.read().split()#['MSN001;Airbus;A320;2006;LACSA', 'N804AM;Boeing;737;2020;COPA', 'LOT;Embraer;E1170;2002;AF']AvionesAerolineas
      m.close()
      nuevalista=[]
      for r in dentro:
         c=r.split(parar)
         nuevalista=nuevalista+c#['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF
#['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF']
      copiaListaVuelo=listaVuelo
         
      contador=-1# saber la posicion, y si lo que sige del modelo esta en el otro
      equivale=0#saber si se encontrp
      while listaVuelo!=[]:
         if listaVuelo[0]==matricula:#saber si la que buscamos se encuentra
            equivale+=1#['MSN001', 'CDM', 'SJO', 'COPA', 'A320', '16', '50', '130']#VUELOS
            break
         else:
            contador+=1# hase en 7# esta BIEN QUIERE DECIR QUE NO SE ENCUENTA
            listaVuelo=listaVuelo[1:]
      
           
            
      contador2=0
      #contador vale 11 se recontra pasa
      
      # me esta dando el final
      if equivale>0:#si se encuentra buscamos la posicion
         verificacion=copiaListaVuelo[contador]#Para refiicar el modelo si coincide, mousequeramienta que usare mas tarde
     
      
   
      posicion=-1
      Trouve=0
      
      #################CONTADOR POSICION MATRICULA
      for u in nuevalista:# encontara si aqui esta la maricula
         if matricula!=u:#['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF']
            posicion+=1#LEE 1 DE MAS
         elif matricula==u:
            Trouve+=1
 ##############################################           
      copia=posicion# ese tres cuando se divida entero da cifra exacta de donde esta
      
     # deberia darme el modelo, en AVIONES AEROLINEAS
      
      posicion-=1
      verifica2=nuevalista[posicion]
      print(verifica2)
      if equivale>0 and Trouve>0 and verificacion==verifica2:# funciona
         print("NO SE PUEDE BORRAR ESTE MODELO, ESTA ASOCIADO EN VUELOS")
         return Gestión_De_Avion_Por_Aviones()
      if equivale>0 and Trouve==0:
         print("El avion a eliminar no existe en modelos")
         return Gestión_De_Avion_Por_Aviones()
      if Trouve==0 and equivale==0:
         print("Este modelo no existe")
         return Gestión_De_Avion_Por_Aviones()
      if Trouve>0 and equivale==0:
         copia//=5
         borrar=open(avero,"w")
         borrar.close()

         
         for s in dentro:
            if s != dentro[copia]:
               abre=open(avero,"a")
               print(s,file=abre)
               abre.close()
         print("Modelo borrado con exito")
         return Gestión_De_Avion_Por_Aviones()

   except Exception as e:
      print("ERROR: en INCLUIR GESTION:", e)
      return Gestion_De_Vuelos()
      


              #['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF
#['MSN001', 'Airbus', 'A320', '2006', 'LACSA', 'N804AM', 'Boeing', '737', '2020', 'COPA', 'LOT', 'Embraer', 'E1170', '2002', 'AF']
      
    
  
##################################################################################################################3
   #NUEVA FUNCION

   
 #################################################################################################################  
def Gestion_De_Vuelos():
   print("####################################################################################################")
   print("")
   print("(1)Incluir Vuelos")
   print("")
   print("(2)Eliminar Vuelo")
   print("")
   print("(3)Mostrar Vuelos")
   print("")
   print("(4)Salir")
   print("")
   print("####################################################################################################")
   eli=input("DIGITE SU ELECCION:")
   if eli=="":
      print("La eleccion no debe estar en blanco")
      return Gestión_De_Avion_Por_Aviones()
   elif eli=="1":
      return Incluir_Gestion()
   elif eli=="2":
      return Eliminar_Gestion()
   elif eli=="3":
      return Mostrar_Vuelos()
   elif eli=="4":
      return OpcionesAdministrativas()
   else:
      return Gestión_De_Avion_Por_Aviones()
######################################################################################################################

   
def Incluir_Gestion():
   try:





      avero="avionesAerolineas.txt"
      aviones="Aviones.txt"
      vuelos="vuelos.txt"
      
      abrir=open(avero)
      contenido=abrir.read()
      abrir.close()
      
      abre=open(aviones)
      contenido1=abre.read()
      abre.close()
      
      abra=open(vuelos)
      contenido2=abra.read().split()
      abra.close()
      parar=";"
      listaAerolinea=[]
      x=open(avero)
      dentro1=x.read().split()
      x.close()
      listaModelos=[]
      
      for p in dentro1:
         c=p.split(parar)
         listaAerolinea=listaAerolinea+c
      
      datos = dentro1
      e=4
      listaAerea=[]
      u=open(avero)
      wao=u.read().split()
      u.close()
      datos = dentro1
      largo=0
      MU=[]
      for n in wao:
         s=n.split(parar)
         MU=MU+s

      
      for u in MU:
         largo+=1
      
      
      while e<largo:
         listaAerea=listaAerea+[MU[e]]
         e+=5
         if e>largo:
            break

         
      listaModelos = []
      

      while datos != []:
          linea = datos[0]
          partes = linea.split(parar)

          if partes != []:
             try:
                listaModelos = listaModelos + [partes[2]]
                
             except:
               print("Dato malo:", partes)

          datos = datos[1:]
      
       
      print("Bienvenido: porfavor ingresar")
      print(contenido)
      print("")
      print("Matricula del avion que decea Generar el vuelo:")
      codigo=input("Ingrese: un codigo")
      print("")
      print("Ingrese el modelo de avion, modelos actuales son:")
      print(contenido1)
      CodigoAeropuerto=input("Ingrese el codigo del Aeropuerto:")
      print("")
      print("Digite el modelo de avion:")
      print(listaModelos)
      modelo=input("modelo avion:")
      print("")
      print(listaAerea)
      print("Digite la aerolinea")
      aerolinea=input("Digite la aerolinea:")
      if codigo=="":
         print("Matricula Vacia")
         return eliminar_Avion()
      elif CodigoAeropuerto=="":
         print("modelo avion vacio")
         return eliminar_Avion()
      elif modelo=="":
         print(" modelo esta vacio")
         return eliminar_Avion()
         
      elif aerolinea=="":
         print("La aerolinea esta vacia")
         return eliminar_Avion()
      

      Encontrada_Aerolinea=0#SOLO COMPRUEVA QUE ELIGE UNA AEROLINEA REGISTARDA
      for n in listaAerea:
         if aerolinea==n:
            Encontrada_Aerolinea+=1
      if Encontrada_Aerolinea==0:
         print("La aerolinea No existe")
         return Gestion_De_Vuelos()
      








      
   except Exception as e:
       print("ERROR: en INCLUIR GESTION:",e)
       return Gestion_De_Vuelos()

def Eliminar_Gestion():
   s=1

def Mostrar_Vuelos():
   m=0


















   








   
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
   
   elif elige=="1":#abre ese archivo en especifico y lo lee
       return consultaVuelos()#mandarlo a estos función que desarrollare más tarde
   elif elige=="2":
      return ReservacionesVuelos()#esto sera la parte de usuario
   elif elige=="3":
       return CancelarReservacion()# Para salirme de la pagina
   elif elige=="4":
      return menu()
   else:
      print(" no dijitaste una eleccion valida")
      return menugeneral() 


   
def usuario():
   m=0
