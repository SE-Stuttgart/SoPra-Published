# Abgaben

Zu jedem Meilenstein werden bestimmte Dokumente, Dateien und/oder weiteres als Abgabe erwartet. Wie diese Dinge genau aussehen und wie abgegeben werden muss, wird hier erklärt, welche Dinge gefordert sind, steht in der [Beschreibung zu den Meilensteinen](Meilensteine.Abgaben.und.Zielplattform.md).

## <a name="abgabeGitTag"></a> Abgabe immer mit **git tag**
Abgaben müssen über *git-tags* markiert werden (außer bei Meilenstein 2, bei dem nur die Review-Teilnahme bewertet wird) und die entsprechenden Commits müssen vor dem Ende des Abgabezeitraums auch *gepusht* werden.
Es zählt nicht die Commit-Zeit alleine sondern auch ob die Commits **gepusht** wurden und damit rechtzeitig im GitLab-Repository eingetragen waren.

*git-tags* müssen ausdrücklich *gepusht* werden: `git push origin tagname` bzw. konkreter `git push origin v0.1`.

## <a name="markdownFormat"></a> Markdown-Format

Fast alle Dokumente müssen im Markdown-Format abgegeben werden. Hierbei ist die **Darstellung/das Rendering in der GitLab-Weboberfläche erheblich für die Bewertung**. 

Diese kann von der Vorschau oder Darstellung in anderen Werkzeugen, auch von der des Haroopads, abweichen.

## <a name="apk"></a> Ausführbare App (APK-Datei)

Die ausführbare App muss im Repository bei der Abgabe im Wurzelverzeichnis als installierbare APK-Datei abgelegt sein. 

Man sollte die APK-Datei nur bei einem Release bzw. einer Abgabe im Repository ablegen. Für alle anderen Änderungen zwischendurch exisitert ja der Quellcode und seine Änderungsgeschichte im git-Repository.

## <a name="productBacklog"></a> Product Backlog

- **Datei**: Bis inklusive des Meilensteins 3 wird das **Product Backlog in einer Datei** (Markdown) auf Basis der Vorlage `doc/Product.Backlog.md` erwartet.

    Hierbei müssen Features (vor allem bis Meilenstein 1) noch nicht in Implementable Stories und Tasks aufgebrochen werden. Es ist aber möglich, diese auch bereits zu Meilenstein 1 und/oder 3 zu dokumentieren, da sie sowieso spätestens im ersten Sprint erstellt werden müssten.

