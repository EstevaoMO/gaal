from time import sleep

#Questão 7
print("7) Num hexágono regular abaixo, a medida de cada lado vale 2. Calcular |𝐴 − 𝐵| × |𝐶 − 𝐵|\n")
sleep(2)

#Introdução
print("I.")
BA_modulo = 2
print("Podemos chamar A - B de vetor BA\n")
sleep(2)
BC_modulo = 2
print("Bem como C - B de vetor BC\n")
sleep(2)

#Análise Geométrica
print("II.")
print("Temos por entendimento que a soma dos ângulos internos de um hexágono equivale a 720°. \nPara tomar o ângulo entre os vetores, basta dividir por 6.\n")
sleep(2)
angulo_entreBABC = 2*pi/3
print("Assim, 120° é o ângulo entre BA e BC\n")

#Resolução
print("III.")
print("|BA × BC| = |BA| × |BC| x sen 120°\n")
sleep(2)

modulo_do_prodvetorial = BA_modulo * BC_modulo * sin(angulo_entreBABC)
sleep(1)
print("Portanto, o modulo do produto vetorial equivale a ")
sleep(2)
show(modulo_do_prodvetorial)
