print('Hola Mundo!2022')
x= '2'
print(type(x))
# class 'str'
x = int(x)
print(type(x))
# class 'int'
y = int(2.8)
print(y)

## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
a = 5
print(a)

# 2) Imprimir el tipo de dato de la constante 8.5
b = 8.5
print(type(b))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(a))

# 4) Crear una variable que contenga tu nombre
c = 'Alex'

# 5) Crear una variable que contenga un número complejo
d = 1 + 5j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(d))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
e = 3.1415
print(e)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
f = 'True'
g = True


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(f))
print(g)

# 10) Asignar a una variable, la suma de un número entero y otro decimal
h = 5 + 4.3

# 11) Realizar una operación de suma de números complejos
i = 4 + 3j
j = 5 + 2j
suma = i + j
print(suma)

# 12) Realizar una operación de suma de un número real y otro complejo
i = 4.5
j = 5 + 2j
suma = i + j
print(suma)

# 13) Realizar una operación de multiplicación

print(2*2)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
div = 27 / 4
print(div)

# 16) De la división anterior solamente mostrar la parte entera
div_ent = 27 // 4
print(div_ent)

# 17) De la división de 27 entre 4 mostrar solamente el resto
res = 27 % 4
print(res)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4 * div_ent + res)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
a1 = 'Yo '
a2 = 'Veo'
print(a1 + a2)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print(2 == 2.)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(2 == int(2.))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3.8')

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
x = 3
x -= 1
print(x)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1 << 2)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# 26) Realizar una operación válida entre valores de tipo entero y string

print (2 + int('2'))