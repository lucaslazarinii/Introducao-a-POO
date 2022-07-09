contador_cobaias = 0
contador_rato = 0
contador_sapo = 0
contador_coelho = 0
def porcentagens(coelho, rato, sapo):
    t = coelho+rato+sapo
    pcoelho = (coelho*100)/t
    prato = (rato*100)/t
    psapo = (sapo*100)/t
    return pcoelho, prato, psapo
N = int(input("Digite a quantidade de experimentos realizados: "))
print("\nSiglas a serem utilizadas:")
print("R = Rato \nS = Sapo \nC = Coelho\n")
for i in range(0, N):
    r = False
    nmr, anm = input("Digite a quantidade de cobaias e a sigla da cobaia: ").upper().split()
    nmr = int(nmr)
    contador_cobaias += nmr
    if anm == "R":
        contador_rato += 1*nmr
    elif anm == "S":
        contador_sapo += 1*nmr
    elif anm == "C":
        contador_coelho += 1*nmr
c1, c2, c3 = porcentagens(contador_coelho, contador_rato, contador_sapo)
print("\nTotal: {} cobaias".format(contador_cobaias))
print("Total de coelhos: {}".format(contador_coelho))
print("Total de ratos: {}".format(contador_rato))
print("Total de sapos: {}".format(contador_sapo))
print("Percentual de coelhos: {:.2f}%".format(c1))
print("Percentual de ratos: {:.2f}%".format(c2))
print("Percentual de sapos: {:.2f}%".format(c3))



    
