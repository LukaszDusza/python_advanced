# Zagadnienia do omówienia:

# python -m pip install virtualenv
# python -m virtualenv env_1
# cd env_1/Scripts
# activate.bat
# pip freeze > requirements.txt # pobiera obecne zależności i tworzy plik.
# pip install -r requirements.txt
# deactivate.bat
# rm -rf env_2 # rmdir /S env_2 # kasowanie env zależnie linux/windows

# Zadanie 1
# Stwórz dwa wirtualne środowiska dla Python: tests dev oraz prod. Na tests zainstaluj flask w wersji 1.1.2 a na dev w wersji 1.03.
# Stwórz odpowiedni plik reqirements.txt oraz wywołaj odpowiednie komendy w każdym środowisku.

# Zadanie 2
# Aktywuj środowisko dev po czym przełącz się na środowisko tests. Na koniec deaktywuj tests.

# Zadanie 3
# Skasuj utworzone wcześniej virtualne środowiska