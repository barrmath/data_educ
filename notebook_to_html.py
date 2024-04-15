from nbconvert import HTMLExporter
from os import listdir
from os import mkdir

# lister les notebooks present à la racine
all_file = listdir()

# liste vide, servira pour crée un index avec les adresses des notebooks
notebook = []

# créer le dossier html et gerer si le dossier existe deja
try:
    mkdir("html")
except OSError as error:
    # print(error)
    pass

# pour chaque fichier notebook faire la convertion et envoyer la copie html vers le dossier html
for file in all_file:
    if file.endswith(".ipynb"):
        # faire la convertion avec un object
        htmlexport = HTMLExporter()
        htmlexport.exclude_input = True
        htmldata, ressource = htmlexport.from_file(file)
        notebook.append(file[:-6] + ".html")
        # write to output file
        outputdata = "html/" + file[:-6] + ".html"
        with open(outputdata, "w") as f:
            f.write(htmldata)

# faire un fichier index.html avec les liens vers les page html notebook

html_text = """<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>index</title>
  </head>
  <body>
  <p>index généré par <a href=https://github.com/barrmath/jupyter2html >https://github.com/barrmath/jupyter2html</a><br><br>\n"""


for file in notebook:
    html_text += "<a href= " + file + ' target="blank">' + file[:-5] + "</a>\n<br>"

html_text += "</p></body>"

with open("html/index.html", "w") as f:
    f.write(html_text)
