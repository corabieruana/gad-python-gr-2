my_list=[7,8,9,2,3,1,4,10,5,6]
print("Primul punct (afisare lista): ")
print(my_list)

my_list2=[7,8,9,2,3,1,4,10,5,6]
print("Al doilea punct (ordonare cresc): ")
my_list_aux=my_list2   #sau my_list_aux=my_list2.copy()    #sau my_list_aux=list(my_list2)
my_list_aux.sort()
print(my_list_aux)


my_list3=[7,8,9,2,3,1,4,10,5,6]
print("Al treilea punct (ordonare descr): ")
my_list_aux2=my_list3
my_list_aux2.sort()
my_list_aux2.reverse()
print(my_list_aux2)

my_list4=[7,8,9,2,3,1,4,10,5,6]
print("Al patrulea punct (afisare nr pare):")
my_list4.sort()
lista_nrpare=my_list4[1::2]
print(lista_nrpare)
#sau
my_list4=[7,8,9,2,3,1,4,10,5,6]
my_list4.sort()
my_list4.pop(0)
print("Al patrulea punct (afisare nr pare-metoda2):")
lista_nrpare=my_list4[::2]
print(lista_nrpare)
#sau
print("Metoda cu for: ")
my_list4=[7,8,9,2,3,1,4,10,5,6]
for x in my_list4:
    if x%2==0:
        print(x)


my_list4=[7,8,9,2,3,1,4,10,5,6]
print("Al cincilea punct (afisare nr impare):")
my_list4.sort()
lista_nrimpare=my_list4[::2]
print(lista_nrimpare)

my_list4=[7,8,9,2,3,1,4,10,5,6]
print("Al saselea punct (afisare el multiplu de 3):")
my_list4.sort()
lista_nrmultipluTrei=my_list4[2::3]
print(lista_nrmultipluTrei)




