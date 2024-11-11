import tkinter as tk
from tkinter import simpledialog, messagebox, Tk, Frame, Label, LEFT, RIGHT, Button, Entry,font

import json

class Main_wind:
    def __init__(self, root_1):
        self.root_1 = root_1
        self.root_1.title("mhtFoam")
        self.fontePadrao = ("Adobe Myungjo Std M", "11")
        self.fonteBotoes = ("Arial", "10")
        #self.root_1["pady"]=40
        #self.root_1["padx"]=40
        
    def interface(self):
        self.botoes_main_wind()
        self.define_titulo()
        #self.leitura_blockMeshDict()
        #self.gerar_jsonIntf_malha()
        #self.parametro_window()
        
        
        
    def define_titulo(self):
        """
        Função responsável pela construção da parte relativa ao título na interface
        """
        # Construção do container para título da janela
        self.primeiroContainer = Frame(root_1)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer["padx"] = 20
        self.primeiroContainer.pack()
        
        #Texto da intro do mhtFoam
        texto1= """O solver mhtFoam simula o processo de magnetohipertermia
aplicado a tratamento de tumores. Entre com as informações
do domínio de cáculo/malha e com as informações dos tumores
através dos botões acima.

v 1.0"""


        # Atribuição do título dentro da janela (1a informação exibida)
        self.titulo = Label(self.primeiroContainer, text=texto1)
        self.titulo["font"] = self.fontePadrao
        self.titulo.pack()
        self.titulo["pady"]=5
        self.titulo["padx"]=5
        self.titulo["justify"]=tk.CENTER
    def botoes_main_wind(self):
        # Botão malha

        self.segundoContainer = Frame(root_1)
        self.segundoContainer["pady"] = 20
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.malha = Button(self.segundoContainer)
        self.malha["text"] = "Parâmetros da malha"
        self.malha["font"] = self.fonteBotoes
        self.malha["width"] = 20
        self.malha["pady"] = 10
       
        self.malha["command"] = self.leitura_blockMeshDict
        self.malha.pack(side=LEFT)
        #self.leitura_blockMeshDict()
        
        # Botão tempo
        
        self.tempo = Button(self.segundoContainer)
        self.tempo["text"] = "Parâmetros temporais"
        self.tempo["font"] = self.fonteBotoes
        self.tempo["width"] = 20
        self.tempo["pady"] = 10
       
        self.tempo["command"] = self.leitura_ControlDict
        self.tempo.pack(side=LEFT)
       
        # Botão tumor
        
        self.tumor = Button(self.segundoContainer)
        self.tumor["text"] = "Parâmetros dos tumores"
        self.tumor["font"] = self.fonteBotoes
        self.tumor["width"] = 20
        self.tumor["pady"] = 10
       
        self.tumor["command"] = self.tumors
        self.tumor.pack(side=RIGHT)
        
        
    def leitura_ControlDict(self):
        """
        Função responsável pela construção da parte relacionada ao controlDict
        """
        #parametro_window2 = tk.Toplevel(root_1)
        #parametro_window2.title("Parâmetros temporais")
        # Construção do container para a entrada do tempo final desejado
        #self.segundo3Container = Frame(parametro_window2)
        #self.segundo3Container["padx"] = 20
        #self.segundo3Container["pady"] = 10
        #self.segundo3Container.pack()
        
        # Construção do container para a entrada do time step desejado
        #self.terceiro3Container = Frame(parametro_window2)
        #self.terceiro3Container["padx"] = 20
        #self.terceiro3Container["pady"] = 10
        #self.terceiro3Container.pack()

        # Informação exibida ao lado do campo para entrada do tempo final
        
        #self.endtimeLabel = Label(self.segundo3Container,text="Tempo final: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada do tempo final
        #self.endtime = Entry(self.segundo3Container)
        #self.endtime["width"] = 30
        #self.endtime["font"] = self.fontePadrao
        #self.endtime.pack(side=LEFT)
        self.data={}
        
        endtime = simpledialog.askfloat("Parâmetros temporais", "Tempo final:", minvalue=0, maxvalue=1000)
        timestep = simpledialog.askfloat("Parâmetros temporais", "Time step:", minvalue=0, maxvalue=1000)
        if endtime is not None:
            self.data["endtime"] = endtime
        if timestep is not None:
            self.data["timestep"] = timestep
        with open("inputDict_controlDict.json", "w") as arquivo:
            json.dump(self.data, arquivo, indent=4)
            
      
        
        # Informação exibida ao lado do campo para entrada do time step
        
        #self.timestepLabel = Label(self.terceiro3Container,text="Time step: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada do time step
        #self.timestep = Entry(self.terceiro3Container)
        #self.timestep["width"] = 30
        #self.timestep["font"] = self.fontePadrao
        #self.timestep.pack(side=LEFT)
    
        
    def leitura_blockMeshDict(self):
        #self.gerar_jsonIntf_malha()
        """
        Função responsável pela construção da parte relacionada ao blockMeshDict
        """
        parametro_window = tk.Toplevel(root_1)
        parametro_window.title("parâmetros do Domínio de Cálculo")
        
        # Construção do container para a entrada de xmax
        self.segundo2Container = Frame(parametro_window)
        self.segundo2Container["padx"] = 20
        self.segundo2Container["pady"] = 10
        self.segundo2Container.pack()
        # Construção do container para a entrada de ymax
        self.terceiro2Container = Frame(parametro_window)
        self.terceiro2Container["pady"] = 10
        self.terceiro2Container["padx"] = 20
        self.terceiro2Container.pack()
        # Construção do container para a entrada de zmax
        self.quarto2Container = Frame(parametro_window)
        self.quarto2Container["padx"] = 20
        self.quarto2Container["pady"] = 10
        self.quarto2Container.pack()
        # Construção do container para a entrada de xnode
        self.quinto2Container = Frame(parametro_window)
        self.quinto2Container["padx"] = 20
        self.quinto2Container["pady"] = 10
        self.quinto2Container.pack()
        # Construção do container para a entrada de ynode
        self.sexto2Container = Frame(parametro_window)
        self.sexto2Container["padx"] = 20
        self.sexto2Container["pady"] = 10
        self.sexto2Container.pack()
        # Construção do container para a entrada de znode
        self.setimo2Container = Frame(parametro_window)
        self.setimo2Container["padx"] = 20
        self.setimo2Container["pady"] = 10
        self.setimo2Container.pack()
        # Construção do container para a entrada de endTime
        self.oitavo2Container = Frame(parametro_window)
        self.oitavo2Container["padx"] = 20
        self.oitavo2Container["pady"] = 10
        self.oitavo2Container.pack()
        
        #########################################################
        
        # Informação exibida ao lado do campo para entrada de xmax
        
        self.xmaxLabel = Label(self.segundo2Container,text="size of the domain in x direction (m): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de xmax
        self.xmax = Entry(self.segundo2Container)
        self.xmax["width"] = 30
        self.xmax["font"] = self.fontePadrao
        self.xmax.pack(side=LEFT)
        
        # Informação exibida ao lado do campo para entrada de ymax
        
        self.ymaxLabel = Label(self.terceiro2Container, text="size of the domain in y direction (m): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de ymax
        self.ymax = Entry(self.terceiro2Container)
        self.ymax["width"] = 30
        self.ymax["font"] = self.fontePadrao
        self.ymax.pack(side=LEFT)
        
        # Informação exibida ao lado do campo para entrada de zmax
        
        self.zmaxLabel = Label(self.quarto2Container, text="size of the domain in z direction (m): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de zmax
        self.zmax = Entry(self.quarto2Container)
        self.zmax["width"] = 30
        self.zmax["font"] = self.fontePadrao
        self.zmax.pack(side=LEFT)
        
        # Informação exibida ao lado do campo para entrada de xnode
        
        self.xnodeLabel = Label(self.quinto2Container, text="Amount of nodes in the x direction: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de xnode
        self.xnode = Entry(self.quinto2Container)
        self.xnode["width"] = 30
        self.xnode["font"] = self.fontePadrao
        self.xnode.pack(side=RIGHT)
        
        # Informação exibida ao lado do campo para entrada de ynode
        
        self.ynodeLabel = Label(self.sexto2Container, text="Amount of nodes in the y direction: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de ynode
        self.ynode = Entry(self.sexto2Container)
        self.ynode["width"] = 30
        self.ynode["font"] = self.fontePadrao
        self.ynode.pack(side=RIGHT)
        
        # Informação exibida ao lado do campo para entrada de znode
        
        self.znodeLabel = Label(self.setimo2Container, text="Amount of nodes in the z direction: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada de znode
        self.znode = Entry(self.setimo2Container)
        self.znode["width"] = 30
        self.znode["font"] = self.fontePadrao
        self.znode.pack(side=RIGHT)
        #botão de gerar jason
        
        self.autenticar = Button(self.oitavo2Container)
        self.autenticar["text"] = "Gerar Json"
        self.autenticar["font"] = self.fonteBotoes
        self.autenticar["width"] = 12
        # Chamada da função utilizada para geraçao do json
        self.autenticar["command"] = self.gera_json_malha
        self.autenticar.pack(side=RIGHT)
        
    # Blocos de geração de arquivos Jason
   

    def gera_json_malha(self):
        import json
        
        inputDict_blockMeshDict = {}
        inputDict_blockMeshDict["xmax"] = self.xmax.get()
        inputDict_blockMeshDict["ymax"] = self.ymax.get()
        inputDict_blockMeshDict["zmax"] = self.zmax.get()
        inputDict_blockMeshDict["xnode"] = self.xnode.get()
        inputDict_blockMeshDict["ynode"] = self.ynode.get()
        inputDict_blockMeshDict["znode"] = self.znode.get()
    
        json_string = json.dumps(inputDict_blockMeshDict, indent=4)
        self.outJson="inputDict_blockMeshDict.json"
        
        json_string = json.dumps(inputDict_blockMeshDict, indent=4)
        self.outJson="inputDict_blockMeshDict.json"
        with open(self.outJson,"w") as f:
            f.write(json_string)
        f.close()

    def tumors(self):
        #parametro_window3 = tk.Toplevel(root_1)
        #parametro_window3.title("Parâmetros dos tumores")
        
        # Construção do container para a entrada de xmax
        
        tumor_count = simpledialog.askinteger("Parâmetros dos tumores", "How many tumors?")
        #tumor_count.geometry("300x150")
    
    

# Inicializa a interface gráfica
root_1 = tk.Tk()
app = Main_wind(root_1)
zaragui = app # Inicialização

zaragui.interface()

root_1.mainloop()


