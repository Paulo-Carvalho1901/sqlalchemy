# Criando uma conexão com banco de dados
from sqlalchemy import create_engine, text
# criando a engine
engine = create_engine('mysql+pymysql://root:D%40vi0406@localhost:3306/cinema')
conn = engine.connect()
response = conn.execute(text('SELECT * FROM filmes;'))

for row in response:
    print(row)
    print(row.titulo)


conn.close()