import pymongo

# Conectando ao MongoDB local
client = pymongo.MongoClient("mongodb://root:exemplo@localhost:27017/")
db = client["meu-banco-de-dados"]  # Substitua "meu-banco-de-dados" pelo nome do seu banco de dados

# Definindo uma coleção para os pacientes
pacientes_collection = db["pacientes"]


# Criando um registro de paciente
paciente = {
    "nome": "Luiz Felix",
    "idade": 40,
    "cidade": "São Paulo"
}

# Inserindo o registro na coleção
resultado_insercao = pacientes_collection.insert_one(paciente)
print("ID do paciente inserido:", resultado_insercao.inserted_id)

# Fechando a conexão com o MongoDB
client.close()
