

#Functions With Outputs
def format_name(f_name, l_name):
    fname = f_name.title() #See .title() muudab kõikide sõnade esimesed täheda suureks in string
    lname = l_name.title()
    print(fname," " ,lname)

format_name("MaRkO", "UsSiSoO")


#Näidis function
a=5                 #Defineerin muutuja A funktsiooni jaoks
def my_function(a): #Defineerib uue funktsiooni "my_function"
    b = a+a         #Teeb midagi muutujaga A et saada B
    return b        #Muudab muutuja B muutujaks A 
print(my_function(a))   #prindib muutuja A peale "my_function" tegemist.