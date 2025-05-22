# Folder Copy Script for User Profiles

📁 **Cel**: Skrypt automatycznie kopiuje zawartość wybranego podfolderu (`AppData\Roaming\[nazwa_folderu]`) od każdego użytkownika systemu Windows do jednego wspólnego folderu zbiorczego na pulpicie, zachowując strukturę.

## 🔧 Co robi skrypt?

1. Przechodzi przez wszystkich użytkowników w `C:\Users`
2. Szuka folderu `AppData\Roaming\[nazwa_folderu]`
3. Tworzy folder docelowy na pulpicie w `Desktop\KOPIA\[NazwaUzytkownika]\[NazwaFolderu]`
4. Kopiuje zawartość znalezionego folderu
5. Loguje wszystkie sukcesy i błędy do plików `.txt`

## 📜 Logi

- `create_folder_logs.txt` – tworzenie folderów
- `Skopiowane_foldery.txt` – udane kopiowanie
- `uzytkownicy_bez_tety.txt` – brak folderu u użytkownika

## ⚠️ Wymagania

- Uruchomienie z uprawnieniami administratora (jeśli są ograniczenia dostępu do katalogów innych użytkowników)
- PowerShell 5.1+

## ❗ Uwaga

Zmieniaj `Set-ExecutionPolicy` tylko jeśli wiesz co robisz. Można bezpiecznie usunąć te linie jeśli skrypt działa bez tego.
