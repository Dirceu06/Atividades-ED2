from leitura import Heroi
#retorn = vetor[[chaveheroi],[pos no vetor linhas]]
def gerarVetorKeyEpos(herois : list[Heroi]):
    vet = list()
    for i in range(len(herois)):
        aux=[int(herois[i].key),i]
        vet.append(aux)
    return vet

def HeroiclassParaLinha(heroi : Heroi):
    atributos = vars(heroi)           
    valores = []    
                     
    for valor in atributos.values(): valores.append(str(valor))    

    linha = "|".join(valores) + "\n" 
    return linha

def reescreverReg(vet = 0,herois = 0, arquivo = 0, funcionou = True):
    
    arq = open(arquivo,"w+")
    if funcionou:
        if len(vet) != len(herois):
            print("reescrever reg erro!!!")
            return
        linhas = list()
        linha = "key,Name,Alignment,Gender,EyeColor,Race,HairColor,Publisher,SkinColor,Height,Weight,Intelligence,Strength,Speed,Durability,Power,Combat,Total\n"
        linhas.append(linha)
        for i in range(len(herois)):
            linha = HeroiclassParaLinha(herois[vet[i][1]])
            linhas.append(linha)
        arq.writelines(linhas)
    else:
        linhas = "Arquivo com erro"
        arq.writelines(linhas)
    arq.close()