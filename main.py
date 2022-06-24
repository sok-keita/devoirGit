from fonction import *
print("****************menu*****************************")
print("**************************************************")
print("1-addition")
print("2-soustraction")
choix=int(input("faites votre choix"))
if(choix==1):
    print("1-addition")
    n1=int(input("entrez le premier nombre"))
    n2=int(input("entrez le deuxieme nombre"))
    somme(n1,n2)

if(choix==2):
    print("2-soustraction")
    n1=int(input("entrez le premier nombre"))
    n2=int(input("entrez le deuxieme nombre"))
    soustraction(n1,n2)