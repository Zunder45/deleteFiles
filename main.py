"""
  1.0
--------
  -h: Помощь
  -v: Версия
  -p: Выбор профиля
  -l: Список профилей
 -la: Список файлов м кталогов
"""

import sys, os, shutil
from time import sleep
import conf

def chkExcept(path):
  for i in conf.exceptions_path:
    if path == os.path.abspath(i):
      print('! ' + i)
      return True
    else:
      continue
  return False

def getProfile(indexArg = ""):
  args = sys.argv
  if not indexArg == "":
    if not indexArg >= len(args) - 1:
      prf = args[indexArg +1] #значеие аргумента (-p *путь*)(путь - индекс ключа + 1)
      if prf == "" or prf not in conf.pathDir: # значение ключа пустое или его нет в списке
        print("Профиль: " + "def")
        return "def"
      else: 
        print("Профиль: " + prf)
        return prf
    else:
      print("Профиль: " + "def")
      return "def"
  else: 
    print("Профиль: " + "def")
    return "def"

def showListPof():
  for prf in conf.pathDir:
    print(prf)  
      
def showListPofFull():
  for prf in conf.pathDir:
    print(prf)
    listDirs = conf.pathDir[prf]
    for dirs in listDirs:
      print(dirs)

def delFiles(profile):
  #удаление файлов
  for item in conf.pathDir[profile]:

    if os.path.exists(item[0]):
      if item[1] == "": # Простое удаление корневого каталога 
        fileName = item[0]
        if not chkExcept(fileName): # поиск в исключениях
          if os.path.isdir(fileName):
              shutil.rmtree(fileName)
              print('X ' + fileName)
          else:
            os.remove(fileName)
            print('X ' + fileName)
      
      if item[1] == "R": # рекурсивное удаление каталога (корневой каталог остается)
        for f in os.listdir(item[0]):
          fileName = os.path.join(item[0],f)
          if not chkExcept(fileName): # поиск в исключениях
            if os.path.isdir(fileName):
              shutil.rmtree(fileName)
              print('X ' + fileName)
            else:
              os.remove(fileName)
              print('X ' + fileName)
    else: 
      print("файла нет")

def showHelp():
  print(__doc__)

def showVer():
  print(__doc__.replace(" ","").split("\n")[1])


def main(): 
  args = sys.argv 
  prof = ""

  if "-h" in args:
    showHelp()
    exit()
  elif "-l" in args:
    showListPof()
    exit()
  elif "-la" in args:
    showListPofFull()
    exit()  
  elif "-v" in args:
    showVer()
    exit()
  elif "-p" in args:
    index = args.index("-p")
    if not index == len(args)-1: 
      prof = getProfile(index)
    else:
        prof = getProfile() 
  else:
    prof = getProfile() 

  delFiles(prof)

  print("OK")
  # sleep(2)

if __name__ == "__main__":
  main()