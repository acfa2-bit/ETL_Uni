#utilizamos o método que acabamos de criar em extract.py:
# a execução do código é feita dentro da classe main
# mais é para executar a classe extract, que é onde está o método de extrair as informações do país.

# do arquivo src.extract, importe a classe Extract:

from src.extract import Extract
from src.load import Load

# o objeto é o resultado de uma classe.
#instanciamos o objeto:
#método que acessa links e substitui a variável "country" por "Brazil", "Canada" e "Italy".

ext = Extract()
ld = Load()

ext2 = Extract()
ld2 = Load()

# Aqui você está instanciando (criando) um objeto da classe Extract.
# ext passa a ser uma instância dessa classe.
# dentro de ld tem todos os métodos que criamos.
# Isso permite usar os métodos definidos dentro de Extract.

# br = ext.extract_country("Brazil")
# print(br)

# ca = ext.extract_country("Canada")
# print(ca)

# ld.create_sqlite_table(br, "universidades", "uni_br")
# Aqui você está chamando o método create_sqlite_table da classe
# criando a tabela e passando os parametros necessários: a lista de universidades do Brasil, o nome do banco de dados e o nome da tabela.

it = ext.extract_country("Italy")
ld.create_sqlite_table(it, "universidades", "uni_it")

#.gitignore -> colocar dentro .venv


