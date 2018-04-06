# Ziel-Platform

Vorgaben für die **Mindestanforderungen**:

- Programmiersprache: Java
- [Android-Version/API-Level](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html): `minSdk <= 25` und `targetSdk >= 25` [**API-Level 25: Android 7.1 (nougat)**](https://developer.android.com/about/versions/nougat/index.html)
- Referenz-Endgerät: **Aktueller Emulator**. Bei der Abnahme werden echte Geräte verwendet. (siehe [Geräte ausleihen](Geraete.Hardware.md))

Das bedeutet, die Android App muss auf jeden Fall auf diesem Gerät mit der angegebenen Android Version **lauffähig** und **funktionsfähig** sein. 

Sollten **Funktionen aus neueren Android Versionen** verwendet werden, ist darauf zu achten diese **abwärtskompatibel** zu implementieren. Sprich wenn sie nicht verfügbar sind, soll das Programm trotzdem noch funktionieren.
Ebenso darf die App auch auf älteren Android Versionen funktionieren, das ist sogar wünschenswert.

# Meilensteine

| Meilenstein  | Name  | Abgaben/Wichtiges  | Datum/Uhrzeit/Ort  |
|---|---|---|---|
| M0  | [Kick-Off](#m0)  | Anwesenheitspflicht  | Montag, 2017-10-16, 17:30 - 19:00 in V38.01 |
| N/A  | [1. Kunden-Befragung](#kundenBefragung)  | Anwesenheitspflicht  | Donnerstag, 2017-10-19, 08:00 - 09:30 in V38.04 |
| M1  | [Ergebnisse der ersten Analyse](#m1)  | Product Backlog (Datei), Definition of Done, Zeitabrechnung  | Freitag, 2017-10-27 23:59 |
| M2  | [Review](#m2)  | Review-Protokoll  | KW 44 hauptsächlich  |
| M3  | [Verbesserte Dokumente](#m3)  | Verbessertes Product Backlog (Datei), Definition of Done, Entwurf, Review-Protokoll (PDF) und Zeitabrechnung. Optionale Begründung für unbearbeitete kritische und Haupt-Befunde des Reviews  | Freitag, 2017-11-10 23:59  |
| M4  | [Critical Features Implementierung](#m4)  | Quellcode, ausführbares Programm, (aktualisierte) Readme, Sprint Report, Product Backlog (Issues) sowie eventuell noch weiter verbesserte/aktualisierte Dokumente aus M3 und Zeitabrechnung  | Freitag, 2017-12-08 23:59  |
| N/A  | [2. Kunden-Befragung](#kundenBefragung)  | Anwesenheitspflicht  | Mittwoch, 2017-12-13, 08:00 - 09:30 V38.02 |
| M5  | [Additional Features Implementierung](#m5)  | *siehe M4*, *Weihnachtsferien zählen nicht, laufende Kosten nur für 4 Wochen*  | Mittwoch, 2018-01-24 23:59 |
| M6  | [Abnahme durch den Kunden](#m6)  | *siehe M4*, Readme mit Lizenz-Angaben, Anwesenheitspflicht  | KW 5  |
| M7  | [Abschlussfest](#m7)  | Anwesenheitspflicht  | Donnerstag, 2018-02-08 15:45 - 19:00 in V38.03 |

## Scheinbedingungen

- Rechtzeitige Anmeldung des SoPras beim Prüfungsamt
- Mindestens neutrales Spielgeldkapital an jedem [Meilenstein-Ausgang](Begriffslexikon.md#meilensteinAusgang)
- Teilnahme an allen Meilensteinen mit Anwesenheitspflicht
- Durchgängige Beteiligung (siehe [Zeitabrechnung](Abgaben.und.Bewertung.md#zeitabrechnung))
- Mitarbeit beim Programmieren (Jeder muss programmieren)
- Lauffähige Software bei der Abnahme

## Täuschungs- und Manipulations-Versuche

- Bereits der Versuch einer Täuschung oder Manipulation führt zum **Ausschluss und dem Nicht Bestehen** des Softwarepraktikums!
- Als (versuchte) Manipulation zählen insbesondere Änderungen der git history, welche sich auf die Bewertung auswirken (würden). D.h. unter anderem bewertete Commits (bis zum Meilenstein-tag) dürfen nicht ohne weiteres verändert werden.

## <a name="m0"></a>M0 Kick-Off

Die Kick-Off-Veranstaltung ist ein erstes Treffen aller am Softwarepraktikum (SoPra) beteiligten Personen. Die Betreuer präsentieren die Rahmenbedingungen und erläutern den Ablauf des SoPra. Der Kunde beschreibt in Grundzügen die Software, die er sich wünscht. Am Ende der Kick-Off-Veranstaltung finden sich alle Teilnehmer in Entwickler-Teams (zu je 3 Teilnehmern) zusammen.

- Jeder Teilnehmer bekommt ein Passwort für eine Ilias-Gruppe (für jedes Entwickler-Team) in dem er sich im Ilias-Kurs eintragen muss.
- Auf Basis dieser Daten aus Ilias werden nach der Anmeldefrist die GitLab-Benutzer-Konten erstellt.

## <a name="kundenBefragung"></a>Kunden-Befragung

Fragen Sie in dieser Veranstaltung den Kunden über die Software, die er sich wünscht, aus. Stellen Sie vorbereitete Fragen über die gewünschten Anforderungen und das geforderte Mengengerüst. Nutzen Sie bitte eine (nicht zu technische) Sprache, die der Kunde versteht.

## <a name="m1"></a>M1 Ergebnisse der ersten Analyse

Abgabe: **Product Backlog (als Datei), Definition of Done, Zeitabrechnung** git-tag: *v0.1*

Hier müssen Sie die Ergebnisse Ihrer ersten Analyse der Kundenanforderungen in Form von User Stories (1 – 3 Epics & 10 – 20 Features) (im Product Backlog) abgeben.
Eine Kostenschätzung für das Projekt muss im SoPra nicht erstellt werden.
Diese Dokumente, bis auf die Zeitabrechnung, sind Grundlage des Reviews (M2).

## <a name="m2"></a>M2 Review

Abgabe: **Review-Protokoll**

Zur Sicherung der Qualität der User Stories hinsichtlich Verständnis und Vollständigkeit werden Reviews dieser Dokumente sowie aller weiterer bei M1 abgegebener Dokumente (bis auf die Zeitabrechnung) durchgeführt. Jeder Teilnehmer des SoPras nimmt an 2 Reviews teil.
Hierzu lädt, nach der Zuweisung der Rollen durch die Betreuer, der Moderator die zugewiesenen Teilnehmer zum Review ein. In dieser Einladung fordert er auch den Autor/Notar dazu auf, ihm den Prüfling (also die entsprechenden Dokumente) sofort zukommen zu lassen. Diesen schickt er an die Gutachter und nennt ihnen dabei auch die [Prüfaspekte](Abgaben.und.Bewertung.md#review).
Nach dem Review, bzw. spätestens am nächsten Tag, gibt der Notar das ausgedruckte und von allen Teilnehmern des Reviews unterschriebene Review-Protokoll bei einem der Betreuer ab. Des Weiteren muss das Protokoll digital vorhanden bleiben, da es bei [M3](#m3) zur Abgabe gehört.

## <a name="m3"></a>M3 Verbesserte Dokumente

Abgabe: **Verbessertes Product Backlog (als Datei), Definition of Done, Entwurf, Review-Protokoll (PDF) und Zeitabrechnung. Optionale Begründung `(doc/Begruendung.md)` für unbearbeitete kritische und Haupt-Befunde des Reviews** git-tag: *v0.3*

Die verbesserten User Stories werden (durch das aktualisierte Product Backlog) eingereicht.
Alle im Review festgestellten kritischen und Haupt-Befunde müssen entweder behoben worden sein oder die Nicht-Behebung in einem zusätzlichen Dokument `doc/Begruendung.md` begründet worden sein. Zu dieser Abgabe gehört auch die PDF-Version des angefertigten Protokolls des Reviews.
Abzugeben ist ebenfalls ein Entwurf des entstehenden Systems durch den ersichtlich wird, welche Komponenten selbst entwickelt werden und welche Komponenten „von Außen“ gestellt werden. 
Zusätzlich sollte für die eigenen Komponenten die Aufteilung in Klassen dokumentiert sein sowie GUI-Skizzen enthalten sein. 

## <a name="m4"></a>M4 Critical Features Implementierung

Abgabe: **Quellcode, ausführbares Programm, (aktualisierte) Readme, Sprint Report, Product Backlog (in Issues) sowie eventuell noch weiter verbesserte/aktualisierte Dokumente aus M3 und Zeitabrechnung**  git-tag: *v0.4*

Der Meilenstein M4 markiert das Ende des ersten Sprints der Implementierungsphase. Dem agilen Gedanken folgend, sollte hier eine erste funktionsfähige Version der Software entstanden sein.

## <a name="m5"></a>M5 Additional Features Implementierung

Abgabe: **siehe M4** git-tag: *v0.5*

M5 markiert das Ende des zweiten Sprints. Die Software sollte einem Release-Kandidaten entsprechen.

## <a name="m6"></a>M6 Abnahme durch den Kunden

Abgabe: **siehe M4**, Readme mit Lizenz-Angaben git-tag: *v0.6*

Die Betreuer begutachten in Zusammenarbeit mit dem Kunden Ihre finale Abgabe. Dabei werden Sie gebeten verschiedene Funktionalitäten nach Aufforderung zu präsentieren. Sie haben nach der Präsentation des „Pflichtteils“ noch die Möglichkeit Besonderheiten Ihrer Lösung zu präsentieren.
Weiterhin gilt es spätestens hier die [Lizenz](Abgaben.und.Bewertung.md#lizenzierung) für das Projekt festzulegen.

## <a name="m7"></a>M7 Abschlussfest

Die Abschlussveranstaltung ist das offizielle Ende des Softwarepraktikums. Das Siegerteam wird verkündet und die besten Abgaben werden präsentiert. Bei der Veranstaltung besteht Anwesenheitspflicht. Wer nicht kommen kann, muss sich vorher bei seinem Betreuer abmelden.


# Meilensteine (Template nur Wochen)

| Meilenstein  | Name  | Abgaben/Wichtiges  | Datum/Uhrzeit/Ort  |
|---|---|---|---|
| M0  | [Kick-Off](#m0)  | Anwesenheitspflicht  | Woche 0 |
| N/A  | [1. Kunden-Befragung](#kundenBefragung)  | Anwesenheitspflicht  | Woche 1 |
| M1  | [Ergebnisse der ersten Analyse](#m1)  | Product Backlog (Datei), Definition of Done, Zeitabrechnung  | Woche 2 |
| M2  | [Review](#m2)  | Review-Protokoll  | Woche 3  |
| M3  | [Verbesserte Dokumente](#m3)  | Verbessertes Product Backlog (Datei), Definition of Done, Entwurf, Review-Protokoll (PDF) und Zeitabrechnung. Optionale Begründung für unbearbeitete kritische und Haupt-Befunde des Reviews  | Woche 4  |
| M4  | [Critical Features Implementierung](#m4)  | Quellcode, ausführbares Programm, (aktualisierte) Readme, Sprint Report, Product Backlog (Issues) sowie eventuell noch weiter verbesserte/aktualisierte Dokumente aus M3 und Zeitabrechnung  | Woche 8  |
| N/A  | [2. Kunden-Befragung](#kundenBefragung)  | Anwesenheitspflicht  | Woche 9 |
| M5  | [Additional Features Implementierung](#m5)  | *siehe M4*, *Weihnachtsferien zählen nicht, laufende Kosten nur für 4 Wochen*  | Woche 12 |
| M6  | [Abnahme durch den Kunden](#m6)  | *siehe M4*, Readme mit Lizenz-Angaben, Anwesenheitspflicht  | Woche 13  |
| M7  | [Abschlussfest](#m7)  | Anwesenheitspflicht  | Woche 14 |