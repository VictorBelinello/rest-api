from json import loads, dump
import re
import os

def loadVariable(var_name):
  """Procura a variável no arquivo texto e retorna o valor definido para ela"""
  with open('vars.txt', 'r') as f:
    for line in f:
      if line.find(var_name) != -1:
        m = re.findall('\w+\s*=\s*(.*)', line)
        var_value = m[0]
        return var_value

def subsVariable(string):
  # Procura se uma variavel foi usada 
  m = re.findall('\$\{(\w+)\}', string)
  # Se sim, substitui pelo valor definido
  if m:
    var_value = loadVariable(m[0])
    old = f"${{{m[0]}}}"
    string = string.replace(old,var_value)
  return string

def parseLine(line):
  """Monta o dicionário para representar a requisição"""
  req = {}
  # Formato: METODO URL <JSON>
  # Separa a linha usando espaco como delimitador, no maximo duas vezes (gerando 3 elementos)
  splitted = line.split(' ', maxsplit=2)

  # Obtem metodo
  req['method'] = splitted[0]

  # Obtem url
  req['url'] = subsVariable(splitted[1].strip())

  # Se tiver 3 elementos 
  if len(splitted) == 3:
    # O terceiro eh um JSON
    json = subsVariable(splitted[2])
    req['json'] = loads(json)
  return req

def loadRequests():
  """Retorna lista de tuplas do tipo (metodo, url)"""
  data = []
  with open('requests.txt', 'r') as f:
    for line in f:
      if line != "\n":
        data.append(parseLine(line))
  return data

def saveResponse(req, res):
  """Salva a resposta do servidor"""
  with open('responses.txt', 'a') as f:
    method = req.get('method')
    url = req.get('url')
    f.write(f'Response for {method} {url}\n')
    dump(res, f, indent=2,sort_keys=True)
    f.write('\n\n')

def removeResponsesFile():
  """Apaga o arquivo responses.txt"""
  try:
    os.remove('responses.txt')
  except Exception:
    pass