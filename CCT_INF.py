#CREATED BY @NIX
#ORG CCT
#CLUSTER CYBERTERRORIST

import os
import time
import socket
import socket, random, time
import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[94m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (G+"""
          
╔═╗╔═╗╔══╗───╔══╗╔═╦╗╔══╗
║╔╝║╔╝╚╗╔╝───╚║║╝║║║║║═╦╝
║╚╗║╚╗─║║────╔║║╗║║║║║╔╝─
╚═╝╚═╝─╚╝────╚══╝╚╩═╝╚╝──

        
 """+R+"""v1.1\nORGANIZACION CCT"""+CY+"""

             
     

"""+Y+""">>"""+G+"""----"""+G+""" DEVELOPER - NIX """+G+"""----"""+Y+"""<<""")
        
    def m3():
        try:
            print(R+"""\n
#"""+CY+""" Selecciona Una Opcion """+G+""" >>"""+Y+"""

[1]"""+Y+""" Informacion De Tu IP """+Y+"""
[2]"""+Y+""" Informacion De otra IP"""+Y+"""
[3]"""+Y+""" DoS [Testing] """+Y+"""
[4]"""+Y+""" Scaneo De puertos """+Y+"""
[5]"""+Y+""" Salir
""")
            ch=int(input(G+"Selecciona Una Opcion del Menu: "+G))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                os.system("clear")
                os.system("python3 DoS.py")
            elif ch==4:
                os.system("clear")
                os.system("python3 scan.py")
            elif ch==5:
                 print (R+"adios...")
            else:
                print(R+"\n ¡Elección no válida! Inténtalo de nuevo¡Elección no válida! Petición\n")
                m3()
        except ValueError:
            print(R+"\n ¡Elección no válida! Inténtalo de nuevo\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(R+"\n◈━━━━━━━ ▣ ━━━━━━━ ◈ [ ORG CCT ] ◈━━━━━━━ ▣ ━━━━━━━ ◈")
                print(Y+'\n>>>'+CY+' Detalles de la dirección IP\n ')
                print(G+"1) Direccion IP : "+Y,data['query'],'\n')
                print(G+"2) ISP : "+Y,data['org'],'\n')
                print(G+"3) City : "+Y,data['city'],'\n')
                print(G+"4) Region : "+Y,data['regionName'],'\n')
                print(G+"5) Pais : "+Y,data['country'],'\n')
                print(G+"6) GeoLocalizacion\n\n\n")
                print(Y+"\t\t Latitud : "+G,data['lat'],'\n')
                print(Y+"\t\t Longitud: "+G,data['lon'],'\n')
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print(R+"\n#"+G+" Google Map link : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" ¿Abrir enlace en el navegador?"+G+" (Y / N): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\n Verifique otra IP o salga usando Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\n ¡Elección no válida! Inténtalo de nuevo\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" Open link in browser?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\n-----------------------------------------------------------------------------------------------------")
                        print(Y+"\n Verifique otra IP o salga usando "+R+"Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\n ¡Elección no válida! Inténtalo de nuevo\n")
                        m3()
                return
            except KeyError:
                print(R+"\n ¡Error! ¡Dirección IP/sitio web no válida!\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nError!"+Y+" ¡Por favor revise su conexion a internet! \n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+"Ingrese la dirección IP/dirección del sitio web"+W+" ")
        if u=="":
            print(R+"\n ¡Ingrese una dirección IP/dirección del sitio web válida!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
          
         
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nInterrupted ! :)"+W)
