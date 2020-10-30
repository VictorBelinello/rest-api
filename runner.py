import requests
from file_handler import saveResponse

def runRequest(req):
  method = req.get('method')
  url = req.get('url')
  json = req.get('json')

  if method == 'GET':
    res = requests.get(url)
  if method == 'POST':
    res = requests.post(url, json=json)
  if method == 'DELETE':
    res = requests.delete(url)

  if not res.ok:
    # Problema com resposta, apresenta erro no terminal
    print(f"Error with {method} request for {url}")
    print(f"Status code: {res.status_code}")
    # Salva a responsa no formator raw
    saveResponse(req, res.text)
  else:
    # Resposta ok, salva json 
    saveResponse(req, res.json())

def runRequests(requestsList):
  for req in requestsList:
      runRequest(req)