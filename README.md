# MP3 to MP34

Avant de lancer le programme, il y a 2 étapes **obligatoires** :

1. L'installation des modules, pour ce faire, vous devez simplement lancer le fichier "setup.bat" et attendre

2. L'installation de ImageMagick, pour ce faire, vous devez simplement l'installer via ce lien : https://imagemagick.org/archive/binaries/ImageMagick-7.1.0-59-Q16-HDRI-x64-dll.exe

   Puis, se rendre dans C:\Users\NOM_UTILISATEUR\AppData\Roaming\Python\Python311\site-packages\moviepy
   Ensuite ouvrir avec le bloc note le fichier "config_defaults.py"
   Se rendre à la ligne 47 (IMAGEMAGICK_BINARY) et vous devrez voir cette ligne :
   IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"
   Si la ligne n'est pas celle-ci, copiez-collez le chemin d'accès ci-dessus à la place.

## Bravo, vous avez réussis à faire toutes les étapes intermédiaires avant de lancer le programme.

Maintenant, mettez la/les musique(s) de votre choix dans le dossier "**music**". Les fichiers doivent **obligatoirement**
être en .mp3 et être nommés de cette sorte : **NOM AUTEUR-TITRE**

Maintenant, lancez le programme et copiez-collez le nom du fichier mp3 dans le terminal. 

Une fois que le programme aura finis, la vidéo finale se retrouvera dans le dossier "**final**".
