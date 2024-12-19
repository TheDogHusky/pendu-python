@echo off
echo Supression du dossier venv..
rmdir /s /q .venv
echo Reussi.
echo Creation d'un nouvel environnement virtuel..
"%CD:~0,3%Applications\python-3.12.0-embed\python.exe" -m virtualenv .venv
echo Reussi.
echo Installation des paquets..
.\.venv\Scripts\pip install numpy pyfiglet rich
echo Reussi.
echo Setup termine