from Receita import Receita
import json
import os

#Cria uma receita com base num dicionario
def to_receita(dic):
    return Receita(dic["nome"],dic["ingredientes"])

#Retorna a lista de todas as receitas
def lista_receitas():
    file_path = "Livro_De_Receitas.json"  
    recipes = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                recipe_data = json.loads(line.strip())  
                recipes.append(to_receita(recipe_data))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return recipes

#Mostra todas as receitas no Livro
def show_receitas():
    if not lista_receitas():
        print("nao ha receitas na lista") 
    for r in lista_receitas():
        r.show_receita()

#Guarda uma receita no Livro
def saveReceita(r):
    with open("Livro_De_Receitas.json", 'a') as file:
        l = lista_receitas()
        if not is_saved(r):
            # Create a dictionary representing the recipe
            recipe_data = {
                'nome': r.name(),
                'ingredientes': r.ingredientes()
            }
            file.write(json.dumps(recipe_data) + "\n")
            print(f"Receita {r.name()} Guardada")
        else:
            print(f"Receita {r.name()} já estava guardada")

#Verifica se uma receita ja esta guardada 
def is_saved(r):
    name = r.name()
    with open("Livro_De_Receitas.json", 'r') as file:
        for line in file:  
            x = json.loads(line)
            if x['nome'] == name:
                return True
        return False

#Apaga todas as receitas
def limpar_livro():
    os.remove("Livro_De_Receitas.json")

#Remove receitas pelo nome
def remover_receita(nome):
        with open("Livro_De_Receitas.json", 'r') as file:
            lines = file.readlines()

        with open("Livro_De_Receitas.json", 'w') as file:
            for line in lines:
                line1 = json.loads(line)
                if line1["nome"] != nome: 
                    file.write(line)

        print(f"{nome} foi removida do Livro de Receitas")

#Pesquisa de receitas pelo nome
def search_receita(nome): 
    found = False
    with open("Livro_De_Receitas.json", 'r') as file:
        for line in file:
            dict = json.loads(line)
            if nome == dict["nome"]:
                Receita.show_receita(to_receita(dict))
                found = True
    if not found:
        print("Nao foi possivel encontrar a receita")

#Procura Receitas parecidas (3 ou mais ingredientes em comum)
def search_similar(r):
    lista_recipes = []
    with open("Livro_De_Receitas.json", 'r') as file:
        for line in file:
            recipe = to_receita(json.loads(line))
            if (em_comum(recipe, r) >= 3 and recipe.name() != r.name()):
                lista_recipes.append(recipe)
    if lista_recipes:
        if (len(lista_recipes) == 1):
            print("Aqui esta uma receita semelhante:")
            lista_recipes[0].show_receita()
        else:
            print("Aqui estao algumas receitas semelhantes:")
            for recipe in lista_recipes:
                recipe.show_receita()
    else:
        print("Nao foi possivel encontrar receitas suficientemente parecidas")

#Verifica quantos ingredientes em comum entre duas receitas
def em_comum(r1, r2):
    i1 = r1.ingredientes()
    i2 = r2.ingredientes()
    n = 0
    for ing in i1:
        if ing in i2:
            n += 1
    return n

#Cria uma lista de ingredientes por input do user
def nova_lista():
    ret = []
    while True:
        x = input("Adicione um ingrediente(caso tenha terminado deixe em branco) \n")
        if x != "":
            ret.append(x)
        else: 
            break
    return ret

#Cria e guarda uma nova receita atraves de input do user
def nova_receita():
    nome = input("Qual é o nome da Receita? \n")
    ingredientes = nova_lista()
    r = Receita(nome, ingredientes)
    r.show_receita()
    saveReceita(r)