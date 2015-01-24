''' 
	tipos nativos

	Lista -> array
	Tupla -> array constante
	Rango -> lista de valores numericos range(10)	
'''

lista =[1,2,3]
lista_b=[4,5,6]
lista_c=["h","o","l","a"]
lista.append(lista_c)
lista.extend(lista_b)

# print(lista)

# name=raw_input('Nombre: ')

# print("El "+name+" es gay")
'''
---------------------------------
>>> a=dict(one=1,two=2)
>>> b={"one":1,"two":2}
>>> c=dict(zip([one=1]))
---------------------------------
'''


'''
a={
	"array": [1,2,3],
	"string": "hola mundo",
	"number": 1,
	"objeto": {
		"string": "hola"
	}
}

for k,v in a.iteritems():
	print(k)
	print(v)
'''

def fib(n):
	a=0
	b=1
	while a<n
		print(a, end=" ")
		a, b =b, a+b
	print()

fib(10)

'''
def funcion(arguments,keyword_argument,*arg, **kwargs)
	- arguments: 
	- keyword_argument: asigna los argumentos por nombre especificado
	- *arg: aceptar una lista de argumentos
	- **kwargs: 
'''