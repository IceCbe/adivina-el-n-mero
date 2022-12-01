import random
import time
from os import system

def pista(aleatori_argument, numerointroduit):
    pistes_posibles=["Parell/imparell", "Quadrat", "Xifres", "Bigger/Smaller"]
    aleatori_pista=random.choice(pistes_posibles)
    if (aleatori_pista=="Parell/imparell"):
        if (aleatori_argument%2==0):
            print("\nPista: Es tracta d'un número parell")
        else:
            print("\nPista: Es tracta d'un número imparell")
    elif (aleatori_pista=="Quadrat"):
        print("\nPista: Es tracta d'un número el quadrat del qual és: " + str(aleatori_argument*aleatori_argument))
    elif(aleatori_pista=="Xifres"):
        print("\nPista: Es tracta d'un número amb " + len(str(aleatori_argument)) + " xifres")
    else:
        if (aleatori_argument>numerointroduit):
            print("\nProva amb un número més gran")
        else:
            print("\nProva amb un número més petit")

def menu():
    print("\nBenvingut a adivina el número!")
    opcio_menu=(int(input(("\nElegeix una opció:\n1-Jugar\n2-Consultar puntuació\n3-Regles del joc\n4-Crèdits\n5-Sortir\n"))))
    return opcio_menu

def jugar(puntuacio):
    sortir=False
    while (sortir==False):
        oportunitats=3
        intents=1
        endevinat=False
        print("\nSelecciona dificultat: \n")
        dif=int(input("1-Fàcil: Número entre 1 i 15\n2-Normal: Número entre 1 i 25\n3-Difícil: Número entre 1 i 100\n"))
        if (dif==1):
            aleatori=random.randint(1,15)
            num_max=15
        else:
            if (dif==2):
                aleatori=random.randint(1,25)
                num_max=25
            else:
                aleatori=random.randint(1,100)
                num_max=100
        while(endevinat==False and oportunitats>0):
            print("\nEt queden " + str(oportunitats) + " oportunitats")
            numerointroduit=int(input("\nIntrodueix un número de l'1 al " + str(num_max) + ": "))
            while(numerointroduit<1 or numerointroduit>num_max):
                print("\nNúmero fora de l'interval")
                numerointroduit=int(input("\nIntrodueix un número de l'1 al " + str(num_max) + ": "))
            if (numerointroduit==aleatori):
                endevinat=True
                if(dif==1):
                    puntuacio=puntuacio+1
                elif(dif==2):
                    puntuacio=puntuacio+3
                else:
                    puntuacio=puntuacio+10
            else:
                print("\nIncorrecte!")
                oportunitats-=1
                intents+=1
                opcio_pista=str(input("\nVols una pista? (S/N)"))
                while(opcio_pista!="S" and opcio_pista!="N"):
                    print("\nOpció no vàlida.")
                    opcio_pista=int(input("\nVols una pista? (S/N)"))
                if(opcio_pista=="S"):
                    pista(aleatori,)
        if (endevinat==True):
            print("\nEnhorabona!!! El número era " + str(aleatori) + ". L'has endevinat en " + str(intents) + " intents.")
        else:
            print("Llàstima!!! El número era " + str(aleatori))
        tornar=str(input("Vols tornar a jugar? (S/N)"))
        while(tornar!="N" and tornar!="S"):
            print("\nOpció no vàlida.")
            tornar=str(input("Vols tornar a jugar? (S/N)"))
        if(tornar=="N"):
            print("\nSortint del joc...\n")
            sortir=True

def main():
    puntuacio=0
    opcio_menu=menu()
    while(opcio_menu<1 or opcio_menu>5):
            print("\nOpció no vàlida.\n")
            opcio_menu=menu()
    while(opcio_menu!=5):
        if (opcio_menu==1):
            jugar(puntuacio)
        elif(opcio_menu==2):
            #consultar_puntuacio()
        #elif(opcio_menu==3):
            #consultar_regles()
        #else:
            credits()
    print("\nSortint...\n")

def credits():
    print("\n\n\nCÓDIGO E IDEA ÍNTEGRAMENTE REALIZADA POR ANDREU P.J.\n\n\n")
    tornar=""
    while(tornar!='S'):
        tornar=str(input("\nPrem 'S' per tornar al menú. "))

def consultar_puntuacio(puntuacio):
    print(("\nLa teva puntuació és: ") + str(puntuacio) + (" punts."))
    tornar=""
    while(tornar!='S'):
        tornar=str(input("\nPrem 'S' per tornar al menú. "))
print("Hóla")
