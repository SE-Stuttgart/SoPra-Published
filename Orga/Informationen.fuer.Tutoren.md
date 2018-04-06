# Informationen für Tutoren

# Treffen der Betreuer und Tutoren

Ein regelmäßiges Treffen zwischen den Betreuern und Tutoren ist festzulegen. 
Vorzugsweise ein zwei Tage (zum Beispiel über das Wochenende) nach einer Abgabefrist, damit sich die Tutoren einen kleinen Überblick schon verschaffen können.

# GitLab

Die Dokumentation für Tutoren gibt es in einem separaten Projekt zu dem die Tutoren Zugriff bekommen.

# Bewertungen

Für die Bewertung muss die [Bewertungs-Vorlage](templates/Bewertung.md) verwendet werden **UND** den Entwicklern unter jedem Kontoauszug ab Meilenstein **M3** angehängt werden.

Generell gilt: Es dürfen in der Begründung der Bewertung gerne Tipps an die Studenten gegeben werden, wie das Team beim nächsten Meilenstein die nächst höhere "Geldstufe" erreichen können.
## Bewertungsmaßstab
### Crtical Features
- Ungenügend: Feature nicht implementiert (Auch nach DoD Definition) oder keinerlei Funktionalität oder stüzt sofort ab
- Schlecht: Feature zwar da, aber sehr fehlerhaft; Erwartete Grundfunktion des Features nicht vollständig;
- Mittel: Feature zwar da, aber noch fehlerhaft; Erwartete Grundfunktion des Features vollständig
- Gut: Feature mit nur kleinen Abstrichen nutzbar; Erwartete Grundfunktion des Features vollständig
- Sehr Gut: Feature ohne Probleme einstetzbar; Code ist lesbar
- Überdurchschnittlich: Feature ohne Probleme einsetzbar; Code ist gut strukturiert, lesbar und kommentiert

### Additional Features
- Zusätzliches Feature: Es gibt ein zusätzliches Feature oder das Entwicklerteam behauptet es gibt ein Feature. Das Feature bietet aber keinen Mehrwert.
- Sinnvolles Feature: Es gibt ein zusätzliches Feature, dass einen Mehrwert bietet. Das Feature kann noch mit Fehlern behaftet sein.
- Gutes Feature: Es gibt ein zusätzliches Feature, dass einen Mehrwert bietet. Das Feautre arbeitet einwandfrei.
- Sehr gutes Feature: Es gibt ein zusätzliches Feature, dass einen **deutlichen** Mehrwert bietet. Das Feature arbeitet einwandfrei. Der Code ist lesbar und kommentiert.

### Code-Qualität
Die Qualität des Codes muss einen Einfluss auf die Bewertung der **Critical** und **Additional Features** haben. Besonders ist darauf zu achten:
- Die Variablen und Methoden sind sinnvoll benannt und spiegeln ihre Funktion wieder
- Die Methoden erfüllen **nur eine** Aufgabe
  - Keine Nebeneffekte (z. B. nicht übergebene oder assozierte Variablen werden verändert)
  - Zusammenfassen von komplexeren Aufgaben in einer Methode (z. B. Methode fügt Element zu Liste, sortiert und eliminiert doppelte Einträge -> sollten drei Methoden sein)
- Methoden sollten nicht zu viele Parameter (>5) haben
- Der Code sollte, nach der üblichen Konvention, eingerückt und strukturiert sein
- **Der Code sollte sinnvoll modularisiert sein (Kopplung gering, Zusammenhalt hoch)**
- Der Code sollte nicht unnötig komplex sein
- Wo nötig, sollte der Code kommentiert sein. (JavaDoc Klassen- und Methoden-Kommentare für ein **Überdurchschnittlich** zwingend nötig!) 

