import sys
import os
import csv

class Musica:
    def __init__(self, RRN, id, name, album, album_id, artists, artist_ids,
                 track_number, disc_number, explicit, danceability, energy,
                 key, loudness, mode, speechiness, acousticness,
                 instrumentalness, liveness, valence, tempo, duration_ms,
                 time_signature, year, release_date):
        self.RRN = RRN
        self.id = id
        self.name = name
        self.album = album
        self.album_id = album_id
        self.artists = artists
        self.artist_ids = artist_ids
        self.track_number = track_number
        self.disc_number = disc_number
        self.explicit = explicit
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.time_signature = time_signature
        self.year = year
        self.release_date = release_date
    def exibirReg(self):
        valores = []
        for attr, value in self.__dict__.items():
            if attr == "RRN": 
                continue
            valores.append(str(value))
        return ",".join(valores)
      
def lerArquivos():
    lista = sys.argv
    arqDados = lista[1]
    arqConsulta = lista[2]
    arqSaida = lista[3]
    arqs = [arqDados, arqConsulta, arqSaida]
    return arqs

def criarEscreverArqSec(musicas:list):
    os.makedirs("index/Sec", exist_ok=True)
    campos_validos = [
        'name', 'album', 'artists', 'track_number',
        'disc_number', 'key', 'mode', 'year', 'explicit'
    ]

    for campo in campos_validos:
        reg = []
        for m in musicas:
            chave_sec = getattr(m, campo, "-")
            chave_prim = m.id
            reg.append((str(chave_sec), str(chave_prim)))

        reg.sort(key=lambda x: (x[0].lower(), x[1].lower()))

        with open(f"index/Sec/{campo}.idx", "w", encoding="utf-8") as f:
            for sec, prim in reg:
                f.write(f"{sec},{prim}\n")

def criarEscreverArqPrim(musicas:list):
    os.makedirs("index/Prim", exist_ok=True)
    reg = []
    for m in musicas:
        reg.append((m.id, m.RRN))

    reg.sort(key=lambda x: x[0].lower())

    with open("index/Prim/arqPrim.idx", "w", encoding="utf-8") as f:
        for id, rrn in reg:
            f.write(f"{id},{rrn}\n")      

def gerarArqs(arquivoCSV,inicio=True):
    try:
        with open(arquivoCSV, "r", encoding="utf-8") as arq:
            leitor = csv.reader(arq)
            linhas = list(leitor)
            
    except FileNotFoundError:
        print(f"Arquivo {arquivoCSV} não encontrado!")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao abrir arquivo: {e}")
        sys.exit(1)
    
    if not linhas:
        print("Arquivo vazio!")
        return
    
    musicas = []
    
    for numero_linha, campos in enumerate(linhas[1:], start=1):
        if not campos:  continue #pula linhas vazias
            
        campos = [campo if campo else "-" for campo in campos]
        
        try:
            rrn = str(numero_linha - 1)
            campos_com_rrn = [rrn] + campos
            
            song = Musica(*campos_com_rrn)
            musicas.append(song)
            
        except TypeError as e:
            print(f"Erro ao criar Musica na linha {numero_linha}: {e}")
            print(f"Campos: {campos_com_rrn}")
            continue
        except Exception as e:
            print(f"Erro inesperado na linha {numero_linha}: {e}")
            continue
    if inicio:
        criarEscreverArqSec(musicas)
        criarEscreverArqPrim(musicas)
    
    return musicas

def buscaBinaria(lista,chave):
    #retorna o indice do elemento que bate com a chave
    chave = str(chave).lower()
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valor = str(lista[meio][0]).lower()

        if valor == chave:
            return lista[meio][1]
        elif chave < valor:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return -1
    
def buscaBinIdx(lista,chave):
    #retorna uma lista com a chave primaria dos elementos que batem com a chave
    chave = str(chave).lower()
    esquerda, direita = 0, len(lista) - 1
    achou = -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valor = str(lista[meio][0]).lower()

        if valor.startswith(chave):
            achou = lista[meio][1]
            achouidx = meio
            direita = meio - 1
        elif chave < valor:
            direita = meio - 1
        else:
            esquerda = meio + 1

    if achou == -1:
        return []

    resultados = [achou]

    i = achouidx - 1
    while i >= 0 and str(lista[i][0]).lower().startswith(chave):
        resultados.append(lista[i][1])
        i -= 1

    i = achouidx + 1
    while i < len(lista) and str(lista[i][0]).lower().startswith(chave):
        resultados.append(lista[i][1])
        i += 1

    resultados.sort()
    return resultados

def listaAnd(listas):
    if not listas:
        return []
    
    # Usar Counter do Python (hash map O(n))
    from collections import Counter
    
    contador = Counter()
    for lista in listas:
        # Converte para set para remover dups da mesma lista
        contador.update(set(lista))
    
    # Só elementos que aparecem em TODAS as listas
    n_listas = len(listas)
    return [elem for elem, count in contador.items() if count == n_listas]

def listaOr(listas):
    # Usar set para união O(n)
    resultado = set()
    for lista in listas:
        resultado.update(lista)
    return list(resultado)