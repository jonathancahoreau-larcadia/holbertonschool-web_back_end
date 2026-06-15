======================================================================
PYTHON - ASYNC
======================================================================

DESCRIPTION
-----------
Ce projet explore l’exécution asynchrone en Python, un paradigme essentiel
pour écrire des programmes capables de gérer plusieurs opérations
concurrentes sans bloquer l’exécution.

L’objectif est de comprendre comment Python permet d’exécuter des tâches
en parallèle grâce au module asyncio, aux coroutines, aux mots-clés async
et await, ainsi qu’à la création de tâches concurrentes.

Ce projet s’appuie sur les concepts suivants :
    - Python - Asynchronous execution
    - Python - Asynchronous Programming

----------------------------------------------------------------------
RESOURCES
---------
Async IO in Python: A Complete Walkthrough
asyncio - Asynchronous I/O
random.uniform

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------
À la fin de ce projet, vous devez être capable d’expliquer clairement :

async and await syntax
    Comprendre comment déclarer et utiliser des coroutines Python.

How to execute an async program with asyncio
    Savoir lancer une boucle événementielle et exécuter des coroutines.

How to run concurrent coroutines
    Exécuter plusieurs tâches en parallèle grâce à asyncio.gather ou
    asyncio.as_completed.

How to create asyncio tasks
    Créer des tâches explicites avec asyncio.create_task pour lancer des
    opérations concurrentes.

How to use the random module
    Utiliser random.uniform pour générer des délais ou valeurs aléatoires
    dans des coroutines simulant des opérations asynchrones.

----------------------------------------------------------------------
REQUIREMENTS
------------

GENERAL
    - Un fichier README.md est obligatoire à la racine du projet.
    - Éditeurs autorisés : vi, vim, emacs
    - Tous les fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS
      avec Python 3.8
    - Tous les fichiers doivent se terminer par une nouvelle ligne
    - Tous les fichiers doivent être exécutables
    - La longueur des fichiers sera testée avec wc
    - La première ligne de tous les fichiers doit être exactement :
          #!/usr/bin/env python3
    - Le code doit respecter pycodestyle (version 2.5.x)
    - Toutes les fonctions et coroutines doivent être annotées avec des
      types compatibles Python 3.8
    - Tous les modules doivent avoir une documentation :
          python3 -c 'print(__import__("my_module").__doc__)'
    - Toutes les fonctions doivent avoir une documentation :
          python3 -c 'print(__import__("my_module").my_function.__doc__)'
    - Une documentation doit être une phrase complète expliquant le but
      du module, de la classe ou de la méthode.

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - écrire du code asynchrone propre et lisible,
    - comprendre la différence entre concurrence et parallélisme,
    - manipuler asyncio pour orchestrer plusieurs
