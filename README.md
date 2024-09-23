# Tableau de bord Analytique des Incidents de sécurité à la SNCF en 2023


https://github.com/user-attachments/assets/f1b40703-1732-4c1b-a3a4-265f5bcd1416


Dans ce projet, je développe un tableau de bord interactif sous Python pour analyser les incidents de sécurité à la SNCF en 2023. Je déploie ce tableau de bord sous un conteneur **Docker** pour faciliter son éventuelle déploiement sur le Cloud.


## Contexte: 

Le jeu de données que j'ai utilisé représente la description et la localisation des incidents de sécurité selon l’échelle de gravité de l’EPSF (Établissement public de sécurité ferroviaire) depuis janvier 2023.

Historiquement, l’indicateur de pilotage des événements SEF (Sécurité de l'Exploitation Ferroviaire) à la SNCF était le nombre d’Évènements de Sécurité Remarquables (ESR), c’est-à-dire un évènement qui met en risque l’intégrité physique des personnes ou aux abords des installations ferroviaires sous couvert d’une défaillance du système ferroviaire (y compris les personnels, salariés de prestataires et sous-traitants, etc.).

La SNCF a décidé à partir de janvier 2023 de suivre l’indicateur de pilotage l’EPSF afin de favoriser les comparaisons avec l’ensemble des exploitants ferroviaires et promouvoir une vision commune de la sécurité.

 

L’échelle de gravité de l’EPSF comprend six niveaux :

1 : Évènement « mineur » de sécurité

2 : Évènement qui aurait pu avoir des conséquences matérielles / blessés légers

3 : Évènement qui aurait pu avoir des conséquences humaines individuelles

4 : Évènement qui aurait pu avoir des conséquences humaines collectives

5 : Accident qui a eu des conséquences significatives

6 : Accident qui a eu des conséquences graves

## Objectif

L'objectif du projet est de développer un tableau de bord sous **python** qui permet de synthétiser et de mettre en évidence les informations pertinentes sur les incidents de sécurité dans les gares SNCF pour l'année 2023.


La base de données que nous avons exploitée est disponible sur le site opendata de la [SNCF](https://ressources.data.sncf.com/explore/dataset/incidents-de-securite-epsf/table/?sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJib3hwbG90IiwiZnVuYyI6IkNPVU5UIiwieUF4aXMiOiJncmF2aXRlX2Vwc2YiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjQTEwMDZCIiwiY2hhcnRzIjpbeyJmdW5jIjoiTUlOIiwieUF4aXMiOiJncmF2aXRlX2Vwc2YifSx7ImZ1bmMiOiJRVUFOVElMRVMiLCJ5QXhpcyI6ImdyYXZpdGVfZXBzZiIsInN1YnNldHMiOjI1fSx7ImZ1bmMiOiJRVUFOVElMRVMiLCJ5QXhpcyI6ImdyYXZpdGVfZXBzZiIsInN1YnNldHMiOjUwfSx7ImZ1bmMiOiJRVUFOVElMRVMiLCJ5QXhpcyI6ImdyYXZpdGVfZXBzZiIsInN1YnNldHMiOjc1fSx7ImZ1bmMiOiJNQVgiLCJ5QXhpcyI6ImdyYXZpdGVfZXBzZiJ9XX1dLCJ4QXhpcyI6ImRhdGUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOiJtb250aCIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImluY2lkZW50cy1kZS1zZWN1cml0ZS1lcHNmIiwib3B0aW9ucyI6eyJzb3J0IjoiZGF0ZSJ9fSwic2VyaWVzQnJlYWtkb3duIjoiIiwic2VyaWVzQnJlYWtkb3duVGltZXNjYWxlIjoiIn1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D&calendarview=month).

## Méthodologie


- Prétraitement des données (Traitement des données manquantes, renommage de certaines modalités)

- Structuration des bases de données qui vont servir à alimenter mon dashboard  

- Tracer des graphiques avec la librairie **plotly**

- Mise en place de l'application web avec la librairie **dash**


## Outils

<img width="391" alt="Capture_Python2" src="https://github.com/Djamel-yod/Prediction-co2-France/assets/60408184/66deb372-f524-4d96-b982-7c7c39d8943b">


<a href="#">#Tableau de Bord</a>
<a href="#">#Pandas</a>
<a href="#">#Plotly</a>
<a href="#">#Dash</a>





