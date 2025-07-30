# sorbonne
Ce repo est à destination des étudiants en Master IBI et SBI de l'Université Paris I La Sorbonne pour le cours "Analyse des données avec python"

==================================================
INSTALLATION DE VS CODE + ENVIRONNEMENT VENV + GIT
==================================================

🎯 Objectifs :
---------------
Préparer un environnement de développement Python propre et professionnel avec Visual Studio Code, un environnement virtuel (venv), et la connexion à un dépôt Git.

🎓 Pré-requis :
----------------
- Python installé (https://www.python.org/downloads/)


1. INSTALLER VISUAL STUDIO CODE
-------------------------------

    ✅ 1.1 Télécharger VS Code :
    -------------------------
    Aller sur : https://code.visualstudio.com/
    Télécharger la version correspondant à votre système (Windows, macOS, ou Linux), puis l’installer.

    ✅ 1.2 Lancer VS Code :
    --------------------
    Une fois installé, ouvrir le logiciel.

    ✅ 1.3 Installer l’extension Python :
    ----------------------------------
        Cliquer sur l’icône des extensions (à gauche).
        Rechercher "Python" (éditeur : Microsoft).
        Cliquer sur "Installer".

    ✅ 1.4 (Optionnel mais recommandé) : Installer l’extension GitHub
    --------------------------------------------------------------
    Même procédure que ci-dessus, rechercher "GitHub Pull Requests and Issues".



2. CONNECTER GIT A UN REPO GITHUB
----------------------------------

    ✅ 2.1. Installer Git si ce n'est pas déjà fait
    --------------------------------------------
    Download from git-scm.com and install.

    ✅ 2.2. Ouvrir VSCode pour se connecter à GitHub
    ---------------------------------------------
    Ouvir la pallette de commande:
        - Windows : Ctrl+Shift+P
        - Mac: Cmd+Shift+P

    Chercher GitHub: connectez-vous et suivant les indications pour vous authentifier.

    ✅ 2.3. Autre méthode:
    ----------------------
    Ouvrir le menu Source Control:
        - Cliquer l'icone en forme de branche dans la barre de tâche latéral gauche.
        - Raccourci clavier Windows : Ctrl+Shift+G
        - Raccourci clavier Mac: Cmd+Shift+G

    VS Code vous demandera de vous authentifier si besoin.

    ✅ 2.4. Cloner un repo GitHub
    ----------------------
    Dans VS Code:
        Ouvir la pallette de commande:
            - Windows : Ctrl+Shift+P
            - Mac: Cmd+Shift+P

        Taper:
            git clone https://github.com/Anthony-Lannes/sorbonne_2025_2026.git

    Choisissez un dossier dans lequel cloner le repo.


3. CRÉER UN PROJET PYTHON AVEC VENV
-----------------------------------

    ✅ 3.1 Créer et ouvrir un dossier :
    -----------------------------------
    Créer un dossier sur votre machine (exemple : `mon_projet_python`).
    Dans VS Code : *Fichier > Ouvrir un dossier* → sélectionner ce dossier.

    ✅ 3.2 Ouvrir le terminal intégré :
    -----------------------------------
    Menu : *Terminal > Nouveau terminal*

    ✅ 3.3 Créer l’environnement virtuel :
    --------------------------------------
        - Windows : python -m venv env
        - macOS/Linux : python3 -m venv env
    Un dossier `env/` sera créé : c’est votre environnement isolé.

    ✅ 3.4 Activer l’environnement :
    ---------------------------------
        - Windows (PowerShell) : .\env\Scripts\Activate.ps1
        - macOS/Linux : source env/bin/activate

    Une fois activé, l’invite du terminal commence par `(env)`.

    ✅ 3.5 Installer des bibliothèques :
    ---------------------------------
    Exemple : pip install pandas==2.3.0 numpy==1.26.4 plotly==6.2.0
