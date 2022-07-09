N = int(input("Digite o número de pessoas detectadas: "))
ultimo_insto = 0
ligada = 0

def tempo(inst, ut, lig):
    if lig == 0:
        lig += 10
    elif inst-ut <= 10:
        lig += (inst - ut)
    else:
        lig += 10
    return lig
      
for i in range(1, N+1):
    insute = int(input("Instante da detecção: "))
    ligada = tempo(insute, ultimo_insto, ligada)
    ultimo_insto = insute


print("A escada ficou ligada por: ", ligada)
