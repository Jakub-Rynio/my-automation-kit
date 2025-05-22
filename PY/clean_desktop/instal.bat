@echo off
setlocal

:: Ustawienia zmiennych
set "userAppData=%LOCALAPPDATA%"
set "exeFileName=clean_desktop.exe"  :: Zmienna do nazwy pliku EXE
set "configFileName=czysty_pulpit_config.yaml"  :: Zmienna do nazwy pliku konfiguracyjnego YAML

:: Ścieżka do bieżącego folderu (folder, w którym znajduje się skrypt .bat)
set "currentFolder=%~dp0"

:: Utwórz folder docelowy
set "folderPath=%userAppData%\clean_desktop"
if not exist "%folderPath%" (
    mkdir "%folderPath%"
)

:: Skopiuj pliki EXE i YAML do folderu
copy "%currentFolder%%exeFileName%" "%folderPath%\%exeFileName%"
copy "%currentFolder%%configFileName%" "%folderPath%\%configFileName%"

:: Dodaj zadanie do harmonogramu uruchamiające EXE przy logowaniu
schtasks /create /tn "my-automation-kit\%exeFileName%" /tr "\"%folderPath%\%exeFileName%\"" /sc onlogon /ru "%username%"

echo Zadanie zostało utworzone pomyślnie!

endlocal
pause
