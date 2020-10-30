O objetivo desse projeto é implementar um cliente para APIs REST simples, semelhante a programas como Postman ou Insomnia. Não existe nenhum objetivo de distribuição do produto final, o desenvolvimento é focado no aprendizado das tecnologias envolvidas e no uso pessoal, não há garantia alguma de funcionamento correto. <br>
OBS: Para simplicidade o cliente supõe que o servidor trabalha apenas com JSON.<br>
<br>
Ao contrário dos programas citados a configuração dos requests será feita através de um arquivo chamado requests.txt, que será lido ao iniciar o programa.<br>
A resposta do servidor será escrita em outro arquivo, chamado responses.txt.<br>
Por fim é possível utilizar variáveis nos requests. A sintaxe é semelhante a utilizada na formatação de strings em JS., a definição das variáveis é feita no arquivo vars.txt.

# Exemplo de uso:
## Arquivo requests.txt
GET ${base_url}/ <br>
POST ${base_url}/products/ ${prod}<br>

## Arquivo vars.txt
base_url = http://localhost:5000 <br>
prod = {"id": "1", "name": "Produto 1", "desc": "Breve descricao do produto"}

## Arquivo requests.txt após leitura das variáveis
GET http://localhost:5000/ <br>
POST http://localhost:5000/products/ {"id": "1", "name": "Produto 1", "desc": "Breve descricao do produto"}

## POST
Como pode ser visto o body da requisição POST é informado logo após a URL, como citado no início é esperado que esteja no formato JSON.
