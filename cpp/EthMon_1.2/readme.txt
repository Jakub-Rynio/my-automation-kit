# 🖥️ IP Monitor & Router Tool (Windows)

C++ narzędzie do monitorowania zmian adresu IP oraz interakcji z domyślną bramką sieciową na systemie Windows. Pomaga wykryć zmianę adresu IP, umożliwia jego odnowienie (`ipconfig /renew`) oraz test połączenia z routerem (`ping`).

---

## 🧩 Co robi ten program?

🔹 Wykrywa bieżący adres IP komputera (tylko interfejs Ethernet).  
🔹 Sprawdza domyślną bramkę (`Default Gateway`).  
🔹 Monitoruje zmiany adresu IP.  
🔹 W przypadku zmiany:
- Proponuje pingowanie routera (`ping [bramka]`)
- Umożliwia ponowne odnowienie adresu IP (`ipconfig /renew`)  
🔹 Wyświetla informację o braku sygnału, jeśli po odnowieniu IP nadal wynosi `0.0.0.0`.

---