### Dokumente
- Ungenügend: Die Dokumente sind nicht vorhanden oder in einem Zustand, der den Nutzen ausschließt.
- Schlecht: Die Dokumente sind vorhanden, aber der Inhalt weist Lücken auf oder ist stellenweise schlicht falsch.
- Mittel: Die Dokumente sind vorhanden und haben den minimalsten vollständigen Inhalt. Die Qualität des Inhalts ist **deutlich** verbesserungsfähig und/oder der Inhalt enthält viele Fehler (z.B. Entwurf zu grob, falsche Abstraktionsebenen der User Stories,...)
- Gut: Die Dokumente sind vorhanden. Die Qualität des Inhalts ist noch verbesserungsfähig und/oder der Inhalt enthält nur noch wenige Fehler.
- Sehr gut: Die Dokumente sind vorhanden. Die Qualität des Inhalts ist gut. Struktur und Aufbau der Dokumente ist gut.
- Überdurchschnittlich: Die Dokumente sind vorhanden. Die Qualität des Inhalts ist sehr gut. Struktur und Aufbau der Dokumente ist mindestens gut. Bei User Stories und Entwurf ist der Grad der Detailierung und Abstraktion richtig gewählt.

## Excel-Datei

[Excel-Rechner](Gruppen_Budget_Berechnung.xlsx)

Hinweise: Zurzeit ist es möglich für *Additonal Features* über den Excel-Rechner zu viel Geld zu vergeben. Bitte darauf achten, dass der maximale Betrag nicht überschritten wird!

## Wiki Konto

- Kontoauszüge entsprechend [der Vorlage](templates/Wiki.Konto.md) im **Projekt-Wiki des Teams** (nicht im eigentlichen Repository) aktualisieren bzw. eine Wiki-Seite mit dem Namen *Konto* anlegen.
- Bewertungen/Investitionen immer mit ausführlicher Begründung!

## Tutorensprechstunde

Die Tutoren müssen eine wöchtenliche Tutorentsprechstunde anbieten. 
Es müssen mindestens **2 verschiedene Sprechzeiten pro Woche** angegeben werden, um den Entwicklern terminliche Flexibilität zu ermöglichen.
In der Tutorentsprechstunde stehen die Tutoren den Teilnehmern zur Diskussion zur Verfügung. 
Des Weiteren gibt es in dieser Zeit auch die [Geräte](../Dokumentation.Allgemein/Geraet.Hardware.md) zum Testen der App.

# Konkrete Aufgaben an Meilensteinen

## M0 Start-Spielgeldkapital

Konto mit Start-Spielgeldkapital füllen. Ab Montag in der zweiten Woche.

## M1

Konto entsprechend Vorlage im Wiki des Teams aktualisieren.

## M2 Review-Teilnahme

- Review-Betreuung (Anwesenheit)
- Teilnahme-Info an Tutoren kommt von Betreuern
- Aktualisierung der Konten entsprechend der Review-Teilnahme

## M3 Verbesserte Dokumente, Entwurf

**Verbessertes Product Backlog (Datei), Definition of Done, Entwurf, Review-Protokoll (PDF) und Zeitabrechnung. Optionale Begründung in `doc/Begruendung.md` für unbearbeitete kritische und Haupt-Befunde des Reviewss**

- Anzahl überprüfen
- Sinnhaftigkeit prüfen
- Granularität prüfen
- Schätzungen grob prüfen
- Verbesserungen durchgeführt, wenn nicht? Begründung ausreichend?
- Definition of Done: 3 zusätzliche Kriterien vorhanden?

## M4, M5 Critical Features Implementierung

- Features entsprechend **Defintion im Meilenstein-Dokument** bewerten
- Wurden die verlangten kritischen Features umgesetzt, und wie?
- Wurden geeignete Addtional Features implementiert, und wie?
- An M5 werden auch nur für 4 Wochen Abzüge gemacht (Weihnachtsferien zählen nicht)

## M6 Abnahme

Betreuer:
- Zeitabrechnung kontrollieren
- Source-Code anschauen
- App starten/testen/vorführen lassen
**Tutoren als Schriftführer bei der Abnahme**

## M7 N/A