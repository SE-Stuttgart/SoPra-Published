# Release (Veröffentlichen der Dokumentation/Vorlagen)

Um keine internen Abläufe oder Daten aus Commits zu veröffentlichen sowie immer einen festen Stand der Dokumentation und Vorlagen zu haben, werden separate GitLab-Projekte (Repositories) verwendet.

Die Tutoren bekommen Zugang zur gesamten Dokumentation während die Studenten (Entwickler) nur die Dokumentation und Vorlagen im Ordner `Dokumentation.Allgemein` sehen sollen.

## Vor Release

- Falls Änderungen an Folien im `Orga`-Ordner getätigt wurden, sollten die entsprechend für die Studenten bereitgestellten PDF-Dateien im `Dokumentation.Allgemein`-Ordner aktualisiert worden sein.

## Für Tutoren / **[SoPra-Doku-Tutoren](https://sopra.informatik.uni-stuttgart.de/minderki/SoPra-Doku-Tutoren)**

Vorgehen:
- der vorhandene Inhalt im Ziel-Repo (erstellen in GitLab und klonen) gelöscht werden.
- der komplette zu veröffentlichende neue Inhalt wieder geholt werden `cd SoPra; git checkout-index -a -f --prefix=../SoPra-Doku-Tutoren/`
- ein neuer Commit erstellt werden `git add .; git commit -m "release x.y.z"`
- und ein neuer einzigen Commit erzeugt werden `git reset --hard $(git commit-tree HEAD^{tree} -m "release x.y.z")`.
- Dann muss noch gepusht werden `git push --force origin master`
- Alle Features wie Wiki/Issues in dem Projekt deaktivieren
- Tutoren Konten erstellen und sie als `Reporter` dem Projekt zuweisen (`Guest` reicht nicht, da sie dann den Code, in unserem Fall also die Dokumentation, nicht sehen können).

## <a name="dokuEntwickler"></a> Für Teilnehmer und Entwickler / **[SoPra-Doku-Entwickler](https://sopra.informatik.uni-stuttgart.de/sopra-ws1718/SoPra-Doku-Entwickler)**

**Projekte jedes Jahr neu im Namespace des entsprechend [GitLab](Gitlab.md) erstellten Administrator-Kontos für das SoPra WS XX/XX erstellen.**

Vorgehen:
- der vorhandene Inhalt im Ziel-Repo (erstellen in GitLab und klonen) gelöscht werden.
- der komplette zu veröffentlichende neue Inhalt wieder geholt werden `cp -r SoPra/Dokumentation.Allgemein/* SoPra-Doku-Entwickler`
- ein neuer Commit erstellt werden `git add .; git commit -m "release x.y.z"`
- und ein neuer einzigen Commit erzeugt werden `git reset --hard $(git commit-tree HEAD^{tree} -m "release x.y.z")`.
- Dann muss noch gepusht werden `git push --force origin master`

## <a name="projectTemplate"></a> Für Teilnehmer und Entwickler / **[SoPra-Project-Template](https://sopra.informatik.uni-stuttgart.de/sopra-ws1718/SoPra-Project-Template)**

**Template jedes Jahr neu, als *internal*, im Namespace des entsprechend [GitLab](Gitlab.md) erstellten Administrator-Kontos für das SoPra WS XX/XX erstellen.**

**Nur am Beginn des SoPras nötig, da die anderen Projekte schon auf Basis des templates erstellt wurden!**

Vorgehen:
- der vorhandene Inhalt im Ziel-Repo (erstellen in GitLab und klonen) gelöscht werden.
- der komplette zu veröffentlichende neue Inhalt wieder geholt werden `cd SoPra-Project-Template; git checkout-index -a -f --prefix=../SoPra-Project-Template-Entwickler/`
- ein neuer Commit erstellt werden `git add .; git commit -m "release x.y.z"`
- und ein neuer einzigen Commit erzeugt werden `git reset --hard $(git commit-tree HEAD^{tree} -m "template release x.y.z")`.
- Dann muss noch gepusht werden `git push --force origin master`
