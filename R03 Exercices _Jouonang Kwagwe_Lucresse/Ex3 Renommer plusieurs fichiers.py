# importez os
import os
os.chdir(os.path.dirname(__file__))

# # allez dans le dossier Ex3 Videos
os.chdir ("C:\Users\6301154\OneDrive - Cégep Édouard-Montpetit\SESSION 2\PROGRAMMATION 2\Rencontre 3\Exercice\R03 Exercices _Jouonang Kwagwe_Lucresse\Ex3 Vidéos")
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
liste_vidéo = os.listdir()
for vidéo in liste_vidéo :
   print (vidéo)  


# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier