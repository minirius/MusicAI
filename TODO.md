# TODO
- [ ] Créer un système qui décompose les voix et isole la voix de piano d'une musique brute \n
- [ ] Analyser la musique et trouver le tempo du morceau (peut-être le demander) \n
- [ ] Analyser les notes et les rythmes joué par le piano\n
- [ ] Les convertir en format MIDI\n

# OPTIONNEL

- [ ] Créer une interface graphique qui simplifie la tache\n
- [ ] Créer une API facilement réutilisable\n
- [ ] Créer un site qui répertorie les partitions analysées\n

#ROAD

##ETAPE 1 : Analyse 1

- [ ] Trouver un module python pour analyser le fichier audio
- [ ] Trouver un json avec les notes de piano et leur fréquences
- [ ] Stocker tout les pics de fréquence dans un dictionnaire avec leur time code
- [ ] Print et afficher les notes

##ETAPE 2 : Analyse 2

- [ ] Trouver le tempo de la musique
- [ ] Calculer le rythme a l'aide des pics de fréquences (tenter avec un dictionnaire note + timecode)
- [ ] Décomposer la musique et faire correspondre la fréquence avec les notes
- [ ] Afficher et print le tout dans un terminal

##ETAPE 3 : Exporter

- [ ] Trouver un module python pour généer des fichiers midi
- [ ] Stocker toute les notes et les rythme dans le fichier midi

##ETAPE 3 : Interface graphique

- [ ] Trouver un module python pour gérer une partie graphique
- [ ] Permettre un input type file sur python
- [ ] Analyser et afficher une partition avec un module particulier
