Dans ce notebook, vous trouverez des documents qui viennent de datagouv, sur l'éducation nationale.<br>
Vous pouvez les consulter sur ce site : <a href="https://www.data.gouv.fr/fr/pages/donnees_education/">data_gouv_educ</a><br>
<br>
On va juste voir ce qu'on peut y voir à l'interieur.<br>
On va commencer par une vue générale en France, puis les différences générale entre secteur public et privé au niveau national.<br>
Arborescence :
.
├── Analyse.ipynb                           Fichier final pour l ánalyse de la situation.<br>
├── college_nettoyage_et_analyse.ipynb      Fichier pour analyse des données "collége"<br>
├── donnee                                  Dossier contenant les données de data gouv<br>
├── donnee_temp                             Dossier contenant les données extraites pour analyse<br>
│   ├── college.csv<br>
│   ├── ecole.csv<br>
│   └── readme.md<br>
├── ecole_nettoyage_et_analyse_.ipynb       Fichier pour analyse des données 'écoles'<br>
├── fonctions<br>
│   ├── perso_stats.py                      Fonction personnelle pour les tests statistiques<br>
├── lycee_nettoyage_analyse.ipynb<br>
├── readme.md                               Ce readme<br>
├── datadownload                            Fichier bash pour telecharger les fichier sur datagouv<br>

Prérequis :<br>
avoir wget installer<br>
sous Linux : sh datadownload<br>
    Wget va telecharger ou mettre à jour les fichiers donnée.<br>

Pour les notebooks  les paquets suivants sont installés :

matplotlib==3.8.2<br>
matplotlib-inline==0.1.6<br>
numpy==1.26.4<br>
pandas==1.5.3<br>
scikit-learn==1.4.1.post1<br>
scipy==1.12.0<br>
seaborn==0.12.2<br>

Pour la mise en ligne automatique : faire un bucket S3 en mode static website : https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html