======================================================================
PYTHON - ASYNC COMPREHENSION
======================================================================

DESCRIPTION
-----------
Ce projet approfondit l’exécution asynchrone en Python en introduisant trois
concepts essentiels :

1. Les générateurs asynchrones (async generators)
2. Les compréhensions asynchrones (async comprehensions)
3. L’annotation de type pour les générateurs

Ces outils permettent de traiter des flux de données asynchrones de manière
simple, élégante et performante, tout en conservant la syntaxe familière
des compréhensions Python.

----------------------------------------------------------------------
RESOURCES
---------
PEP 530 -- Asynchronous Comprehensions
What’s New in Python: Asynchronous Comprehensions / Generators
Type-hints for generators

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------
À la fin de ce projet, vous devez être capable d’expliquer clairement :

How to write an asynchronous generator
    Savoir utiliser "async def" avec "yield" pour produire des valeurs
    de manière asynchrone.

How to use async comprehensions
    Utiliser la syntaxe :
        [await x async for x in async_generator()]
    pour collecter des données asynchrones efficacement.

How to type-annotate generators
    Annoter correctement les générateurs asynchrones avec les types
    compatibles Python 3.8 (ex : AsyncGenerator, AsyncIterable, etc.).

----------------------------------------------------------------------
REQUIREMENTS
------------

GENERAL
    - Éditeurs autorisés : vi, vim, emacs
    - Tous les fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS
      avec Python 3.8
    - Tous les fichiers doivent se terminer par une nouvelle ligne
    - Tous les fichiers doivent être exécutables
    - La première ligne de tous les fichiers doit être exactement :
          #!/usr/bin/env python3
    - Un fichier README.md est obligatoire à la racine du projet
    - Le code doit respecter pycodestyle (version 2.5.x)
    - La longueur des fichiers sera testée avec wc
    - Tous les modules doivent avoir une documentation :
          python3 -c 'print(__import__("my_module").__doc__)'
    - Toutes les fonctions doivent avoir une documentation :
          python3 -c 'print(__import__("my_module").my_function.__doc__)'
    - La documentation doit être une phrase complète expliquant le but
      du module, de la classe ou de la méthode
    - Toutes les fonctions et coroutines doivent être annotées avec des
      types compatibles Python 3.8

----------------------------------------------------------------------
OBJECTIF GLOBAL
---------------
Ce projet vous apprend à :
    - manipuler des flux de données asynchrones,
    - écrire des générateurs capables de produire des valeurs au fil du temps,
    - utiliser des compréhensions asynchrones pour collecter des données
      de manière concise et performante,
    - typer correctement vos générateurs et coroutines,
    - préparer des pipelines asynchrones plus avancés.

======================================================================
