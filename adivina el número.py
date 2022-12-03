import random
import time
from os import system

def pista(aleatori_argument, numerointroduit, pistes_possibles):
    aleatori_pista=random.choice(pistes_possibles)
    if (aleatori_pista=="Parell/imparell"):
        if (aleatori_argument%2==0):
            print("\nPista: Es tracta d'un número parell")
            return 0
        else:
            print("\nPista: Es tracta d'un número imparell")
            return 0
    elif (aleatori_pista=="Quadrat"):
        print("\nPista: Es tracta d'un número el quadrat del qual és: " + str(aleatori_argument*aleatori_argument))
        return 1
    elif(aleatori_pista=="Xifres"):
        print(("\nPista: Es tracta d'un número amb ") + str(len(str(aleatori_argument))) + (" xifres"))
        return 2
    elif(aleatori_argument=="Triple"):
        print(("\nPista: el triple d'aquest número és: ") + str(aleatori_argument*3))
        return 3
    else:
        if (aleatori_argument>numerointroduit):
            print("\nPista: Prova amb un número més gran")
            return 4
        else:
            print("\nPista: Prova amb un número més petit")
            return 4

def menu():
    print("\nBenvingut a adivina el número!")
    opcio_menu=(int(input(("\nEscull una opció:\n\n1-Jugar\n2-Consultar puntuació\n3-Regles del joc\n4-Crèdits\n5-Sortir\n"))))
    return opcio_menu

def jugar(puntuacio, impossible):
    pistes_possibles=["Parell/imparell", "Quadrat", "Xifres", "Bigger/Smaller", "Triple"]
    sortir=False
    while (sortir==False):
        oportunitats=3
        intents=1
        endevinat=False
        print("\nSelecciona dificultat: \n")
        if (impossible==False):
            dif=int(input("1-Fàcil: Número entre 1 i 15\n2-Normal: Número entre 1 i 25\n3-Difícil: Número entre 1 i 100\n"))
            while(dif<1 or dif>3):
                print("\nOpció no vàlida.")
                print("\nSelecciona dificultat: \n")
                dif=int(input("1-Fàcil: Número entre 1 i 15\n2-Normal: Número entre 1 i 25\n3-Difícil: Número entre 1 i 100\n"))
        else:
            dif=int(input("1-Fàcil: Número entre 1 i 15\n2-Normal: Número entre 1 i 25\n3-Difícil: Número entre 1 i 100\n4-Impossible: Número entre 1 i 500\n"))
            while(dif<1 or dif>4):
                print("\nOpció no vàlida.")
                print("\nSelecciona dificultat: \n")
                dif=int(input("1-Fàcil: Número entre 1 i 15\n2-Normal: Número entre 1 i 25\n3-Difícil: Número entre 1 i 100\n4-Impossible: Número entre 1 i 500\n"))
        if (dif==1):
            aleatori=random.randint(1,15)
            num_max=15
        elif(dif==2):
            aleatori=random.randint(1,25)
            num_max=25
        elif(dif==3):
            aleatori=random.randint(1,100)
            num_max=100
        else:
            aleatori=random.randint(1,500)
            num_max=500
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
                if (oportunitats!=0):
                    opcio_pista=str(input("\nVols una pista? (S/N)"))
                    while(opcio_pista!="S" and opcio_pista!="N"):
                        print("\nOpció no vàlida.")
                        opcio_pista=int(input("\nVols una pista? (S/N)"))
                    if(opcio_pista=="S"):
                        posicio_pista=pista(aleatori,numerointroduit,pistes_possibles)
                        if(posicio_pista==0):
                            del pistes_possibles[posicio_pista]
                        elif(posicio_pista==1):
                            del pistes_possibles[posicio_pista]
                        elif(posicio_pista==2):
                            del pistes_possibles[posicio_pista]
                        elif(posicio_pista==3):
                            del pistes_possibles[posicio_pista]
                        elif(posicio_pista==4):
                            del pistes_possibles[posicio_pista]
                        else:
                            del pistes_possibles[posicio_pista]
        if (endevinat==True):
            print("\nEnhorabona!!! El número era " + str(aleatori) + ". L'has endevinat en " + str(intents) + " intents.")
        else:
            print("Llàstima!!! El número era " + str(aleatori))
        tornar=str(input("\nVols tornar a jugar? (S/N)"))
        while(tornar!="N" and tornar!="S"):
            print("\nOpció no vàlida")
            tornar=str(input("\nVols tornar a jugar? (S/N)"))
        if(tornar=="N"):
            print("\nSortint del joc...\n")
            time.sleep(3)
            sortir=True
        return puntuacio

def main():
    impossible=False
    puntuacio=0
    
    opcio_menu=menu()
    while(opcio_menu!=5):
        while(opcio_menu<1 or opcio_menu>5):
            print("\nOpció no vàlida.\n")
            opcio_menu=menu()
        if (opcio_menu==1):
            puntuacio=puntuacio+jugar(puntuacio, impossible)
        elif(opcio_menu==2):
            consultar_puntuacio(puntuacio)
        elif(opcio_menu==3):
            consultar_regles()
        else:
            credits()
        opcio_menu=menu()
    print("\nSortint...\n")

def credits():
    print("\n\n\nCÓDIGO E IDEA ÍNTEGRAMENTE REALIZADA POR ANDREU P.J.\n\n\n")
    tornar=""
    while(tornar!='S'):
        tornar=str(input("\nPrem 'S' per tornar al menú. "))

def consultar_puntuacio(puntuacio):
    print(("\nLa teva puntuació és: ") + str(puntuacio) + (" punts.\n"))
    if (puntuacio<10):
        print(("Amb " ) + str(10-puntuacio) + (" més punts podràs desbloquejar el nivell 'Impossible'"))
        impossible=False
    else:
        desbloquejar_impossible=str(input("\nVols desbloquejar el nivell 'Impossible'? (S/N) "))
        if (desbloquejar_impossible=='S'):
            print("\nNivell impossible desbloquejat. Bona sort.")
            impossible=True
    tornar=""
    while(tornar!='S'):
        tornar=str(input("\nPrem 'S' per tornar al menú. "))
    return impossible

def consultar_regles():
    print("\n\n\nEN DESARROLLO\n\n\n")
    print("Tornant al menú en...")
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)

main()