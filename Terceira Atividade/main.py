from leituraEescrita import *

class gerenciador:
    def __init__(self):
        self.campos_validos = [
            'name', 'album', 'artists', 'track_number',
            'disc_number', 'key', 'mode', 'year', 'explicit'
        ]
        self.idxSec = dict()
        if self.carregarDados()==-1: sys.exit()
        pass
    
    def carregarDados(self):
        arqs = lerArquivos()
        if len(arqs)!=3:
            problema = open('saida.txt','w')
            problema.write('parametros incorretos!') 
        
        dados = open(arqs[0],'r')
        entrada = open(arqs[1],'r')
        try:
            out = open(arqs[2],'r')
            self.saida = arqs[2]
        except FileNotFoundError:
            out = open(arqs[2],'w')
            self.saida=arqs[2]
        erro = False
        if dados==-1:
            problema = open('saida.txt','w')
            problema.write('arquivo de dados não encontrado!') 
            erro=True
        if entrada==-1: 
            problema = open('saida.txt','w')
            problema.write('arquivo de consulta não encontrado!')
            erro=True
        if erro:
            problema.close()
            return -1
        self.dataset=arqs[0]
        self.consulta=arqs[1]
        
        dados.close()
        entrada.close()
        out.close()
        self.condicao, self.procuras = self.retirarDadosConsulta()
        return 1

    def pesquisar(self):
        chaves = self.retirarChaves()
        resultados = list()
        aux1 = list()
        adicional=0
        for pos, pro in enumerate(self.procuras):
            try:
                if pro == 'artists':
                    chaves[pos+adicional] = f"['{chaves[pos+adicional]}']"
                aux1.append(buscaBinIdx(self.idxSec[pro], chaves[pos+adicional]))
            except IndexError:
                pass
            except TypeError:
                for pos1,p in enumerate(pro):
                    if p == 0 or p == 1: break
                    if p == 'artists': chaves[pos+pos1] = f"['{chaves[pos+pos1]}']" 
                    aux1.append(buscaBinIdx(self.idxSec[p], chaves[pos+pos1]))
                    adicional+=1
        if self.condicao != 2:
            # Processamento normal para condições -1, 0, 1
            
            if self.condicao == -1:
                resultados = aux1[0]
            elif self.condicao == 0:
                resultados = listaAnd(aux1)#resultados = listaAnd(aux1, len(self.procuras))
            elif self.condicao == 1:
                resultados = listaOr(aux1)
        else:
            operacao=0
            aux2=list()
            for pos, pro in enumerate(self.procuras):
                idxSecVisado=''
                chaveVisada=''
                contador=0
                foiLista=False
                for PosIn,p in enumerate(pro):
                    if p == 1 or p == 0: break
                    if len(p) != 1: idxSecVisado=p
                    else: break                  
                    contador+=1
                    foiLista=True
                    #if p == 'artists': chaveVisada=f"['{chaves[pos+pro.index(p)]}']"
                    
                    chaveVisada=chaves[PosIn]
                    aux1.append(buscaBinIdx(self.idxSec[idxSecVisado],chaveVisada))
                    if contador==2: 
                        operacao = self.procuras[pos][2]
                        if operacao == 0:
                            aux2 = listaOr(aux1)
                        else:
                            aux2 = listaAnd(aux1)
                if foiLista: continue   
                if pro == 'artists': chaveVisada=f"['{chaves[pos+pro.index(p)]}']"
                ultimaProcura = [aux2.copy(),buscaBinIdx(self.idxSec[pro],chaves[pos+1])]
                if operacao == 0:
                    resultados = listaAnd(ultimaProcura)
                else:
                    resultados = listaOr(ultimaProcura)  
        
        self.exportarRes(resultados)
    
    def exportarRes(self,resultados):
        self.idxPrim = self.carregarIdx('index/Prim/arqPrim.idx')
        final=list()
        for res in resultados:
            rrn = buscaBinaria(self.idxPrim, res)
            final.append(int(rrn)) 
        saida = open(self.saida,'w',encoding='utf-8')
        for i in final:
            saida.write(f'{self.musicas[i].exibirReg()}\n')
        if len(resultados)==0:
            saida.write('Nenhum resultado encontrado!')
        saida.close()
        
    def retirarChaves(self):
        arq = open(self.consulta,'r')
        linhas = arq.readlines()
        chaves=linhas[1].strip().split(',')
        chaves = [c.strip() for c in chaves]
        arq.close()
        return chaves
         
    def retirarDadosConsulta(self):
        consulta = open(self.consulta,'r')
        linhas = consulta.readlines()
        vazio=True
        for pos,f in enumerate(linhas[0]):
            if f!=' ' or not (f=='\n' and pos==0): vazio=False
        if vazio:
            problema = open('saida.txt','w')
            problema.write('arquivo vazio/incompleto!') 
            sys.exit()
        condicao=-1 # -1 se tiver somente um indexsec para procurar, 0 se tever and, 1 se tiver ou
        procuras = list()
        
        try:  
            if ' || ' in linhas[0] and ' & ' in linhas[0]:
                aux = linhas[0].strip() 
                primeiro = 0 if aux.find(' || ') < aux.find(' & ') else 1 
                
                if primeiro == 0:
                    aux = aux.split(' & ')
                    for i in range(len(aux)):
                        if ' || ' in aux[i]:
                            aux[i]= aux[i].split(' || ')
                            aux[i].append(0) # 0 no final do vetor significa que aquele par deve ter o tratamento OR       
                else:
                    aux = aux.split(' || ')
                    for i in range(len(aux)):
                        if ' & ' in aux[i]:
                            aux[i]= aux[i].split(' & ')
                            aux[i].append(1) # 1 no final do vetor significa que aquele par deve ter o tratamento AND
                procuras = aux
                condicao=2
            elif ' & ' in linhas[0]:
                condicao=0
                procuras = linhas[0].strip().split(' & ')            
            elif ' || ' in linhas[0]:
                condicao=1
                procuras = linhas[0].strip().split(' || ')
            else:
                procuras.append(linhas[0].strip())
        except  IndexError:
            problema = open('saida.txt','w')
            problema.write('arquivo vazio/incompleto!') 
            sys.exit()
        for procura in procuras:
            if procura not in self.campos_validos:
                    for p in procura:
                        campoAlt = self.campos_validos+[0,1]
                        if p not in campoAlt:
                            problema = open('saida.txt','w')
                            problema.write('parametros de consulta não disponiveis!') 
                            sys.exit()
            
            try:
                temp = open(f'index/Sec/{procura}.idx','r')
                self.musicas=gerarArqs(self.dataset, inicio=False)
            except FileNotFoundError:
                try:
                    for p in procura:
                        if p == 0 or p == 1: break
                        temp = open(f'index/Sec/{p}.idx','r')
                    self.musicas=gerarArqs(self.dataset, inicio=False)
                except FileNotFoundError:
                    self.musicas=gerarArqs(self.dataset)
                    temp = open(f'index/Sec/{p}.idx','r')
            try:
                self.idxSec[procura] = self.carregarIdx(f'index/Sec/{procura}.idx')
            except (FileNotFoundError,TypeError):
                for p in procura:
                    if p == 0 or p == 1: break
                    self.idxSec[p] = self.carregarIdx(f'index/Sec/{p}.idx')   
            try:       
                temp.close()
            except:
                problema = open('saida.txt','w')
                problema.write('arquivo vazio/incompleto!') 
                sys.exit()
        return condicao,procuras

    def carregarIdx(self, caminho: str):
        registros = []
        try:
            with open(caminho, 'r', encoding='utf-8') as arq:
                for linha in arq:
                    linha = linha.strip()
                    sec, prim = linha.strip().split(',', 1)
                    registros.append((sec, prim))
        except FileNotFoundError:
            return FileNotFoundError
        return registros


def main():
    exemplo = gerenciador()
    exemplo.pesquisar()
main()