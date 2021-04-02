# Publicis_QA_Challenge

Une petite description du projet

## Pour commencer

Mettre en place un Framework d’automatisation des tests en utilisant l’outil de votre choix qui permet de :
- Rédiger les scénarios en Gherkin d’une recherche par mot clé sur Google;
- Faire l’implémentation des steps Gherkin du scénario;
- Expliquer comment paramétrer un build dans le CI pour exécuter les tests et comment l’intégrer dans le processus de déploiement du produit;
- Documenter le setup dans le README.

### Pré-requis

Ce projet tourne avec Python 3 et utilise l'environnement virtuel pipenv pour simplicité du workflow ainsi que ses dépendences.

- Installer pipenv  
- Installer selenium
- Installer chromedriver

### Installation

Utilisez pip install pour installer pipenv, pytest et pytest-bdd

_exemple_: exécutez les commandes 
- ``pip install pipenv``, 
- ``pip install pytest --dev``,
- ``pip install pytest-bdd``, 
- ``pipenv install selenium --dev``

## Exécution des tests

Les tests peuvent être exécuter de façon global ou particulière selon que l'on veuille exécuter l'ensemble des tests (si plusieurs) ou un test spécifique

_tous les tests_: exécuter la commande ``pytest``
_un test spécifique_: exécuter la commande ``pytest -k "test_name"``

Mais avec l'utilisation de pipenv, nous préférons la méthode suivante : ``pipenv run python -m pytest``

## Projet sous Gitlab/CI



## Notes de l'auteur

Nous avons proposé deux façons d'implémenter le fichier searching.feature; notamment en utilisant le "Page Object Pattern" pour une meilleure lisibilité et réutilisabilité.
Dans le fichier test_searching.py, la partie commentée est celle ne nécitant pas l'utilsation du Page Object Pattern. 
Il suffit donc de la décommenter et commenter la partie "active" (celle faisant appel au pattern).
