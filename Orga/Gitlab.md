# GitLab für das Softwarepraktikum (SoPra)

Auf Basis der im Ilias zum SoPra-Kurs angemeldeten Benutzer und von dort exportierten Benutze-Daten (Name, E-Mail, Gruppennummer(zusätzliches Pflichtfeld)) nach der Anmelde-Deadline
werden diese durch ein Script in GitLab angelegt.

Teilnehmer die zu spät sind müssen persönlich erscheinen. 
Dann werden sie in Ilias hinzugefügt und ein GitLab-Konto erstellt und dem Projekt als Teilnehmer zugewiesen

## Abbilden von [Entwickler-Team](Begriffslexikon.md#entwicklerTeam)/[Investoren](Begriffslexikon.md#investor) in GitLab-Berechtigungen ohne GitLab Groups:

Es reicht dafür einen (Administrator)-Benutzer `sopra-wsxxxx` für jedes neue SoPra zu erstellen. 
In dessen *Namespace* werden die Projekte angelegt:
- Für jedes Entwickler-Team erstellt der gerade erstellte Benutzer (per Script) ein **privates** GitLab-Projekt `sopra-team-x`: 
    - Jeder Entwickler eines Entwickler-Teams bekommt die **Master-Berechtigung** in *seinem* GitLab-Projekt.
    - Investoren bekommen die **Developer-Berechtigung** in den GitLab-Projekten für die sie zuständig sind.
- Für die übergreifende Dokumentation und Diskussion werden noch folgende GitLab-Projekte erstellt:
    - **Internal** Projekt [*SoPra-Doku-Entwickler*](Release.md#dokuEntwickler), in dem die allgemeine Dokumentation  (aus dem Ordner `Dokumentation.Allgemein`) zu finden ist. Alle Teilnehmer sollen hier **Guest**-Berechtigungen bekommen, damit das Projekt in ihrem Dashboard direkt angezeigt wird. **Master-Branch Protection entfernen!**
    - ein **privates** [*Muster-Projekt*](Release.md#projectTemplate), welches als Basis für die Erstellung der Entwickler-Team GitLab-Projekte verwendet wird. In diesem Projekt sollen die Vorlagen sowie die Ordnerstruktur vorgegeben werden. (Inhalt ist auch in der Dokumentation enthalten, deshalb reicht es *privat*). **Master-Branch Protection entfernen!**


## GitLab Problems

- The through the API created users have to get a predefined password which they don't know (https://gitlab.com/gitlab-org/gitlab-ce/issues/1051)
- `confirm`-flag is ignored (https://gitlab.com/gitlab-org/gitlab-ce/issues/1296)

## Ilias-Export

Es gibt aktuell keinen Export der die Gruppen/Team-Mitgliedschaften enthält

- Deshalb die Teilnehmerliste, in der die E-Mails enthalten sind, exportieren
- Die Übersicht mit Gruppenteilnehmern kopieren und in Calc/Excel einfügen und nach Benutzername sortieren
- Danach kann man die Teilnehmerliste auch sortieren und die benötigten Daten einfügen. **Dabei aufpassen, dass Teilnehmer die in keinem Team sind, nicht drin sind und alle E-Mail-Adressen verschieben!**

## Manuelles Erstellen über Adminoberfläche

So muss kein Passwort vorgegeben werden und es werden direkt Passwort-Setzen-E-Mails an die Benutzer verschickt

### Ablauf

- [Semiautomatischen Script Teil](#semiAutomaticApproach) verwenden um Script Team-Projekte zu erstellen
- Tabelle mit kombinierten Ilias-Daten-Tabelle öffnen
- 4 

## Script

- https://fedir.github.io/web/2014/01/06/gitlab-projects-management-from-shell/
- https://github.com/gpocentek/python-gitlab
- Example create user Script (with email sending/not sending documentations): https://github.com/kwurst/gitlab-course-managment-scripts/blob/master/create-gitlab-users.py



### Prerequisites

- python-pip
- 

### <a name="semiAutomaticApproach"></a> Semin-Automatic Approuch (automatic team-projects)

If we use the semin-automatic approach in creating the user accounts manual, we first must create the team-projects



### Approach (User Accounts and Teams)

- Get Token of Admin for this years new sopra-admin `sopra-wsxxxx`.
- Get/Set Project-ID of `SoPra-Doku-Entwickler`-Project where all users should get `Guest`-permissions.
- Get/Set Project-ID and name of template-project `SoPra-Project-Template`.
- For each tutors teams:
    - Get Tutor account ID
    - Create user accounts based on teams (team 1 - N):
        - Get Team Number
        - Create Team-Project in namespace of new sopra-admin based on the `SoPra-Project-Template`
        - Create each teams user and assign it the `master`-permissions of the new project and as `Guest` to `SoPra-Doku-Entwickler`
        - Add Tutor as `developer` to the team project
- 


### Steps (with *GitLab Groups*):
- Create Script User `sopra-wsxxxx-admin` as admin, and get its token
- Create Tutor Accounts (or if they exists dont create them)
- Create User Accounts (create usernames, care if already exists, change username):
    `gitlab user create --email email --username Username --name Name --password SomePassword`
    and save ids of the accounts
- Create GitLab-Groups for the developer-teams 
    `gitlab group create --name "Entwickler-Team X SoPra WS1516" --path sopra-ws1516-team-x`
    and save id of groups as `GID`
    `gitlab group-member create --group-id GID --access-level 10 --user-id UID `
- Add the 3 students accounts as guests to the corresponding groups
- Create copies (fork but standalone) of the template-project in the just created groups. Test with `Post /projects ?...&import_url=template-project`. Else use `POST /projects/fork/:id` then rename/delte fork relation/and enable needed features:
    `gitlab project create --name "SoPra Projekt x WSXXXX" --namespace GID --visibility-level 10 --path "sopra-wsxxxx-project-x"`
- add users to project with Master-access:
    `gitlab project-member create --project-id PID --access-level 40 --user-id UID`
- add capital-wiki-page to each project
- create issues for each milestone (check that the numbers are correct like in the capital-wiki-page)
- add corresponding tutor to the group and project