# Aufgabenspezifische Dokumentation

In diesem Ordner werden Dokumente abgelegt welche sich auf die konkrete Aufgabe im SoPra beziehen.

## Aufgabe: Feld-/Schaden-Koordinaten-Erfassungs-App für Schadensfall-Gutachter

Landwirte versichern ihre Felder gegen verschiedenste Schäden. 
Ein wichtiger Parameter ist die Fläche des Feldes und die Region in der das Feld bewirtschaftet wird.
Kommt es zu einem Schaden, müssen Gutachter oder Landwirte die genaue Position und Abmessungen des Schadens erfassen können und den Sachbeareitern in der Versicherung übermitteln können.

Eine App, die automatisch Positionsdaten des Feldes bzw. des Schadens erfassen kann, wäre eine deutliche Erleichterung für die Gutachter.

# Critical Features (Verbindliche Vorgaben)

## Visuelle Darstellung der Schadensfälle

> Als Benutzer möchte ich, dass Schadensfälle, auch während der Erfassung, auf einer Karte angezeigt werden können.

- Aufwandsschätzung: *TODO*
- Akzeptanztests: 
    - [ ] Schadensfälle können in einer Kartenansicht dargestellt werden.
    - [ ] Die Kartenansicht des Schadens zeig Polygone der versicherten Objekte.
    - [ ] Die Kartenansicht des Schadens zeigt den Schaden als Polygon/Fläche innerhalb der versicherten Objekte.
    - [ ] Die Kartenansicht inkl. der Schadensdarstellung ermöglicht mehrere Maßstäbe.
    - [ ] Die Ansicht der Polygone ist ohne Internetverbindung möglich.

## Verwaltung von Schadensfällen

> Als Gutachter möchte ich Schadensfälle verwalten (erfassen/bearbeiten/löschen) können.

- Aufwandsschätzung: *TODO*
- Akzeptanztests: 
    - [ ] Schadensfälle können mit der Angabe des Versicherungsobjekts (Name des Versicherungsnehmers, Fläche und Koordinaten des Objekts, Region (mind. Landkreis)), Schadensinformationen (Schadensfläche, Schadensposition, Schadens-Koordinaten/-Polygon, Datum) und Name des Gutachters erfasst werden.
    - [ ] Die Erfassung von Schadensfällen/-Koordinaten verwendet tatsächliche Sensorwerte eines Positionssensors im Gerät.
    - [ ] Schadensfälle sind nach dem vollständigen Schließen der App und Starten der App wieder im gleichen Zustand verfügbar.
    - [ ] Schadensfälle können während des Erfassens in der Kartenansicht (*siehe Visuelle Darstellung der Schadensfälle*) dargestellt werden.
    - [ ] Schadensfälle können während des Bearbeitung in der Kartenansicht (*siehe Visuelle Darstellung der Schadensfälle*) dargestellt werden.
    - [ ] Schadensfälle können nach Name des Versicherungsnehmers gesucht werden.
    - [ ] Schadensfälle können gelöscht werden.
    - [ ] Schadensfälle können bearbeitet werden.
    - [ ] Die Verwaltung ist ohne Internetverbindung möglich.

