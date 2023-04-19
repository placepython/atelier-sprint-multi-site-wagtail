# Blog avec Django et Wagtail pour l'atelier Sprint du mercredi 19 avril 2023

Ce dépôt Github contient mon exemple de blog réalisé avec Django et Wagtail, fortement inspiré de l'exemple de Michael Yin disponible sur le dépôt [wagtail-tailwind-blog](https://github.com/AccordBox/wagtail-tailwind-blog). Je tiens à remercier Michael Yin pour son travail original qui a servi de point de départ pour ce projet.

## Dépendances

Pour exécuter ce projet, il est nécessaire d'installer `pipenv`. Pour l'installer avec `pip`, il suffit d'exécuter la commande suivante :

```
pip install pipenv
```

Voici les étapes à suivre pour installer les dépendances et les dépendances de développement :

1. Créer un répertoire .venv vide
2. Installer les dépendances avec pipenv en exécutant la commande suivante : `pipenv install --dev`
3. Installer les dépendances de développement frontend avec npm en exécutant la commande suivante : `npm install`
4. Compiler les dépendances frontend avec npm en exécutant la commande suivante : `npm run build`
5. Activer l'environnement virtuel avec pipenv en exécutant la commande suivante : `pipenv shell`
6. Lancer le serveur de base de donnée à l'aide de la commande suivante: `docker-compose up -d`
6. Exécuter les migrations avec `python manage.py migrate`
7. Installer les données de démarrage avec `python manage.py load_initial_data`
8. Changer le mot de passe admin avec la commande `python manage.py changepassword admin`

Une fois que toutes les dépendances sont installées et les migrations exécutées, vous pouvez lancer le serveur de développement de Django avec la commande suivante : `python manage.py runserver`.

Lorsque vous avez terminé de travailler sur le projet, vous pouvez stopper la base de données avec docker-compose down.

## À propos du projet
Ce blog utilise la combinaison de Django, un framework web en Python, et Wagtail, un CMS (système de gestion de contenu) open-source, pour créer un blog moderne et dynamique avec une interface d'administration conviviale. J'ai également intégré Tailwind CSS, un framework de conception de sites web, pour une expérience utilisateur encore plus agréable.

Le code source de ce projet est disponible pour être exploré et utilisé comme point de départ pour vos propres projets de blog. J'ai essayé de rendre le code aussi clair et facile à comprendre que possible, en utilisant des noms de variables et des commentaires explicatifs.

N'hésitez pas à me contacter si vous avez des questions ou des commentaires sur ce projet.

## Licence
Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus d'informations.
