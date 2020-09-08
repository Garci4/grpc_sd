import os

def ListFiles(path):
  try:
    return os.listdir(path)
  except Exception as e:
    print('error! -> ', e)
    return None

def OpenFile(path):
  try:
    return os.open(path)
  except Exception as e:
    print('error! -> ', e)
    return None

def CloseFile(path):
  try:
    return os.close(path)
  except Exception as e:
    print('error! -> ', e)
    return None