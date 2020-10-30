import requests

from file_handler import loadRequests, removeResponsesFile, saveResponse


def runRequest(req):
  # Extrai campos do dicionario request, se campo nao existe retorna None
  method = req.get('method')
  url = req.get('url')
  json = req.get('json')

  # Trata apenas esses metodos
  if method == 'GET':
    res = requests.get(url)
  elif method == 'POST':
    res = requests.post(url, json=json)
  elif method == 'PUT':
    res = requests.put(url, json=json)
  elif method == 'DELETE':
    res = requests.delete(url)
  else:
    print(f"Method {method} not valid/available, ending program")
    exit()

  if not res.ok:
    # Problema com resposta, apresenta erro no terminal
    print(f"Error with {method} request for {url}")
    print(f"Status code: {res.status_code}")
    # Salva a responsa no formato raw
    saveResponse(req, res.text)
  else:
    # Resposta ok, salva json 
    saveResponse(req, res.json())

if __name__ == "__main__":
  # Apaga o arquivo anterior
  removeResponsesFile()
  # Obtem lista com requests
  requestsList = loadRequests()
  # Pega cada um dos requests (dicionario)
  for req in requestsList:
      # Executa request
      runRequest(req)
