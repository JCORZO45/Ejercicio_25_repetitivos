# Ejercicio 25 hallar la suma de los n primeros numeros

#input 
N=int(input("Digite el valor de N: "))

#processing 
i=1
sum=0
while(i<=N):
    sum=sum+i
    i=i+1

#output 
print(" la suma es : " +str(sum))

#fin 