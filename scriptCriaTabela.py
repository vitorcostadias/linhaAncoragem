import pymysql

# Função para criar a conexão com o banco de dados
def criar_conexao():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="laboratorio"
    )

# Função para criar a tabela linha_ancoragem
def criar_tabela_linha_ancoragem():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Definição do comando SQL para criar a tabela
    sql = """
    CREATE TABLE linha_ancoragem (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(50),
        comprimento FLOAT,
        densidade FLOAT,
        tensaotopo FLOAT
    )
    """

    cursor.execute(sql)
    conexao.commit()

    cursor.close()
    conexao.close()

# Chamada da função para criar a tabela
criar_tabela_linha_ancoragem()
