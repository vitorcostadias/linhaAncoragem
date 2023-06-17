import tkinter as tk
import pymysql 

# Funçoes de Backend (regras de negócio e interação com Banco de Dados)
# Função para criar a conexão com o banco de dados
def criar_conexao():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="laboratorio"
    )

# Classe LinhaAncoragem
class LinhaAncoragem:
    def __init__(self):
        self.id = 0
        self.tipo = ""
        self.comprimento = 0
        self.densidade = 0
        self.area = 0
        self.tensaotopo = 0

    def criar_linha_ancoragem(self):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = "INSERT INTO linha_ancoragem (tipo, comprimento, densidade, area, tensaotopo) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.tipo, self.comprimento, self.densidade,self.area, self.tensaotopo)

        cursor.execute(sql, valores)
        conexao.commit()

        self.id = cursor.lastrowid

        cursor.close()
        conexao.close()

    def atualizar_linha_ancoragem(self):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = "UPDATE linha_ancoragem SET tipo = %s, comprimento = %s, densidade = %s, area = %s, tensaotopo = %s WHERE id = %s"
        valores = (self.tipo, self.comprimento, self.densidade, self.area, self.tensaotopo, self.id)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

    def excluir_linha_ancoragem(self):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = "DELETE FROM linha_ancoragem WHERE id = %s"
        valor = (self.id, )

        cursor.execute(sql, valor)
        conexao.commit()

        cursor.close()
        conexao.close()

    @staticmethod
    def obter_linha_ancoragem_por_id(id):
        conexao = criar_conexao()
        cursor = conexao.cursor()

        sql = "SELECT * FROM linha_ancoragem WHERE id = %s"
        valor = (id, )

        cursor.execute(sql, valor)
        resultado = cursor.fetchone()

        if resultado is not None:
            linha = LinhaAncoragem()
            linha.id = resultado[0]
            linha.tipo = resultado[1]
            linha.comprimento = resultado[2]
            linha.densidade = resultado[3]
            linha.area = resultado[4]
            linha.tensaotopo = resultado[5]
            return linha

        cursor.close()
        conexao.close()
        return None
    
    def calcular_linha_ancoragem(self):
        peso = self.area*self.comprimento*self.densidade
        return peso

# Funções de Frontend (interacao com usuario)    
def cadastrar_linha_ancoragem():
    linha = LinhaAncoragem()
    linha.tipo = entry_tipo.get()
    linha.comprimento = float(entry_comprimento.get())
    linha.densidade = float(entry_densidade.get())
    linha.area = float(entry_area.get())
    linha.tensaotopo = float(entry_tensaotopo.get())

    linha.criar_linha_ancoragem()

    print("Linha de Ancoragem cadastrada com sucesso!")

def buscar_linha_ancoragem():
    id = int(entry_id.get())

    linha = LinhaAncoragem.obter_linha_ancoragem_por_id(id)

    if linha is not None:
        entry_tipo.delete(0, tk.END)
        entry_tipo.insert(tk.END, linha.tipo)
        entry_comprimento.delete(0, tk.END)
        entry_comprimento.insert(tk.END, str(linha.comprimento))
        entry_densidade.delete(0, tk.END)
        entry_densidade.insert(tk.END, str(linha.densidade))
        entry_area.delete(0, tk.END)
        entry_area.insert(tk.END, str(linha.area))
        entry_tensaotopo.delete(0, tk.END)
        entry_tensaotopo.insert(tk.END, str(linha.tensaotopo))
    else:
        print("Linha de Ancoragem não encontrada.")

def atualizar_linha_ancoragem():
    linha = LinhaAncoragem()
    linha.id = int(entry_id.get())
    linha.tipo = entry_tipo.get()
    linha.comprimento = float(entry_comprimento.get())
    linha.densidade = float(entry_densidade.get())
    linha.area = float(entry_area.get())
    linha.tensaotopo = float(entry_tensaotopo.get())

    linha.atualizar_linha_ancoragem()

    print("Linha de Ancoragem atualizada com sucesso!")

def excluir_linha_ancoragem():
    linha = LinhaAncoragem()
    linha.id = int(entry_id.get())

    linha.excluir_linha_ancoragem()

    print("Linha de Ancoragem excluída com sucesso!")

def calcular_peso_linha_ancoragem():
    id = int(entry_id.get())

    linha = LinhaAncoragem.obter_linha_ancoragem_por_id(id)
    peso = linha.calcular_linha_ancoragem()
    if linha is not None:
        entry_tipo.delete(0, tk.END)
        entry_tipo.insert(tk.END, linha.tipo)
        entry_comprimento.delete(0, tk.END)
        entry_comprimento.insert(tk.END, str(linha.comprimento))
        entry_densidade.delete(0, tk.END)
        entry_densidade.insert(tk.END, str(linha.densidade))
        entry_area.delete(0, tk.END)
        entry_area.insert(tk.END, str(linha.area))
        entry_tensaotopo.delete(0, tk.END)
        entry_tensaotopo.insert(tk.END, str(linha.tensaotopo))
        entry_peso.delete(0, tk.END)
        entry_peso.insert(tk.END, str(peso))
    else:
        print("Linha de Ancoragem não encontrada.")
    

# Início da execução do programa
root = tk.Tk()
root.geometry(f"{300}x{300}")
root.title("Cadastro de Linha de Ancoragem")

# ID
label_id = tk.Label(root, text="ID:")
label_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()

# Tipo
label_tipo = tk.Label(root, text="Tipo:")
label_tipo.pack()
entry_tipo = tk.Entry(root)
entry_tipo.pack()

# Comprimento
label_comprimento = tk.Label(root, text="Comprimento:")
label_comprimento.pack()
entry_comprimento = tk.Entry(root)
entry_comprimento.pack()

# Densidade
label_densidade = tk.Label(root, text="Densidade:")
label_densidade.pack()
entry_densidade = tk.Entry(root)
entry_densidade.pack()

# Área
label_area = tk.Label(root, text="Área:")
label_area.pack()
entry_area = tk.Entry(root)
entry_area.pack()

# Tensão Topo
label_tensaotopo = tk.Label(root, text="Tensão Topo:")
label_tensaotopo.pack()
entry_tensaotopo = tk.Entry(root)
entry_tensaotopo.pack()

#Peso
label_peso = tk.Label(root, text="Peso:")
label_peso.pack()
entry_peso = tk.Entry(root)
entry_peso.pack()

# Botões
button_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_linha_ancoragem)
button_cadastrar.pack(side=tk.RIGHT)

button_buscar = tk.Button(root, text="Buscar", command=buscar_linha_ancoragem)
button_buscar.pack(side=tk.RIGHT)

button_atualizar = tk.Button(root, text="Atualizar", command=atualizar_linha_ancoragem)
button_atualizar.pack(side=tk.RIGHT)

button_excluir = tk.Button(root, text="Excluir", command=excluir_linha_ancoragem)
button_excluir.pack(side=tk.RIGHT)

button_calcular = tk.Button(root, text="Calcular Peso", command=calcular_peso_linha_ancoragem)
button_calcular.pack(side=tk.RIGHT)

root.mainloop()