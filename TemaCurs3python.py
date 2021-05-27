
# Sa se scrie o functie care primeste un nr nedefinit de parametrii si sa se calculeze suma parametrilor nr intregi sau reale
#*args ia toate argumentele pozitionale pana la intalnirea primului parametru cheie valoare (param cheie:valoare este de exemplu param_1=2)

def f_sum(*args,**kwargs):
    summ=0
    if args!="":
        for x in args:
            if  type(x) == int:
                summ=summ+x
        return summ
    return 0

rezultat=f_sum(1, 5, -3, 'abc', [12, 56, 'cad'])#args ia 1,5,-3,'abc',[12,56,cad]
print(rezultat)

rezultat2=f_sum(2, 4, ‘abc’, param_1=2)#args ia 2,4,'abc',iar kwargs ia param_1(parametru cheie:valoare
print(rezultat2)                #regula:param cheie:valoare trebuie mereu pusi la sfarsit

rezultat3=f_sum()
print(rezultat3)

#Sa se scrie o func care citeste de la tastatura si returneaza valoarea daca aceasta este nr intreg, altfel returneaza 0

def f_verificareNumar(nr):
    if nr.isdigit()==True:
        return nr
    return 0
    
nr=input('Introduceti nr:')
rez=f_verificareNumar(nr)
print(rez)

#sau

def f_verificareNumar(nr):
    try:
        nr2=int(nr)
        return nr2
    except ValueError as e:
#        print('Nu este int',e)
        return 0
    
nr=input('Introduceti nr:')
rez=f_verificareNumar(nr)
print(rez)


#Sa se scrie o func care citeste de la tastatura si returneaza valoarea daca aceasta este nr intreg, altfel returneaza 0

def f_GaussNerecursiv(n):
    summ=0
    for x in range(n+1):
        summ=summ+x
    return summ


def f_GaussRecursiv(n):
    if n==0:
        return n
    return n + f_GaussRecursiv(n-1)
        
def f_SumaPara(n):
    if n==0:
        return n
    if n%2==0:
        return n + f_SumaPara(n-1)
    else:
        pass
        

rez=f_GaussNerecursiv(100)
print(rez)

rez2=f_GaussRecursiv(100)
print(rez2)

rez3=f_SumaPara(100)
print(rez3)


def suma_nrpare(n):
    if n%2!=0: #daca e impar
        n=n-1
    if n==0:
        return n
    if n%2==0:    #daca n este par
        return n+suma_nrpare(n-2)

def suma_nrimpare(n):
    if n%2==0: #daca e par
        n=n-1
    if n<1:
        return n
    if n%2!=0:   #daca n este impar
        return n+suma_nrimpare(n-2)
        
        
rezSumaPara=suma_nrpare(10)
print(rezSumaPara)

rezSumaImpara=suma_nrimpare(10)
print(rezSumaImpara)
