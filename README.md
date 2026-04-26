#  Smart Timer App (Flutter & Django REST API)

Tento projekt je full-stack ukázkou moderní mobilní aplikace propojené s vlastním backendem. Slouží k vytváření, správě a spouštění uživatelských časovačů (presetů) se záznamem historie do databáze. 

Projekt byl vytvořen s důrazem na čistou architekturu, RESTful API komunikaci a pochopení základních konceptů databázových relací.

##  Klíčové vlastnosti

###  Frontend (Flutter)
* **Dynamické UI:** Zobrazení presetů s možností smazání gestem (Swipe-to-delete) a aktualizací seznamu potažením dolů (Pull-to-refresh).
* **Stavový automat časovače:** Plynulý odpočet s vizualizací, která mění barvy podle nastavení presetu a po dokončení spustí varovné blikání.
* **Haptická odezva:** Využití vibrací zařízení po dokončení odpočtu. (Funkčnost neověřena)
* **Multi-user demonstrátor:** Přepínač v horní liště aplikace demonstruje izolaci dat mezi různými uživateli bez nutnosti složitého přihlašovacího procesu.

###  Backend (Django)
* **REST API:** Plně funkční API postavené na Django REST Frameworku (endpointy `/api/presets/` a `/api/history/`).
* **Relační databáze:** SQLite databáze s využitím cizích klíčů (`ForeignKey`) a kaskádového mazání (`CASCADE`) pro zachování datové integrity.
* **Datová filtrace:** API automaticky filtruje presety a historii na základě query parametrů (např. `?user=2`), což zajišťuje multi-user funkcionalitu.

##  Použité technologie
* **Frontend:** Flutter, Dart, `http` balíček pro API dotazy.
* **Backend:** Python, Django, Django REST Framework.
* **Databáze:** SQLite (výchozí pro Django).

##  Jak projekt spustit

### 1. Spuštění Backend serveru (Django)
Ve složce s backendem (např. `timer_api`) spusťte terminál:

```bash
# Aktivace virtuálního prostředí (pokud používáte)
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Instalace závislostí
pip install -r requirements.txt

# Aplikování databázových migrací
python manage.py migrate

# Vytvoření 2 uživatelů pro demonstraci multi-user aplikace 
python manage.py createsuperuser

# Spuštění serveru
python manage.py runserver
```
*Server pro přístup admina poběží na adrese `http://127.0.0.1:8000/`.*

### 2. Spuštění Frontend aplikace (Flutter)
Ujistěte se, že máte spuštěný emulátor nebo připojené fyzické zařízení. Ve složce s Flutter projektem spusťte:

```bash
# Stažení balíčků
flutter pub get

# Spuštění aplikace
flutter run
```
*Poznámka pro Android emulátor: Aplikace přistupuje k lokálnímu serveru Android Studia přes IP adresu `10.0.2.2`, což je standardní alias pro localhost vývojářského stroje z prostředí Android emulátoru.*

##  Architektura a plány do budoucna (Future Work)

Aplikace aktuálně využívá **Online-only přístup**, kdy jsou data vázána na dostupnost serveru. Avšak si i udržuje lokální kopii stažených presetů, takže v mobilní aplikaci jdou spustit načtené časovače. V okamžiku načtení jiného uživatele nebo stránky s historií je potřeba načíst online data ze serveru.

V rámci dalšího vývoje a přesunu do produkčního prostředí je naplánován přechod na **Offline-First architekturu**:

1. **Lokální databáze (Cache):** Implementace balíčku (např. `sqflite` nebo `Hive`) pro lokální ukládání presetů. Aplikace by tak byla okamžitě použitelná i bez připojení k internetu.
2. **Synchronizační fronta (Background Sync):** Pokud uživatel dokončí měření v offline režimu, záznam se uloží primárně do lokální fronty. Jakmile zařízení detekuje stabilní připojení, aplikace tiše odešle ("flushne") neshromážděná data na Django server.
3. **Tokenové přihlašování:** Nahrazení demonstračního přepínače uživatelů za standardní JWT (JSON Web Tokens) autentizaci pro plné zabezpečení osobních dat.