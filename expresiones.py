#La funcion de print () se usa mucho para depurar variables. ****************
#Ejemplo de If else
#Operador de concatenacion '+'
a= 1
b=2.2

if a > b:
    print ("Estamos en buenas ondas.")
elif b < a:

    print ("En que ondas estamos?>>>>>>~~~~~~~2121" +  b)
else:
    print ("En que ondas estamos?>>>>>>~~~~~~~")

#Manera de hacer conversiones a formato String para que puedan ser impresas
# %s == String , %d == Decimal , %f == Float
#Ejemplo de Uso:
#El destino de los valores tiene que estar dentro de la sarta.
#Por igual, antes de pasar valores puedo hacer operaciones en el parentecis
# *(a,b)*
print ("Valores que se deben desplegar %f %d" % (a,b))


#Try-Except:

try:
    a=1
    b=0
    print (b/a)
#Pass es usado cuando es requerido codigo pero no quieres escribir nada
    pass
except Exception as e:
    print("LALALA")

#El raise que me escribe atom no es necesario.
#Puedo usar el raise para hacer exepciones a proposito.
