"""
@autor: Gabriel Marcos Magalhães
Arquivo onde estão escritas as funções relacionadas a construção de uma interface gráfica para
a aplicação em Python
"""
from tkinter import Tk, Frame, Label, LEFT, RIGHT, Button, Entry
# Bibliotecas desenvolvidas para o projeto
from userData6 import generate_dictionary, changeFileDict

class Application:
    def __init__(self, master):
        """
        Função responsável pela inicialização
        """
        self.janela_principal = master
        self.fontePadrao = ("Arial", "11")
        self.fonteBotoes = ("Arial", "10")

    def interface(self):
        """
        Função responsável pela construção da interface 
        """
        self.define_titulo() # Definição do título interno da janela
        self.leitura_magneticPropeties() # Leitura dos dados no magneticProperties
        self.leitura_ControlDict() # Leitura dos dados no controlDict
        self.gerar_jsonIntf() # Gerar json via interface
        self.botoes_finais() # Botões para operações finais

    def define_titulo(self):
        """
        Função responsável pela construção da parte relativa ao título na interface
        """
        # Construção do container para título da janela
        self.primeiroContainer = Frame(self.janela_principal)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
        # Atribuição do título dentro da janela (1a informação exibida)
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = self.fontePadrao
        self.titulo.pack()

    def leitura_ControlDict(self):
        """
        Função responsável pela construção da parte relacionada ao controlDict
        """
        # Construção do container para a entrada do tempo final desejado
        self.segundoContainer = Frame(self.janela_principal)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()

        # Informação exibida ao lado do campo para entrada do tempo final
        self.tfLabel = Label(self.segundoContainer,text="Tempo final: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada do tempo final
        self.tf = Entry(self.segundoContainer)
        self.tf["width"] = 30
        self.tf["font"] = self.fontePadrao
        self.tf.pack(side=LEFT)

    def leitura_magneticPropeties(self):
        """
        Função responsável pela construção da parte relacionada ao magneticProperties
        """
        # Construção do container para a entrada de chi0
        self.segundoContainer = Frame(self.janela_principal)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()
        # Construção do container para a entrada de beta_m
        self.terceiroContainer = Frame(self.janela_principal)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        # Construção do container para a entrada de Hmax
        self.quartoContainer = Frame(self.janela_principal)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()
        # Construção do container para a entrada de mag_height
        self.quintoContainer = Frame(self.janela_principal)
        self.quintoContainer["padx"] = 20
        self.quintoContainer["pady"] = 10
        self.quintoContainer.pack()


        # Informação exibida ao lado do campo para entrada de chi0
        self.chi0Label = Label(self.segundoContainer,text="Magnetic susceptibility (EFH3 TDS) (chi0): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de chi0
        self.chi0 = Entry(self.segundoContainer)
        self.chi0["width"] = 30
        self.chi0["font"] = self.fontePadrao
        self.chi0.pack(side=LEFT)
        # Informação exibida ao lado do campo para entrada de beta_m
        self.betamLabel = Label(self.terceiroContainer, text="Pyromagnetic coefficient (beta_m): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de beta_m
        self.betam = Entry(self.terceiroContainer)
        self.betam["width"] = 30
        self.betam["font"] = self.fontePadrao
        self.betam.pack(side=LEFT)
        # Informação exibida ao lado do campo para entrada de Hmax
        self.HmaxLabel = Label(self.quartoContainer, text="Maximum applied field (Hmax): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de Hmax
        self.Hmax = Entry(self.quartoContainer)
        self.Hmax["width"] = 30
        self.Hmax["font"] = self.fontePadrao
        self.Hmax.pack(side=LEFT)
        # Informação exibida ao lado do campo para entrada de mag_height
        self.magHLabel = Label(self.quintoContainer, text="Magnet height (mag_height): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de mag_height
        self.magH = Entry(self.quintoContainer)
        self.magH["width"] = 30
        self.magH["font"] = self.fontePadrao
        self.magH.pack(side=RIGHT)

    def gerar_jsonIntf(self):
        """
        Função responsável pela construção da parte relacionada a geraçao do json
        via interface
        """
        # Construção do container para o botão de geraçao do json
        self.validationContainer = Frame(self.janela_principal)
        self.validationContainer["pady"] = 2
        self.validationContainer.pack()
        # Construção do botão de geraçao do json
        self.autenticar = Button(self.validationContainer)
        self.autenticar["text"] = "Gerar Json"
        self.autenticar["font"] = self.fonteBotoes
        self.autenticar["width"] = 12
        # Chamada da função utilizada para geraçao do json
        self.autenticar["command"] = self.gera_json
        self.autenticar.pack()

    def botoes_finais(self):
        """
        Função responsável pela construção da parte relacionada aos botões finais na interface:
        - Geração de um relatório PDF
        - Geração de gráfico HTML com o retorno acumulado do fundo e do CDI e retorno diário do fundo
        - Encerramento da aplicação)
        """
        # Construção do container para os botões inferiores:
        self.ultimoContainer = Frame(self.janela_principal)
        self.ultimoContainer["pady"] = 2
        self.ultimoContainer.pack()

        # Construção do botão para geração do setup (substituiçao dos valores)
        self.relatorio = Button(self.ultimoContainer)
        self.relatorio["text"] = "Gerar Setup"
        self.relatorio["font"] = self.fonteBotoes
        self.relatorio["width"] = 12
        # Chamada da função utilizada para geração do setup (substituiçao dos valores)
        self.relatorio["command"] = self.gera_setup
        self.relatorio.pack(side=LEFT)
        # Construção do botão para executar a simulaçao
        self.reset = Button(self.ultimoContainer)
        self.reset["text"] = "Executar simulação"
        self.reset["font"] = self.fonteBotoes
        self.reset["width"] = 20
        # Chamada da função utilizada para executar a simulaçao
        self.reset["command"] = self.simulation
        self.reset.pack(side=LEFT)
        # Construção do botão para encerramento da interface
        self.encerrar = Button(self.ultimoContainer)
        self.encerrar["text"] = "Sair"
        self.encerrar["font"] = self.fonteBotoes
        self.encerrar["width"] = 12
        # Chamada da função utilizada para encerrar a janela da aplicação
        self.encerrar["command"] = self.janela_principal.quit
        self.encerrar.pack()

    def gera_json(self):
        import json
        """
        Função utilizada para geração do json com os dados
        """
        inputDict = {}
        inputDict["chi0"] = self.chi0.get()
        inputDict["betam"] = self.betam.get()
        inputDict["Hmax"] = self.Hmax.get()
        inputDict["mag_height"] = self.magH.get()
        inputDict["tf"] = self.tf.get()

        # Convert dictionary to JSON string
        json_string = json.dumps(inputDict, indent=4)
        self.outJson="inputInterface.json"

        with open(self.outJson,"w") as f:
            f.write(json_string)
        f.close()

    def gera_setup(self):
        import json
        """
        Função utilizada para substituiçoes de valores do setup
        """
        # Gera o json caso o usuario se esqueça
        self.gera_json
        # Le o json gerado
        with open(self.outJson, 'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary(data)
        changeFileDict(inputDict)

    # Método para gerar o relatório
    def simulation(self):
        """
        Função utilizada para geração de um relatório PDF
        """
        import os

        os.system("./Allclean")
        os.system("./Allpre")
        os.system("./Allrun &")


def main():
    """
    Função principal. Inicializa a aplicação e constrói a interface
    """
    root = Tk()
    root.title('fhdFoam') # Título na barra superior da janela principal
    zaragui = Application(root) # Inicialização
    zaragui.interface() # Execução da interface
    root.mainloop()

if __name__ == "__main__":
    main()