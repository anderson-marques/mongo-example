


- `python -m pip install -r requirements.txt` - Instala as dependencias
- `python3 ./cria_e_insere.py` cria o banco de dados e a collection e insere
- `python3 ./get_by_id.py` - connect no banco de dados e obtem o registro
- `docker compose up -d` - Cria e initializa o bd em background
- `docker compose run mongo-shell` - entra no shell do mongo. Lá dentro:
  - `show dbs` - lista os bancos de dados
  - `use meu-banco-de-dados` - Seleciona o banco
  - `db.pacientes.find({})` - lista todos