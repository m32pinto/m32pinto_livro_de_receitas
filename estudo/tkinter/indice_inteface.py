"""

📁 Nome do arquivo: indice_interface.py | 👤 m32pinto | 🔄 Repyta |
🎯 Objetivo: criação de interface para estudo.

1-Crie o ambiente virtual com o comando:

python3 -m venv ambiente_virtual

2-Ative o ambiente virtual:

source nome_do_ambiente/bin/activate

1-Gere o arquivo rquirements.txt com o comando:

pip freeze > requirements.txt

2-Instalar dependências a partir do requirements.txt

pip install -r requirements.txt

Referências:

https://docs.python.org/3/library/tkinter.html
https://docs.python.org/3/library/sqlite3.html
https://docs.python.org/3/library/webbrowser.html
https://www.reportlab.com/
https://www.youtube.com/watch?v=RtrZcoVD1WM&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674- (Curso completo do tkinter por Rafael Serafim)
https://www.youtube.com/watch?v=Z4S32o-1K8Q&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-&index=17 (Colocar imagens no lugar dos botões, não utilizado)
https://www.youtube.com/watch?v=a7MD7a65RVE&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-&index=18 (Empacotar imagens em base64 para compilar o código sem precisa da imagem, não utilizado)
https://base64.guru/
"""

# >>> CONFIG INICIAL

from tkinter import *
from tkinter import ttk
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import base64

# >>> CÓDIGO AQUI

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def geraRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.fone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Codigo: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ' )
        self.c.drawString(50, 600, 'Cidade: ')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 630, self.foneRel)
        self.c.drawString(150, 600, self.cidadeRel)

        self.c.rect(20, 720, 550, 200, fill= False, stroke= True)

        self.c.showPage()
        self.c.save()
        self.printCliente()

class funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        # como dizer para o botão limpar que ele precisa dessa função ? (ir para o botão e adicionar command)
    def conecta_bd(self): # banco de dados com sqlite
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd (self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self): # cria tabelas dentro do banco de dados
        self.conecta_bd()
        ### criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit();print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self): # adiciona cliente, limpa a lista e vai para select novamente, adiciona os valores ao banco de dados digitados na tela
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
        VALUES(?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCLI.insert("", END, values=i)
        self.desconecta_bd()
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
        WHERE cod = ?""", (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.listaCLI.selection()

        for n in self.listaCLI.selection():
            col1, col2, col3, col4 = self.listaCLI.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCLI.delete(*self.listaCLI.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCLI.insert("", END, values=i)
        self.limpa_tela()

        self.desconecta_bd()



class application(funcs, Relatorios): # adicionamos funcs como argumento para dizer que application pode usar funções de funcs
    def __init__(self): # chamamento
        self.root = root # nomeando root
        self.tela() # chamar função tela
        self.frames_da_tela() # chama frame de tela
        self.widgets_frame1() # chamando frame 1 c
        self.lista_frame2() # chamando frame 2
        self.montaTabelas() # montando as tabelas
        self.select_lista() # criar a lista
        self.Menus() # Menu Superior
        self.busca_cliente() # buscar cliente
        root.mainloop() # loop para manter janela aberta
    def tela(self): # configuração da tela
        self.root.title("Cadastro de clientes") # nome no superior
        self.root.configure(background= 'lightblue') # cor de fundo
        self.root.geometry("700x500") # tamanho da janela inicial
        self.root.resizable(True, True) # Para a janela ser responsiva
        self.root.maxsize(width= 900, height= 700) # tamanho máximo
        self.root.minsize(width=500,height= 400) # valor mínimo da tela
    def frames_da_tela (self):
        self.frame_1 = Frame (self.root, bd= 4, bg= '#dfe3ee', highlightbackground= '#759fe6',
                              highlightthickness= 3) # Classe para os frames, estilo
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth=0.96, relheight= 0.46) # Posição/tamanho do frame

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',
                             highlightthickness=3)  # Classe para os frames, estilo
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)  # Posição/tamanho do frame
    def widgets_frame1(self):
        #self.canvas_bt = Canvas(self.frame_1,bd=0,bg='black',highlightbackground='gray',highlightthickness=3)
        #self.canvas_bt.place(relx= 0.19, rely= 0.08, relwidth= 0.22, relheight=0.19)

        # criação do botão de limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb',activeforeground="white"
                                , font=('verdana', 8, 'bold'), command= self.limpa_tela) # botão dentro do frame 1 localização/texto
        self.bt_limpar.place(relx= 0.2,rely= 0.1, relwidth=0.1, relheight= 0.15 ) # posição/tamanho
        # criação do botão de buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb',activeforeground="white"
                                , font=('verdana', 8, 'bold'), command= self.busca_cliente)  # botão dentro do frame 1 localização/texto
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)  # posição/tamanho
        # criação do botão de Novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb',activeforeground="white"
                                , font=('verdana', 8, 'bold'), command= self.add_cliente)  # botão dentro do frame 1 localização/texto
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)  # posição/tamanho
        # criação do botão de alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb',activeforeground="white"
                                , font=('verdana', 8, 'bold'), command= self.alterar_cliente)  # botão dentro do frame 1 localização/texto
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)  # posição/tamanho
        # criação do botão de apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#107db2', fg='white',
                                activebackground='#108ecb',activeforeground="white"
                                , font=('verdana', 8, 'bold'), command=self.deleta_cliente)  # botão dentro do frame 1 localização/texto
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)  # posição/tamanho

        ## criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Codigo", bg='#dfe3ee', fg = '#107db2') # botão dentro do frame 1 localização/texto
        self.lb_codigo.place(relx= 0.05, rely= 0.05) # localização do botão

        self.codigo_entry = Entry(self.frame_1) # botão dentro do frame 1 localização/texto
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth = 0.08)

        ## criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg='#dfe3ee', fg = '#107db2')  # botão dentro do frame 1 localização/texto
        self.lb_nome.place(relx=0.05, rely=0.35)  # posição/tamanho

        self.nome_entry = Entry(self.frame_1)  # botão dentro do frame 1 localização/texto
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## criação da label e entrada do telefone
        self.lb_fone = Label(self.frame_1, text="Telefone", bg='#dfe3ee', fg = '#107db2')  # botão dentro do frame 1 localização/texto
        self.lb_fone.place(relx=0.05, rely=0.6)  # posição/tamanho

        self.fone_entry = Entry(self.frame_1)  # botão dentro do frame 1 localização/texto
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4) # posição/tamanho

        ## criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg='#dfe3ee', fg = '#107db2')  # botão dentro do frame 1 localização/texto
        self.lb_cidade.place(relx=0.5, rely=0.6)  # posição/tamanho

        self.cidade_entry = Entry(self.frame_1)  # botão dentro do frame 1 localização/texto
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4) # posição/tamanho
    def lista_frame2(self): # treeview no frame 2
        self.listaCLI = ttk.Treeview(self.frame_2, height= 3, columns= ("col1","col2","col3","col4")) # treeview no frame 2 localização/texto
        self.listaCLI.heading("#0", text="" ) # especificar cabeçalhos
        self.listaCLI.heading("#1", text="Codigo" ) # treeview dentro do frame 2 localização/texto
        self.listaCLI.heading("#2", text="Nome")
        self.listaCLI.heading("#3", text="Telefone")
        self.listaCLI.heading("#4", text="Cidade")

        self.listaCLI.column("#0", width=1) # treeview dentro do frame 2
        self.listaCLI.column("#1", width=50) # 50 de 500 é 10% em relação ao tamanho
        self.listaCLI.column("#2", width=200)
        self.listaCLI.column("#3", width=125)
        self.listaCLI.column("#4", width=125)

        self.listaCLI.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85) # posição/tamanho

        # barra de rolagem

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCLI.configure(yscroll=self.scroolLista.set) # fusão para dizer que a scrollbar é da listaCLI no frame 2
        self.scroolLista.place(relx=0.96, rely= 0.1, relwidth= 0.04, relheight= 0.85)
        self.listaCLI.bind("<Double-1>",self.OnDoubleClick)
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Relatórios", menu= filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu2.add_command(label= "Limpa cliente", command= self.limpa_tela)

        filemenu2.add_command(label= "Ficha do cliente", command= self.geraRelatCliente)


application() # chamar a classe

# >>> FIM: ✅ OK | 🧪 Testar: [ ] Leitura [ ] Processamento [ ] Saída

