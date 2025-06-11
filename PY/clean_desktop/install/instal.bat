@echo off
setlocal

:: Ustawienia zmiennych
set "userAppData=%ProgramFiles%"
set "exeFileName=czysty_pulpit_roz.exe"  :: Zmienna do nazwy pliku EXE TEN JEST DODAWANY DO HARMONOGRAMU
set "exeFileName2=czysy_pulpit_edit.exe"  :: Zmienna do nazwy pliku EXE
set "configFileName=czysty_pulpit_config.yaml"  :: Zmienna do nazwy pliku konfiguracyjnego YAML

:: Ścieżka do bieżącego folderu (folder, w którym znajduje się skrypt .bat)
set "currentFolder=%~dp0"

:: Utwórz folder docelowy
set "folderPath=%userAppData%\Czysty_Pulpit"
if not exist "%folderPath%" (
    mkdir "%folderPath%"
)

:: Skopiuj pliki EXE i YAML do folderu
copy "%currentFolder%%exeFileName%" "%folderPath%\%exeFileName%"
copy "%currentFolder%%exeFileName2%" "%folderPath%\%exeFileName2%%"
copy "%currentFolder%%configFileName%" "%folderPath%\%configFileName%"

:: Dodaj zadanie do harmonogramu uruchamiające EXE przy logowaniu
schtasks /create /tn "czysty_pulpit\%exeFileName%" /tr "\"%folderPath%\%exeFileName%\"" /sc onlogon /ru "%username%"

echo Zadanie zostało utworzone pomyślnie!

endlocal
pause
