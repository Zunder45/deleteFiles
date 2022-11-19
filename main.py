import os, shutil, time
import conf


#удаление файлов
for item in conf.path_dir:

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

  

print("OK")

# time.sleep(2)
