from math import sqrt
import requests

def euclidiana(base, usuario1, usuario2):
    si = {}
    for item in base[usuario1]:
       if item in base[usuario2]: si[item] = 1

    if len(si) == 0: return 0

    soma = sum([pow(base[usuario1][item] - base[usuario2][item], 2)
                for item in base[usuario1] if item in base[usuario2]])
    return 1/(1 + sqrt(soma))


def getSimilares(base, usuario):
    similaridade = [(euclidiana(base, usuario, outro), outro)
                    for outro in base if outro != usuario]
    similaridade.sort()
    return melhorRecomendacao(similaridade[0:30],usuario)

def melhorRecomendacao(base,usuario):
    sname = usuario
    headers = {"x-rapidapi-key":"94f454f271mshf275648a95e2a8dp1e6250jsnce28684e324a"}
    userRecomendacao = dict()
    fname = ""
    for dado in base:
        fname = dado[1]
        req = requests.get(f"https://love-calculator.p.rapidapi.com/getPercentage?sname={sname}&fname=f{fname}", headers=headers)
        porcentagem = float(req.json()["percentage"])
        userRecomendacao[dado[1]] = round(porcentagem/(dado[0]+1),2)
    return ordenaDict(userRecomendacao)

def ordenaDict(dict):
    userRecomendacao = {}
    for i in sorted(dict, key = dict.get):
        userRecomendacao[i] = dict[i]
    return userRecomendacao