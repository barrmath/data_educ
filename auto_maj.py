import os

print("mise à jours des données")
os.chdir('donnee')
os.system('sh datadownload')
os.chdir('..')

print("execution des notebooks")

ordre=[]
#vérification si un fichier order.txt est présent
try:
    with open("order.txt", "r") as f:
        ordre = f.readlines()
except:
    pass

if not ordre:
    os.system("jupyter execute *.ipynb") 
 
else:
    for nb in ordre:
        cmd = "jupyter execute " + nb
        os.system(cmd)
 