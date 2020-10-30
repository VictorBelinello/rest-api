from json import loads, dump
import os

def parseLine(line):
  """Monta o dicionário para representar a requisição"""
  req = {}
  splitted = line.split(' ', maxsplit=2)

  req['method'] = splitted[0]
  req['url'] = splitted[1].strip()
  if len(splitted) == 3:
    req['json'] = loads(splitted[2])
  return req

def loadRequests():
  """Retorna lista de tuplas do tipo (metodo, url)"""
  data = []
  with open('requests.txt') as f:
    for line in f:
      data.append(parseLine(line))
  return data

def saveResponse(req, res):
  """Salva a resposta do servidor"""
  with open('responses.txt', 'a') as f:
    method = req.get('method')
    url = req.get('url')
    f.write(f'Response for {method} {url}:\n')
    dump(res, f, indent=2,sort_keys=True)
    f.write('\n\n')

def removeResponsesFile():
  """Apaga o arquivo responses.txt"""
  try:
    os.remove('responses.txt')
  except Exception:
    pass