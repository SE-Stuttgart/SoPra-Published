# Begriffslexikon für Begriffe im SoPra

### <a name="abgabe"></a> Abgabe (Submission)
Die Abgabe ([Beschreibung von Abgaben](Meilensteine.Abgaben.und.Zielplattform.md)) bezeichnet (außer beim Review/M2) alle zu einem speziellen Commit im git-repository des GitLab-Projekts eines Entwickler-Teams gehörenden Dateien (Dokumente/Quellcode). Je nach [Meilenstein](#meilenstein) werden bestimmte Dateien bewertet.

- Abrenzung: Kann auf GitLab-Issues (User Stories) verweisen. Diese gehören dann auch zur Abgabe.
- Bezeichnung: Identifiziert durch einen git-tag im Format *v0.\<MeilensteinNummer\>* (Beispiel: v0.3 oder v0.5)

### <a name="additionalFeature"></a> Additional Feature
Ein [Feature](#feature), welches für die sinnvolle Verwendung/Einsatzfähigkeit der Software *wünschenswert* ist.

- Abgrenzung: [Critical Feature](#criticalFeature)

### <a name="architektur"></a> Architektur (Architecture)
Beschreibung der Software-Architektur einer Software. Enthält Komponentendiagramme die innere und externe Komponenten und die Schnittstellen zwischen den Komponenten, welche so die Struktur und den Aufbau der Software beschreiben. Weiterhin enthält die Architektur kurze Beschreibungen für Komponenten und die an Schnitstellen aus/-eingehenden Daten.

- Querverweise: [Entwurf](#entwurf)

### <a name="budgetModell"></a> Budgetmodell (Finanzplanungsmodell, Budget Model)
Das [Budgetmodell](Budgetmodell.md) legt Rahmenbedingungen für die Bewertung der Abgaben der [Entwickler-Teams](#entwicklerTeam) durch die [Investoren](#investor) fest. Hierfür wird auf **Spielgeld** in der Währung Euro (€) zurückgegriffen.

### <a name="criticalFeature"></a> Critical Feature
Ein [Feature](#feature), welches für die sinnvolle Verwendung/Einsatzfähigkeit der Software *unerlässlich* ist.

- Abgrenzung: [Additional Feature](#additionalFeature)

### <a name="definitionOfDone"></a> Definition of Done
Die Definition of Done enthält alle Bedingungen, die erfüllt sein müssen, damit eine [User Story](#userStory) als erfolgreich beendet gilt.

- Abgrenzung: Enthält explizit keine Zeit- und Aufwandsschätzung
- Gültigkeit: Im SoPra erwarten wir nur eine Definition of Done für das Gesamtprojekt. Diese kann sich aber im Verlauf des Projekts ändern.

### <a name="entwickler"></a> Entwickler (Teilnehmer, Developer)
Mitglieder eines [Entwickler-Teams](#entwicklerTeam) werden Entwickler genannt.

### <a name="entwicklerTeam"></a> Entwickler-Team (Gruppe, Team, Developer-Team)
Die SoPra-Teilnehmer welche gemeinsam in einer Gruppe bzw. in einem Team an der Entwicklung einer Software beteiligt sind, werden zusammen Entwickler-Team genannt.

### <a name="entwurf"></a> Entwurf (Software Design Description)
Entwurf der zu erstellenden Software. Das Entwurfsdokument enthält mindestens die Dokumentation zur [Architektur](#architektur).

### <a name="epic"></a>Epic (User Story)
Beschreibung einer Anforderung in Form einer [User Story](#userStory) auf höchster Abstraktionsebene. Epic User Stories beschreiben Anforderungen die im Allgemeinen einen Umfang von mehreren Monaten haben.

### <a name="feature"></a>Feature (User Story)
Beschreibung einer Anforderung in Form einer [User Story](#userStory) auf zweithöchster Abstraktionsebene. Features beschreiben Anforderungen die im Allgemeinen einen Umfang von mehreren Wochen haben.

- Querverweise: [Critical Feature](#criticalFeature), [Additional Feature](#additionalFeature)

### <a name="konto"></a> Spielgeldkapital (Konto, Play Money Fund)
Das im [Budgetmodell](#budgetModell) verwendete Spielgeld wird auf einem Konto als Spielgeldkapital geführt. Das Konto ist eine durch die [Investoren](#investor) geführte Seite im Projekt-Wiki.

- Gültigkeit: Es wird nur durch [Investoren](#investor) nach [Meilensteinen](#meilenstein) aktualisiert.

### <a name="implementable"></a>Implementable Story (User Story)
Beschreibung einer Anforderung in Form einer [User Story](#userStory) auf dritthöchster Abstraktionsebene. Implementable Stories beschreiben Anforderungen die im Allgemeinen einen Umfang von mehreren Tagen haben. Ihr werden mehrere [Tasks](#task) zugewiesen.

### <a name="investition"></a> Investition (Bewertung, Investoren-Spielgeld, Investement)
Die Bewertung der [Abgaben](#abgabe) findet durch das Aktualisieren des [Kontos](#konto) statt und wird als Investition bezeichnet.

- Gültigkeit: Findet nur an [Meilensteinen](#meilenstein) statt.
- Querverweise: [Budgetmodell](#budgetModell)

### <a name="investor"></a> Investor (Spielgeldgeber, Betreuer, Tutor)
Für die Anwendung des Budgetmodells treten die Betreuer in Kombination mit den Tutoren zur Bewertung der Abgaben als virtuelle Investoren auf, welche neben dem Start-Spielgeldkapital zusätzliches Spielgeld jedem [Entwickler-Team](#entwicklerTeam) individuell, als Investition in die weitere Entwicklung, zur Verfügung stellen.

- Abgrenzung: [Kunde](#kunde)

### <a name="kunde"></a> Kunde (Auftragsgeber, Customer)
Der Kunde ist derjenige der die zu entwickelnde Software verwenden möchte und die Anforderungen an diese stellt. Der Kunde gibt vor, welche Anforderungen [Critical Features](#criticalFeature) und welche [Additional Features](#additionalFeature) sind.

- Abgrenzung: [Investor](#investor)

### <a name="laufendeKosten"></a> Laufende Kosten (Fixkosten, Personalkosten, Running Expenses, Labor Costs)
Ein [Entwickler-Team](#entwicklerTeam) hat laufende Kosten mit ihrem [Spielgeldkapital](#konto) zu bezahlen. 
Laufende Kosten setzen sich aus Fixkosten von 1000 € pro Woche und Personalkosten von 1000 € pro Person pro Woche zusammen. 
Die Bezahlung erfolgt im Rahmen des [Budgetmodells](#budgetModell) nur an [Meilensteinen](#meilenstein).

### <a name="meilenstein"></a> Meilenstein (Milestone)
Ein Meilenstein ist ein Zeitpunkt zu dem bestimmte [Abgaben](#abgabe) von den [Investoren](#investor) als abgegeben erwartet werden und daraufhin [bewertet](#investition) werden und/oder ein wichtiger Termin zu dem das Entwickler-Team anwesend sein muss.

- Abgrenzung: [Abgabe](#abgabe), GitLab-Meilenstein zur Gruppierung/Planung von in GitLab-Issues abgebildeten User Stories und Tasks.
- Querverweise: [Beschreibung von Meilensteinen](Meilensteine.Abgaben.und.Zielplattform.md)

### <a name="meilensteinAusgang"></a> Meilenstein-Ausgang (Milestone-Exit)
Nach der Bewertung der Abgaben eines [Meilensteins](#meilenstein) werden durch den *Meilenstein-Ausgang* die Investitionen mit dem aktuellen Spielgeldkapital verrechnet.

- Abgrenzung: [Meilenstein-Eingang](#meilensteinEingang)
- Querverweise: [Beschreibung von Meilensteinen](Meilensteine.Abgaben.und.Zielplattform.md)

### <a name="meilensteinEingang"></a> Meilenstein-Eingang (Milestone-Entry)
Beim Erreichen eines [Meilensteins](#meilenstein) werden durch den *Meilenstein-Eingang* die Ausgaben für die laufenden Kosten mit dem aktuellen Spielgeldkapital verrechnet.

- Abgrenzung: [Meilenstein-Ausgang](#meilensteinAusgang)
- Querverweise: [Beschreibung von Meilensteinen](Meilensteine.Abgaben.und.Zielplattform.md)

### <a name="backlog"></a> Product Backlog (Backlog)
Das Product Backlog enthält eine Liste der noch zu erfüllenden Anforderungen in Form der [User Stories](#userStory).

- Abgrenzung: Unterscheidet sich vom [Sprint-Report](#sprintReport)
- Unklarheiten: User Stories die erledigt werden sollen, werden in den aktuellen Sprint-Report verschoben und (nur) dort als *Done* markiert, wenn sie erledigt wurden, oder wieder in das Backlog übernommen, falls nicht.
- Querverweise: [Scrum Guide Product Backlog](http://www.scrumguides.org/scrum-guide.html#artifacts-productbacklog)

### <a name="sprint"></a> Sprint (Iteration)
Fester Zeitraum in dem an durch das [Sprint Backlog](#sprintBacklog) vorher festgelegten Zielen gearbeitet wird. Im SoPra gibt es zwei Sprints.

### <a name="sprintBacklog"></a> Sprint Backlog
Im Sprint Backlog werden alle für den aktuellen [Sprint](#sprint) ausgewählten [User Stories](#userStory) festgehalten. 
Es legt damit genau fest, was im Sprint erledigt werden soll.

- Abgrenzung: [Sprint Report](#sprintReport)
- Gültigkeit: Für jeden Sprint erneut festzulegen.

### <a name="sprintReport"></a> Sprint Report
Zusammenfassendes Dokument, welches Testergebnisse, Testabdeckung und zu erledigende sowie erledigte [Features](#feature), aufgebrochen in ihre Implementable Stories und Tasks, des abgeschlossenen [Sprints](#sprint) enthält.
Es verwendet den [Sprint Backlog](#sprintBacklog) als Grundlage.

### <a name="storyPoint"></a> Story Point
Beim Schätzen des Umfangs einer User Story (im SoPra nur für [Implementable Stories](#implementableStory)) können als Einheit *Story Points* verwendet werden. Die genaue Definition wie viel *1 Story Point* ist, legt das Team durch das Schätzen der User Storys implizit fest.

- Abgrenzung: Ein Story Point ist keine Zeiteinheit, man kann höchstens im Nachhinein Berechnungen dafür anstellen.
- Gültigkeit: Zeitlich, rämlich, etc.
- Unklarheiten: Häufig wird eine User Story mit einer spontanen Anzahl an Story Points geschätzt und diese Schätzung als Maß für weitere Schätzungen verwendet. Also wie umfangreich andere User Stories im Vergleich mit der ersten User Story sind.

### <a name="task"></a>Task
Tasks sind einzelne Aufgaben, die notwendig sind, um die übergeordneten [User Stories](#userStory) ([Implementable Story](#implementable) oder [Feature](#feature)) fertig zu stellen. Ein Task hat im Allgemeinen einen Umfang von bis zu mehreren Stunden.

### <a name="userStory"></a>User Story
In Alltagssprache formulierte Anforderung an eine Software. Je nach Abstraktionsebene werden [Epic](#epic), [Feature](#feature) und [Implementable Story](#implementable) synonym verwendet.

- Querverweise: [Task](#task)

## Begriffs-Template

### <a name="eindeutigeAnkerID"></a> Begriff und seine Synonyme
Definition und Erklärung

- Abgrenzung: Wo ist dieser Begriff nicht anzuwenden
- Gültigkeit: Zeitlich, rämlich, etc.
- Bezeichnung: Eindeutiger Name in der Software, Bezeichnung in der Software
- Unklarheiten: 
- Querverweise: Verwandte Begriffe