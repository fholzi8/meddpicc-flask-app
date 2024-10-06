# MEDDPICC Flask App

Diese Flask-Anwendung dient zur Verwaltung und Analyse von Verkaufsprojekten unter Verwendung der MEDDPICC-Methode (Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Implications of Pain, Champion, Competition).

## Funktionen

- Erstellung und Verwaltung von Verkaufsprojekten
- MEDDPICC-Analyse für jedes Projekt
- Scorecard-Generierung mit visueller Darstellung
- Radar-Diagramm zur Visualisierung der MEDDPICC-Elemente
- Export von Projektberichten als PDF und PowerPoint

## Installation

1. Klonen Sie das Repository:
   ```
   git clone https://github.com/fholzi8/meddpicc-flask-app.git
   cd meddpicc-flask-app
   ```

2. Erstellen Sie eine virtuelle Umgebung und aktivieren Sie sie:
   ```
   python -m venv venv
   source venv/bin/activate  # Für Windows: venv\Scripts\activate
   ```

3. Installieren Sie die erforderlichen Pakete:
   ```
   pip install -r requirements.txt
   ```

4. Konfigurieren Sie die Datenbank:
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

## Konfiguration

1. Erstellen Sie eine `.env`-Datei im Hauptverzeichnis und fügen Sie die folgenden Variablen hinzu:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=sqlite:///your_database.db
   ```

2. Passen Sie die Konfiguration in `config.py` nach Bedarf an.

## Nutzung

1. Starten Sie die Anwendung:
   ```
   flask run
   ```

2. Öffnen Sie einen Webbrowser und navigieren Sie zu `http://localhost:5000`

3. Erstellen Sie ein neues Projekt über die Benutzeroberfläche

4. Füllen Sie die MEDDPICC-Elemente für Ihr Projekt aus

5. Generieren Sie Scorecards und Radar-Diagramme

6. Exportieren Sie Projektberichte als PDF oder PowerPoint

## Projektstruktur

```
meddpicc-flask-app/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── edit_project.html
│       └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── migrations/
├── tests/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Abhängigkeiten

- Flask
- SQLAlchemy
- Flask-WTF
- ReportLab
- python-pptx
- Matplotlib

Siehe `requirements.txt` für eine vollständige Liste der Abhängigkeiten.

## Beitrag

Wenn Sie zum Projekt beitragen möchten, erstellen Sie bitte einen Fork des Repositories und reichen Sie einen Pull Request ein.

## Lizenz

[MIT License](https://opensource.org/licenses/MIT)

## Kontakt

Bei Fragen oder Anregungen kontaktieren Sie bitte Florian Holzapfel unter fholzi8+git@gmail.com .