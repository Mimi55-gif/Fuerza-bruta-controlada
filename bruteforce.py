import time, itertools

pal= "eS0%"
abcd= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYabcdefghijklmnñopqrstuvwxyz.:,;¡!¿?+*}{%$#@1234567890 '
cmax= 4

print("Buscando contraseña")

def combinaciones(abcd, cmax):
    for largo in range(1,cmax+1):
        for comb in itertools.product(abcd,repeat=largo):
            yield ''.join(comb)

def buscar(pal,abcd,cmax):
    inicio_t = time.time()
    intentos = 0
    for comb in combinaciones(abcd,cmax):
        intentos+=1
        if comb==pal:
            fin_t=time.time()
            proc_t=fin_t-inicio_t
            return comb,intentos,proc_t
        
contraseña_e, intentos, tiempo = buscar(pal,abcd,cmax)

print("Contraseña encontrada: "+contraseña_e)
print(f"Se han realizado {intentos} intentos")
print(f"La busqueda ha tardado {tiempo:.6f} segundos")
