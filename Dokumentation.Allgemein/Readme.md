# Softwarepraktikum (SoPra) Wintersemester 2017/2018

## Überblick

Der Inhalt des SoPras:

> Die Teilnehmer bearbeiten in Dreiergruppen eine zentral gestellte Aufgabe. Sie erheben dazu die notwendigen Informationen, erstellen die notwendigen Dokumente und implementieren und prüfen ein Programm, das die Aufgabe löst.

Die Aufgabe ist die Entwicklung einer **Android App**. Diese ist für alle Teilnehmer die gleiche. 
Alle Teilnehmer müssen sich dazu in sogenannten **[Entwickler-Teams](Begriffslexikon.md#entwicklerTeam) zu genau 3 Personen** zusammenfinden. 
Dies geschieht spätestens bei der [Kick-Off-Veranstaltung](Meilensteine.Abgaben.und.Zielplattform.md#m0). 
Bei dieser werden die Zugangspasswörter für die Ilias-Gruppen (für die Entwickler-Teams) ausgegeben. 
Für die im Ilias-Kurs angemeldeten Teilnehmer des SoPras wird die Social Coding Plattform **GitLab** bereitgestellt. 
Auf dieser erfolgt die Verwaltung aller Dokumente und des Quellcodes sowie die [**Abgabe** und **Bewertung**](Abgaben.und.Bewertung.md) davon.

Teilnehmer die sich nicht rechtzeitig in ihrer Ilias-Gruppe oder sogar im Ilias-Kurs eintragen, können nicht ohne weiteres am SoPra teilnehmen.

### Agiler Ablauf

- Während bisher ein Wasserfall-Modell verwendet wurde, dient nun ein agilerer Ansatz als Vorlage für den Ablauf des Sopras.
- Um gleiche Bedingungen für alle gewähren zu können gibt es trotzdem [**fest vorgegebene und nicht verschiebbare Meilensteine**](Meilensteine.Abgaben.und.Zielplattform.md). 
- Dabei werden zu Beginn des SoPras in den ersten 4 Wochen hauptsächlich die Anforderungen in Form von [User Stories](User.Stories.md) erstellt, überprüft, verbessert und bewertet. 
- Die Anforderungen kommen von einem Kunden der zweimal für eine [Kundenbefragung](Meilensteine.Abgaben.und.Zielplattform.md#kundenBefragung) zur Verfügung steht.
- Auf Basis der erstellten Dokumente werden dann in **zwei jeweils 4 Wochen langen Sprints** zuerst die [kritischen Features](Begriffslexikon.md#criticalFeatures) und im zweiten Sprint weitere, auch von den Entwicklern selbst vorgeschlagene, [geeignete weitere Features](Begriffslexikon.md#additionalFeature) implementiert.
- Darauf folgt noch eine [Abnahme](Meilensteine.Abgaben.und.Zielplattform.md#m6) sowie ein [Abschlussfest](Meilensteine.Abgaben.und.Zielplattform.md#m7).

Als Übersicht des Ablaufs kann folgendes BPMN-Diagramm verwendet werden:

![BPMN Ablauf des SoPra](images/ablauf.bpmn.png)

## Bewertung nach Budgetmodell

Für die Bewertung der Abgaben kommt ein [Budgetmodell](Budgetmodell.md) zum Einsatz. Dieses wird auf Basis von **Spielgeld** realisiert. 
Das Spielgeld wird in Form von [**Start-Spielgeldkapital**](Begriffslexikon.md#konto) zur Verfügung gestellt, durch [**laufende Kosten**](Begriffslexikon.md#laufendeKosten) verringert und durch [**mögliche Investitionen für Abgaben**](Begriffslexikon.md#investition) erhöht.

## Dokumentation

- [Begriffslexikon](Begriffslexikon.md)
- [Budgetmodell](Budgetmodell.md)
- [Definition of Done](Definition.of.Done.md)
- [Meilensteine, Abgaben, und Zielplattform](Meilensteine.Abgaben.und.Zielplattform.md)
- [Abgaben und Bewertung](Abgaben.und.Bewertung.md)
- [Tools](Tools.md)
- [Product Backlog / User Stories](User.Stories.md)
- [Geräte und Hardware](Geraete.Hardware.md)
- [Beispiel für Kontoauszug (wird im Projekt-Wiki erstellt)](Konto.Beispiel.md)

## Aufgabe

Für die konkrete Aufgabe finden sich Dokumente im Unterordner [`Aufgabe`](Aufgabe/Readme.md)

## Vorlagen

Die Vorlagen, für abzugebende Dokumente als auch für das Android Studio Projekt, finden sich in einem separaten Repository, was als Anfangs-Projekt für jedes Entwickler-Team dient.
Vorlagen für Dokumente sind im Unterordner `doc`.

- Vorlage für Entwurfsdokument: `doc/Entwurf.md`
- Vorlage für Readme: `Readme.md`
- Vorlage für Product Backlog: `doc/Product.Backlog.md`
- Vorlage für optionale Begründung für nicht bearbeitete Befunde: `doc/Begruendung.md`
- Vorlage für Sprint Report: `doc/Sprint.Report.md`


[Licensed under CC-BY-SA 4.0 International](LICENSE)