class Receita:
    def __init__(self, nome, lista_ingredientes):
        self.nome = nome
        self.lista_ingredientes = lista_ingredientes
    
    def name(self): 
        return self.nome

    def ingredientes(self):
        return self.lista_ingredientes

    def show_lista(self):
        separator = ", "
        result_string = separator.join(self.lista_ingredientes)
        return ("["+ result_string +"]")
            
    def show_receita(self):
        print("=" * 30)
        print(f"Receita: {self.nome} \n Ingredientes:")
        for n in self.lista_ingredientes:
            print(f"- {n}") 
        print("=" * 30)

