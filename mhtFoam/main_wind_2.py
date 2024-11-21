import tkinter as tk
from tkinter import simpledialog, messagebox, Tk, Frame, Label, LEFT, RIGHT, Button, Entry,font
from substitute_values_2 import generate_dictionary_1, generate_dictionary_2, generate_dictionary_3, changeFileDict, changeFileDict_2

import json

class Main_wind:
    def __init__(self, root_1):
        self.root_1 = root_1
        self.root_1.title("mhtFoam")
        self.fontePadrao = ("Adobe Myungjo Std M", "11")
        self.fonteBotoes = ("Arial", "10")
        
        largura_tela_1 = self.root_1.winfo_screenwidth()
        altura_tela_1 = self.root_1.winfo_screenheight()
        self.largura_tela = largura_tela_1//4
        self.altura_tela = altura_tela_1//3
        self.root_1.geometry(f'550x350+{self.largura_tela}+{self.altura_tela}')
    def interface(self):
        self.define_titulo()
        self.botoes_main_wind()
        #self.define_titulo()
        self.tumor_data_entries = {}
        self.data_t = {"tumors": []}
        self.jason_quantities = []
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
        
        self.terceiroContainer = Frame(root_1)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.relatorio = Button(self.terceiroContainer)
        self.relatorio["text"] = "Gerar Setup"
        self.relatorio["font"] = self.fonteBotoes
        self.relatorio["width"] = 12
        
        #self.relatorio["command"] = self.gera_setup
        self.relatorio["command"] =self.gera_setup
        self.relatorio.pack(side=LEFT)
        
        self.malha = Button(self.segundoContainer)
        self.malha["text"] = "Parâmetros da malha"
        self.malha["font"] = self.fonteBotoes
        self.malha["width"] = 20
        self.malha["pady"] = 10
       
        self.malha["command"] = self.leitura_blockMeshDict
        self.malha.pack(side=LEFT)
        
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
        self.data={}
        
        endtime = simpledialog.askfloat("Parâmetros temporais", "Tempo final:", minvalue=0, maxvalue=1000)
        timestep = simpledialog.askfloat("Parâmetros temporais", "Time step:", minvalue=0, maxvalue=1000)
        if endtime is not None:
            self.data["endtime"] = endtime
        if timestep is not None:
            self.data["timestep"] = timestep
            
        self.outJson3 = "inputDict_controlDict.json"
        self.jason_quantities.append(self.outJson3)
        with open(self.outJson3, "w") as arquivo:
            json.dump(self.data, arquivo, indent=4)
            
        messagebox.showinfo("Confirmação", "Parâmetros temporais salvos com sucesso.")
        
    def leitura_blockMeshDict(self):
        
        """
        Função responsável pela construção da parte relacionada ao blockMeshDict
        """
        self.parametro_window = tk.Toplevel(root_1)
        self.parametro_window.title("parâmetros do Domínio de Cálculo")
        
        # Construção do container para a entrada de xmax
        self.segundo2Container = Frame(self.parametro_window)
        self.segundo2Container["padx"] = 20
        self.segundo2Container["pady"] = 10
        self.segundo2Container.pack()
        # Construção do container para a entrada de ymax
        self.terceiro2Container = Frame(self.parametro_window)
        self.terceiro2Container["pady"] = 10
        self.terceiro2Container["padx"] = 20
        self.terceiro2Container.pack()
        # Construção do container para a entrada de zmax
        self.quarto2Container = Frame(self.parametro_window)
        self.quarto2Container["padx"] = 20
        self.quarto2Container["pady"] = 10
        self.quarto2Container.pack()
        # Construção do container para a entrada de xnode
        self.quinto2Container = Frame(self.parametro_window)
        self.quinto2Container["padx"] = 20
        self.quinto2Container["pady"] = 10
        self.quinto2Container.pack()
        # Construção do container para a entrada de ynode
        self.sexto2Container = Frame(self.parametro_window)
        self.sexto2Container["padx"] = 20
        self.sexto2Container["pady"] = 10
        self.sexto2Container.pack()
        # Construção do container para a entrada de znode
        self.setimo2Container = Frame(self.parametro_window)
        self.setimo2Container["padx"] = 20
        self.setimo2Container["pady"] = 10
        self.setimo2Container.pack()
        # Construção do container para a entrada de endTime
        self.oitavo2Container = Frame(self.parametro_window)
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
        self.jason_quantities.append(self.outJson)
        
        with open(self.outJson,"w") as f:
            f.write(json_string)
        f.close()
        messagebox.showinfo("Confirmação", "Parâmetros da malha salvos com sucesso.")
        
        self.parametro_window.destroy()
        
    #Aqui abre as janelas para coleta dos parâmetros dos tumores
        
    def tumors(self):
        #self.data_t = {}
        #self.data_t['user_data'] = ""
        #self.data_t['tumors'] = []
        self.tumor_windows = []
        tumor_count = simpledialog.askinteger("Parâmetros dos tumores", "How many tumors?")
        #if tumor_count is not None:
            #self.data_t['tumors'] = [None] * tumor_count
        self.open_tumor_data_screens(tumor_count)
        
    def open_tumor_data_screens(self, tumor_count):
        for i in range(0,tumor_count):
            self.largura_tela2=self.largura_tela+(i-1)*80
            self.altura_tela2=self.altura_tela+(i-1)*100
            self.collect_tumor_data(i,tumor_count)
        #self.tumor_windows = []
        

    def collect_tumor_data(self, index, tumor_count):
        
        self.current_index=index
        self.tumor_data_entries[index] = {}
        
        self.tumor_window = tk.Toplevel(self.root_1)
        self.tumor_window.geometry(f'300x370+{self.largura_tela2}+{self.altura_tela2}')
        self.tumor_window.title(f"Tumor {index + 1} Data")
        self.tumor_windows.append(self.tumor_window)
        #abre os containers
        self.primeiro5Container = Frame(self.tumor_window)
        self.primeiro5Container["padx"] = 20
        self.primeiro5Container["pady"] = 10
        self.primeiro5Container.pack()
        
        self.segundo5Container = Frame(self.tumor_window)
        self.segundo5Container["padx"] = 20
        self.segundo5Container["pady"] = 10
        self.segundo5Container.pack()
        
        self.terceiro5Container = Frame(self.tumor_window)
        self.terceiro5Container["padx"] = 20
        self.terceiro5Container["pady"] = 10
        self.terceiro5Container.pack()
        
        self.quarto5Container = Frame(self.tumor_window)
        self.quarto5Container["padx"] = 20
        self.quarto5Container["pady"] = 10
        self.quarto5Container.pack()
        
        self.quinto5Container = Frame(self.tumor_window)
        self.quinto5Container["padx"] = 20
        self.quinto5Container["pady"] = 10
        self.quinto5Container.pack()
        
        self.sexto5Container = Frame(self.tumor_window)
        self.sexto5Container["padx"] = 20
        self.sexto5Container["pady"] = 50
        self.sexto5Container.pack()
        
        
        # Aqui fica as abas onde serão coletadas os dados do usuário
        # raio,excentricidade,posição x, posição y, inclinação em graus
        
        self.radiusLabel = Label(self.primeiro5Container,text="Equivalent radius: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada do raio
        self.radius = Entry(self.primeiro5Container)
        self.radius["width"] = 30
        self.radius["font"] = self.fontePadrao
        self.radius.pack(side=LEFT)
        self.tumor_data_entries[index]["radius"] = self.radius
        
        self.eccenLabel = Label(self.segundo5Container,text="eccentricity: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada da excentricidade
        self.eccen = Entry(self.segundo5Container)
        self.eccen["width"] = 30
        self.eccen["font"] = self.fontePadrao
        self.eccen.pack(side=RIGHT)
        self.tumor_data_entries[index]["eccen"] = self.eccen
        
        self.posxLabel = Label(self.terceiro5Container,text="x position of the tumor: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada da posição x
        self.posx = Entry(self.terceiro5Container)
        self.posx["width"] = 30
        self.posx["font"] = self.fontePadrao
        self.posx.pack(side=LEFT)
        self.tumor_data_entries[index]["posx"] = self.posx
        
        self.posyLabel = Label(self.quarto5Container,text="y position of the tumor: ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada da posição y
        self.posy = Entry(self.quarto5Container)
        self.posy["width"] = 30
        self.posy["font"] = self.fontePadrao
        self.posy.pack(side=LEFT)
        self.tumor_data_entries[index]["posy"] = self.posy
        
        self.inclinationLabel = Label(self.quinto5Container,text="Inclination of the tumor (º): ", font=self.fontePadrao).pack(side=LEFT)
        # Campo para entrada da inclinação
        self.inclination = Entry(self.quinto5Container)
        self.inclination["width"] = 30
        self.inclination["font"] = self.fontePadrao
        self.inclination.pack(side=LEFT)
        self.tumor_data_entries[index]["inclination"] = self.inclination
        
        self.autenticar_tumor = Button(self.sexto5Container)
        self.autenticar_tumor["text"] = "Gerar Json"
        self.autenticar_tumor["font"] = self.fonteBotoes
        self.autenticar_tumor["width"] = 12
        # Chamada da função utilizada para geraçao do json
 
        self.autenticar_tumor["command"] = lambda win=self.tumor_window, idx=index, total=tumor_count: self.gera_json_tumor(win, idx, total)
        self.autenticar_tumor.pack(side=LEFT)

    def gera_json_tumor(self,window,index,tumor_count):
        import json
        #self.indexx = indexx
        
        indexx=index+1
        inputDict_ID = {
            f"radius_{indexx}": self.tumor_data_entries[index]["radius"].get(),
            f"eccen_{indexx}": self.tumor_data_entries[index]["eccen"].get(),
            f"posx_{indexx}": self.tumor_data_entries[index]["posx"].get(),
            f"posy_{indexx}": self.tumor_data_entries[index]["posy"].get(),
            f"inclination_{indexx}": self.tumor_data_entries[index]["inclination"].get()
        }
        
        self.data_t["tumors"].append(inputDict_ID)
        #self.data_t.append(inputDict_ID)
        
        json_string = json.dumps(inputDict_ID, indent=4)
        self.outJson2="inputDict_ID.json"
        self.jason_quantities.append(self.outJson2)
        
        if len(self.data_t["tumors"]) == tumor_count:
            with open(self.outJson2, "w") as f:
                json.dump(self.data_t, f, indent=4)
            messagebox.showinfo("Confirmação", "Parâmetros de todos os tumores salvos com sucesso.")
            
        window.destroy()
    def gera_setup(self):
        import json
        import os
        #os.system("./Allpre")
        """
        Função utilizada para substituiçoes de valores do setup
        """
        # Gera o json caso o usuario se esqueça
        self.gera_json_tumor
        self.gera_json_malha
        #print(self.current_index)
        indexx=self.current_index+1
        
        with open(self.outJson,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_2(data)
        changeFileDict(inputDict)
        with open(self.outJson3,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_1(data)
        changeFileDict(inputDict)
        #for indexx in range(1,self.current_index+1):
        with open(self.outJson2,'r') as f:
            data = json.load(f)
        inputDict = generate_dictionary_3(data,indexx)
        changeFileDict_2(inputDict)

    # Método para gerar o relatório
    def simulation(self):
        """
        Função utilizada para geração de um relatório PDF
        """
        import os

        os.system("./Allclean")
        os.system("./Allpre")
        os.system("./Allrun &")
# Inicializa a interface gráfica
root_1 = tk.Tk()
app = Main_wind(root_1)
zaragui = app # Inicialização

zaragui.interface()

root_1.mainloop()


