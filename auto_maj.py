import os

print("mise à jours des données")
os.chdir('donnee')
os.system('sh datadownload')
os.chdir('..')

print("execution des notebooks")
os.system("jupyter execute *.ipynb") 
