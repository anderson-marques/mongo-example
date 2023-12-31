import pymongo
from bson.objectid import ObjectId

# Conectando ao MongoDB local
client = pymongo.MongoClient("mongodb://root:exemplo@localhost:27017/")
db = client["meu-banco-de-dados"]  # Substitua "meu-banco-de-dados" pelo nome do seu banco de dados
colecao = db["pacientes"]

# Defina o ID do documento que deseja pesquisar (substitua pelo ID desejado)
id_do_documento = ObjectId("6591919fe07769afdbb85c75")

# Realize a pesquisa pelo ID
documento_encontrado = colecao.find_one({"_id": id_do_documento})

if documento_encontrado:
    print("Documento encontrado:")
    print(documento_encontrado)
else:
    print("Nenhum documento encontrado com o ID especificado.")

# Fechando a conexão com o MongoDB
client.close()
