import sys, os, shutil, time
import conf


def getProfile():

  args = sys.argv
  prf = ""
  index = 0

  for arg in args: #поиск аргументов
    if arg == "-p":
      if index != len(args)-1:
        prf = args[index+1] 
    index = index + 1

  if prf == "" or prf  not in conf.pathDir:
    print("Профиль: " + "def")
    return "def"
  else: 
    print("Профиль: " + prf)
    return prf


def delFiles(profile):
  #удаление файлов
  for item in conf.pathDir[profile]:

    if os.path.exists(item[0]):
      if item[1] == "": # Простое удаление корневого каталога 
        fileName = item[0]
        if os.path.isdir(fileName):
            shutil.rmtree(fileName)
            print(fileName, ' уделен!')
        else:
          os.remove(fileName)
          print(fileName)
        
      if item[1] == "R": # рекурсивное удаление каталога (корневой каталог остается)
        for f in os.listdir(item[0]):
          fileName = os.path.join(item[0],f)
          if os.path.isdir(fileName):
            shutil.rmtree(fileName)
            print(fileName, ' уделен!')
          else:
            os.remove(fileName)
            print(fileName)


def main():  
  delFiles(getProfile())
  print("OK")
  # time.sleep(2)

main()