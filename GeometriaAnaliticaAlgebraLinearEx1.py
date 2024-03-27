from time import sleep
print("Questão 1) Ache as componentes dos vetores u, v, u + v, u - v.")
sleep(1)

# Primeira Parte
print("\nI.")
print("u = ?")
sleep(1)
print("u = cos60°i + sen60°j")
ux = cos(pi/3)
uy = sin(pi/3)
u = vector([ux, uy])

print("u = ", u)
sleep(2)

# Segunda Parte
print("\nII.")
print("v = ?")
sleep(1)
print("v = -cos30°i - sen30°j")
vx = -cos(pi/6)
vy = -sin(pi/6)
v = vector([vx, vy])

print("v = ", v)
sleep(2)

# Terceira Parte
print("\nIII.")
print("u + v = ?")
sleep(1)
print("u + v = (ux + vx)i + (uy + vy)j")
print(f"u + v = ({ux+uy})i + ({uy+vy})j")
sleep(2)

# Quarta Parte
print("\nIV.")
print("u - v = ?")
sleep(1)
print("u - v = (ux - vx)i + (uy - vy)j")
print(f"u - v = ({ux-vx})i + ({uy-vy})j")
sleep(2)

# Conclusão
print("\n\nPortanto,\n\n")
show("u = ", u)
show("v = ", v)
show("u+v = ", u+v)
show("u-v = ", u-v)



