from file_handler import loadRequests as load
from file_handler import removeResponsesFile as remove
from runner import runRequests as run

def main():
  remove()
  requestsList = load()
  run(requestsList)

if __name__ == "__main__":
  main()