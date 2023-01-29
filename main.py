# Importation des modules
from moviepy.editor import *
from mutagen.mp3 import MP3
from datetime import timedelta
from random import randint
from moviepy.config import change_settings

# Génère une couleur aléatoire
R = randint(0,255) 
G = randint(0,255)
B = randint(0,255)

# Récupère la musique
nom = input("Quel est le nom du fichier mp3 ? \n>>> ")
chemin = "music/"

cheminFinal = chemin + nom + ".mp3"

audio = MP3("music/" + nom + ".mp3")

# Récupère l'auteur et le titre de la musique
auteur = nom.split("-")[0]

titre = nom.split("-")[1]

durée = audio.info.length

time = timedelta(seconds=durée)

heure = str(time).split(":")[0]
minute = str(time).split(":")[1]
seconde = str(time).split(":")[2]

seconde = round(float(seconde),0)

seconde = int(seconde)

time = str(heure) + "h" + " " + str(minute) + "min" + " " + str(seconde) + "s"

# Charge la musique
music = AudioFileClip(cheminFinal)

# Crée le fond de couleur
clip = ColorClip(size=(1920,1080), color=[R,G,B], duration=5)

# Crée la vidéo en .mp4
clip.write_videofile('vid/'+ nom +'.mp4', fps=25)

# Charge la vidéo
video = VideoFileClip("vid/" + nom + ".mp4")

clip = video.subclip(0, 5) 

# Affichage du nom de l'auteur
auteurText = TextClip("Auteur/Autrice : " + str(auteur),font="Cambria", fontsize=78, color='white')
auteurText = auteurText.set_pos(("center",60)).set_duration(5)

# Affichage du titre
titreText = TextClip("Titre : " + str(titre),font="Cambria", fontsize=78, color='white')
titreText = titreText.set_pos(("center", 260)).set_duration(5)

# Affichage de la durée
duréeText = TextClip("Durée : " + str(time),font="Cambria", fontsize=78, color='white')
duréeText = duréeText.set_pos(("center", 560)).set_duration(5)

# Assemble les différents textes
textclip = CompositeVideoClip([video, auteurText, titreText, duréeText])

# Met de la musique
finalclip = textclip.set_audio(music)

# Crée la vidéo en .mp4
finalclip.write_videofile('final/'+ nom +'.mp4', fps=25)

print('\n \n La vidéo à bien été créer et peut être trouvée dans le dossier "final" !')