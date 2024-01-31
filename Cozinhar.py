from Receita import Receita
import Livro
import json

def listaDasCompras(str):
    file = open("Livro_De_Receitas.json", "r")
    for line in file:
        x = json.loads(line)
        if x["nome"] == str:
            print("=" * 30)
            print("Comprar: \n")
            for n in x["ingredientes"]:
                    print(f"- {n}")
            print("=" * 30)
            break

def sugere(ingredientes):
    sugestoes = []
    for r in Livro.lista_receitas():
        if all(ing in ingredientes for ing in r.ingredientes()):
            sugestoes.append(r)
    if not sugestoes: 
        print("Nao tenho sugestoes a dar com esses ingredientes, devias ir as compras")
    else:
        print("Sugiro o seguinte:")
        for s in sugestoes:
            s.show_receita()
