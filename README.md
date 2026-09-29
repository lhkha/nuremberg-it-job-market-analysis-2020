# IT-Arbeitsmarkt & Gehaltsanalyse in Deutschland (Fokus Nürnberg)

Fokus: Qualifikationsanforderungen, Gehaltsstrukturen und regionale Trends in Bayern/Nürnberg 

Ein End-to-End Datenanalyseprojekt zur Untersuchung von Gehaltsstrukturen, geforderten Technologien und Erfahrungsstufen auf dem deutschen IT-Arbeitsmarkt, mit regionalem Schwerpunkt auf der Region Nürnberg/Erlangen.

![Dashboard Preview]
![alt text](image.png)

---
1. EINLEITUNG UND PROBLEMSTELLUNG 

1.1. Kontext und Relevanz: 

Der Markt für Datenanalyse und Business Intelligence (BI) in Deutschland wächst kontinuierlich. Insbesondere in Wirtschaftsregionen wie Bayern und der Metropolregion Nürnberg suchen Unternehmen verstärkt nach Fachkräften und Werkstudenten im Datenbereich. Für Studierende und Berufseinsteiger besteht jedoch eine erhebliche Unsicherheit bezüglich der tatsächlich geforderten Qualifikationen und realistischen Einstiegsgehälter. 

1.2. Problemstellung: 

Unklare Anforderungsprofile:  

Es fehlt an Transparenz, welche Hard Skills (z. B. Python, SQL, Power BI) vom Markt primär gefordert werden. 

Gehalts- und Erfahrungskorrelation:  

Der Einfluss von Berufserfahrung, Unternehmensgröße und Standort auf das Jahresgehalt ist für Bewerber schwer einschätzbar. 

Sprachbarrieren:  

Es ist unklar, wie stark die Arbeitssprache (Deutsch vs. Englisch) die Chancen auf dem lokalen Arbeitsmarkt beeinflusst. 

1.3. Zielsetzung des Projekts: 

Ziel dieses Projekts ist die Bereitstellung einer datengestützten Entscheidungsgrundlage. Mittels einer End-to-End-Datenpipeline (Python) und eines interaktiven Dashboards (Power BI) werden relevante Arbeitsmarktdaten bereinigt, analysiert und visualisiert. 

2. METHODIK UND DATENAUFBEREITUNG 

2.1 Datengrundlage:  

Als Basis dient der IT Salary Survey EU Dataset, gefiltert auf Antworten aus Deutschland mit dem Schwerpunkt auf datenbezogenen Rollen (Data Analyst, Data Scientist, BI Analyst, Data Engineer). 

2.2 Datenbereinigung mit Python (Pandas): 

Die Aufbereitung umfasste folgende Schritte: 

Standardisierung der Spalten: Bereinigung von Sonderzeichen und Umbenennung in einheitliche Variablennamen (city, job_title, salary_base, main_tech). 

Behandlung fehlender Werte: Bereinigung unvollständiger Datensätze bei Schlüsselvariablen. 

Bereinigung von Ausreißern: Filterung unrealistischer Gehaltsangaben (Gültigkeitsbereich: 10.000 EUR bis 250.000 EUR p.a.). 

Feature Engineering: Kategorienerstellung für Kerntechnologien sowie regionale Aggregation (Fokus auf Nürnberg, Erlangen und Fürth). 

3. KERNERGEBNISSE UND INSIGHTS: 

3.1. Gehaltsentwicklung nach Karrierestufe
Das durchschnittliche Bruttojahresgehalt liegt laut Dashboard bei rund 57.000 €.
Das dargestellte durchschnittliche Jahresgehalt steigt von etwa 38.000 € auf Junior-Level auf rund 74.000 € auf Lead-Level.
Zwischen Middle- und Senior-Level fällt der Gehaltsunterschied vergleichsweise gering aus.
Die Ergebnisse deuten auf einen Zusammenhang zwischen Karrierestufe und Gehalt innerhalb der untersuchten Stichprobe hin.

3.2. Berufserfahrung
Die durchschnittliche Berufserfahrung beträgt laut Dashboard 7,43 Jahre.
Die Kombination aus Berufserfahrung und Gehaltsniveau ermöglicht einen ersten Einblick in die Gehaltsstruktur verschiedener Karrierestufen.

3.3. Programmiersprachen
JavaScript ist mit 5 Nennungen die am häufigsten erfasste Programmiersprache.
Python und TypeScript wurden jeweils einmal erfasst.
Die Verteilung zeigt, welche Programmiersprachen innerhalb der untersuchten Stichprobe am häufigsten vertreten sind.

3.4. Sprachkenntnisse
Deutsch macht 71,43 % der dargestellten Nennungen aus.
Englisch entspricht den übrigen 28,57 %.
Die Verteilung beschreibt die im Dashboard erfassten Sprachkenntnisse. Ob Mehrfachnennungen möglich sind, hängt von der zugrunde liegenden Datenerhebung ab.

3.5. Zentrale Erkenntnisse
Das Gehalt unterscheidet sich sichtbar zwischen den dargestellten Karrierestufen.
Die Gegenüberstellung von Gehalt, Berufserfahrung und Job-Level ermöglicht eine explorative Analyse der Gehaltsstruktur.
Die Auswertung von Programmiersprachen und Sprachkenntnissen ergänzt die Gehaltsanalyse um ausgewählte Kompetenzmerkmale.

Wichtiger Hinweis: Aufgrund der kleinen Stichprobe von nur 8 IT-Positionen und des Erhebungsjahres 2020 sind die Ergebnisse als deskriptive Momentaufnahme zu interpretieren. Sie sind nicht ohne Weiteres auf den gesamten deutschen IT-Arbeitsmarkt oder auf aktuelle Gehaltsniveaus übertragbar.

4. FAZIT UND EMPFEHLUNGEN: 

Für Bewerber und Werkstudenten in der Region Nürnberg empfiehlt sich eine gezielte Kombination aus fundierten SQL-Kenntnissen, praxisnahen Python-Kenntnissen für die Datenmanipulation sowie Visualisierungskompetenz in Power BI. Deutschkenntnisse vergrößern das Unternehmensportfolio im Mittelstand erheblich. 

---

## Projektstruktur
├── data/
│   ├── raw/                       # Ursprünglicher Kaggle-Datensatz
│   └── cleaned/                   # Bereinigte CSV-Dateien aus Python
├── scripts/
│   └── datasetcleaning.py         # Python ETL-Skript (Explode, Deduplizierung)
├── reports/
│   └── IT_Salaries_Nuremberg.pbix # Power BI Berichtsdatei
├── README.md                      # Projektdokumentation
└── .gitignore                     # Git-Ignore-Regeln
