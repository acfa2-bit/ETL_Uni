#carregar

import sqlite3

class Load():
#classe
    def __init__(self):
        pass
#método construtor

    def create_sqlite_table(self, universities_list:list[dict],db_name:str, table_name:str):

        # Criar o banco e se concectar nele
        con = sqlite3.connect(f"{db_name}.db")
        #criamos o banco
        c = con.cursor()
        #criamos a tabela 
        c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}
                (
                id INTERGER PRIMARY KEY,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
                );
        ''')
        # Percorre a lista de universidades recebida
        for university in universities_list: 
            c.execute(f'''INSERT INTO {table_name} (name, country, state_province, web_pages, domains) VALUES (?,?,?,?,?);''',
                    (university.get('name'), 
                    university.get('country'), 
                    university.get('state-province'), 
                    ', '.join(university.get('web_pages', [])), 
                    ', '.join(university.get('domains', []))))
        con.commit()
        con.close()

#depois povoamos a tabela com as informações do país, utilizando o método get para acessar os valores do dicionário e o join para transformar a lista em string.