- **Issues**: Nach Meilenstein 3 müssen **mindestens die User Stories in GitLab Issues überführt werden, die in der Iteration (bis Meilenstein 4 und danach 5 entsprechend) bearbeitet werden sollen**.
  - Alle User Stories müssen als Issue erstellt werden.
  - Zur Unterscheidung welchen Typ eine User Story hat, müssen **GitLab-Issue-Labels** verwendet werden.
  - Alle Issues müssen einem zu erstellenden **GitLab-Meilenstein** zugeordnet werden (M4, M5 oder M6). Auf die einem Meilenstein zugeordneten Issues kann dann einfach vom Sprint Report aus verwiesen werden. Die unzugeordneten oder zukünftigen Meilensteinen zugeordneten Issues zählen als Product Backlog.
  - Der Issue muss die [geforderten Inhalte](User.Stories.md#inhalte) enthalten. (Titel als Issue Titel, der Rest (inklusive Link zu untergordneten User Stories) in der Beschreibung des Issues)
  - Dabei sind, falls noch nicht bis Meilenstein 3 geschehen, die entsprechenden Implementable Stories und Tasks entsprechend noch zu erstellen. 
  
  Ein Beispiel wie das aussehen soll findet sich in der [Beschreibung der User Stories](User.Stories.md#userStoriesAlsIssues)

## <a name="sprintReport"></a> Sprint Report

Der am Ende der beiden Iterationen zu Meilenstein 4, 5 und 6 abzugebende Sprint Report `doc/Sprint.Report.md` enthält folgendes:
- Link zum GitLab-Meilenstein, dem die GitLab Issues zugeordnet wurden
- Aufzählung der **Änderungen an Dokumenten/User Stories sowie wesentliche Änderungen an der App**, falls die Dokumente verbessert wurden und hierfür Investitionen erwartet werden.
- [Testabdeckungsprotokoll](#testabdeckung)/Link zum Unterordner mit dem Protokoll. 

## Review 

Die Gutachter müssen mindestens auf folgende Prüfaspekte eingehen:
- Vollständigkeit
- Aussagen/Anforderungen zu Benutzbarkeit, Sicherheit, Wartbarkeit, Portierbarkeit, Leistungsanforderungen
- Widersprüchliche Aussagen
- Gruppierung der User Stories
- Wahl der Abstraktionsebene (Epic vs. Feature vs. Task vs. Implementable)
- Zeitschätzung plausibel
- Mindestmenge an Epics und Features

**Hinweis**: Die Tutoren prüfen die zu begutachtenden Dokumente auch grob und können entscheiden, dass diese *nicht reviewfähig* sind. Dann wird das entsprechende Review abgesagt. 
Die Dokumente können weiterhin verbessert werden, aber es werden neue Reviews geplant.

### Review-Protokoll

Abgabe in **ausgedruckter** und von allen tatsächlichen Teilnehmern unterschriebenen Form direkt an die Betreuer.
Abgabe als PDF-Datei beim [Meilenstein 3](Meilensteine.Abgaben.und.Zielplattform.md#m3) unterhalb des `doc`-Ordners.

## Beispiel-Charakter der Vorlagen im Anfangs-Projekt

Alle im Anfangs-Projekt bereits vorhandenen/mitgelieferten Dokumente sind **Vorlagen** und geben hauptsächlich die grobe/minimal erwartete Struktur der Dokumente vor, nicht jedoch die Ewartung an den Inhalt und seinen Umfang.
Die Struktur der Dokumente muss beibehalten werden, aber kann bei Bedarf erweitert werden. 
Von der Ordnerstruktur darf nicht abgewichen werden, damit die Dokumente dort sind wo sie von den Investoren erwartet werden. Zusätzliche Dokumente und Ordner dürfen jederzeit hinzugefügt werden.
Die Anzahlen oder Beispielbeschreibungen stellen keine Vorgabe oder Anhaltswerte für eure Beschreibungen dar! 

## <a name="zeitabrechnung"></a> Zeitabrechnung

Anhand der Zeitabrechnung wird überprüft ob der Aufwand gleichmäßig im Entwickler-Team verteilt ist. Sie ist in der Vorlage `doc/Zeitabrechnung.ods` auszufüllen und entsprechend der [Meilenstein-Dokumentation](Meilensteine.Abgaben.und.Zielplattform.md) abzugeben.

## <a name="readme"></a> Readme.md-Datei

Die bereitgestellte Readme.md-Datei muss angepasst werden. Pflicht-Inhalte sind:
- Name
- Screenshot/Logo
- Liste der Features (inkl. Additional Features)
- Installationsanleitung (sofern die APK-Datei nicht einfach installiert und gestartet werden kann)
- Lizenz der App (spätestens bei M6)
- Verwendete Bibliotheken (inkl. Lizenzen, spätestens bei M6)

## <a name="testabdeckung"></a> Testabdeckungs(-protokoll)

Das Testprotokoll kann in Android Studio über *Generate Coverage Report* (Rechtsklick auf test-Ordner; "Run tests in ... with Coverage") als HTML-Datei exportiert werden. Bei einem Meilenstein soll dieser Export in einem Unterordner unterhalb von `doc` mit abgegeben werden. 

(Verwendete Bibliotheken und deren Code müssen nicht getestet werden)

## <a name="lizenzierung"></a> Lizenzierung

Die Angaben unter welchen Bedingungen der Quellcode, die Dokumentation und die App selbst verwendet, weitergegeben, veröffentlicht und verändert (etc.) werden dürfen, werden in der [Readme.md-Datei](#readme) kurz genannt (z. B. Name der Lizenz) und bei Bedarf in einer weiteren Datei (LICENSE.md) genauer erläutert.

Hier können auch Verweise auf die Lizenzen der verwendeten Bibliotheken und anderer Medien platziert werden.

Sie sind nicht gezwungen Ihre Arbeit unter eine freie Lizenz zu stellen. Insbesondere sollten Sie auch Rücksprache mit Ihrem Kunden halten, welche Lizenz bzw. welche Bedingungen er hat.
Bei der Wahl einer Open-Source-Lizenz kann die folgende Webseite helfen: [choosealicense.com](http://choosealicense.com/)

# Bewertung

- **Feature Bewertung**: Nur abgeschlossene Features werden bewertet. Ein Feature ist abgeschlossen, wenn 
    - der zugehörige **Issue** geschlossen ist und dem entsprechenden **Meilenstein zugeordnet** wurde und
    - die definierten **Akzeptanzkriterien erfüllt** sind und
    - die Kriterien der **Definition of Done** für dieses Feature erfüllt sind und
    - die **Funktion überprüft** werden kann und wurde.