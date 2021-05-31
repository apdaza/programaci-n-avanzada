import os
if os.path.exists("archivos3.txt"):
    os.remove("archivos3.txt")
else:
    print("no existe")
if os.path.exists("prueba"):
    os.rmdir("prueba")
else:
    print("no existe")