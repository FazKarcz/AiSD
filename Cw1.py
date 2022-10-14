#ZAD1
def Kropka(litera,nazwisko):
    return(litera+"."+nazwisko)
#print(Kropka("J","Karcz"))

#ZAD2
def DuzaKropka(imie,nazwisko):
    a = imie.title()
    b = nazwisko.title()
    return(a[0]+"."+b)
#print(DuzaKropka("jakub","karcz"))

#ZAD3
def wiek(pier,ost,wiek):
    pier = pier*100
    ost = pier+ost
    return(ost-wiek)
#print(wiek(20,22,21))

#ZAD4
def co(imie,nazwisko,funkcja):
    return funkcja(imie,nazwisko)
#print(co("j","karcz",DuzaKropka))

#ZAD5
def dzielnosc(a,b):
    if(a<0 or b<0 and b==0):
        return("liczba nie moze być ujemna, drugi argument nie może być zerem")
    return(a/b)
#print(dzielnosc(20,5))

#ZAD6 SKRYPT
#x = 0
#while x<=100:
#    x = x + int(input("x="))
#print(x)

#ZAD7
def listadokrotki(lista):
    krotka=tuple((x for x in lista))
    return krotka

#lista=[1,2,"kokos",69,"jajecznica","Tomaszów",5,4,3]
#print(lista)
#print((listadokrotki(lista)))

#ZAD8 SKRYPT
#lista=[]
#for i in range(0,5):
#    x=input("X=")
#    lista.append(x)
#print((listadokrotki(lista)))

#ZAD9 SŁOWNIK
def dzientygodnia(x):
    return{
        1:'Poniedziałek',
        2:'Wtorek',
        3:'Środa',
        4:'Czwartek',
        5:'Piątek',
        6:'Sobota',
        7:'Niedziela',
    }.get(x,'Wprowadź numer od 1 do 7')
#print(dzientygodnia(1))

#ZAD10
def palindrom(char):
    for i in range(int(len(char)/2)):
        if(char[i]!=char[(len(char)-1)-i]):
            return 0
    return 1
#print(palindrom('131'))
#print(palindrom('9683'))