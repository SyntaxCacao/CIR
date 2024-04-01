# CIR: Übersetzung S. P. Scott

In diesem Ordner befindet sich die Übersetzung der Digesten ins Englische von *Samuel P. Scott* (aus: The Civil Law, 
Cincinnati 1932, 17 Bd.) in maschinenlesbarer Form.

Die Transkription wurde in Rohform zunächst einer Seite der Université Grenoble Alpes entnommen 
([*The Roman Law Library*](https://droitromain.univ-grenoble-alpes.fr/) by Y. Lassard & A. Koptev, dort die
[Scott-Übersetzung](https://droitromain.univ-grenoble-alpes.fr/Anglica/digest_Scott.htm)).
Der HTML-Code wurde mit einem Skript in die Form der Datei `digesta_scott.txt` überführt und dann von Hand noch 
erheblich überarbeitet. Abgesehen von Änderungen, die bloß die äußere Gestalt des Textes betreffen, ist auch die 
Zuordnung der einzelnen Textpartien zu den Stellennummern möglichst der Ausgabe Mommsens angeglichen worden, was eine 
erhebliche Abweichung von Scotts Original bedeutet. Näheres in den Notizen am Ende dieser Datei.

Jede Zeile in der Datei `digesta_scott.txt` entspricht einem dieser vier regulären Ausdrücke (hier Python) und kann so 
gelesen werden:

```
# Book
r"^(\d+) (.+)$"
# Title
r"^(\d+,\d+) (.+)$"
# Fragment
r"^(\d+,\d+,\d+a?) (.+)$"
# Paragraph
r"^(\d+,\d+,\d+a?,\d+[a-e]?) (.+)$"
```

Der Paragraphentext enthält `<i>`-Elemente, wo Scotts Text kursiv gesetzt ist. Problematisch sind bislang noch die 
griechischen Partien, die teilweise nur mit lateinischen Buchstaben transkribiert sind.

## Zur Angleichung an Mommsens Stellennummerierung

Das Skript `compare.py` vergleicht die in Mommsens Text vorhandenen Stellen mit denen bei Scott. Dabei werden die unten 
aufgeführten Unterschiede ignoriert.

### Bemerkungen zu Änderungen

* 28,5,93,1 (fr. beginnt mit § 1 statt pr.) war bei Scott eben pr.; an Mommsen angepasst
* 30,108,15 bis 30,112,1 (Bd. 4, S. 54) hat komplett gefehlt, stattdessen stand dort: "Lacunas : 108, 15 – 112, 1"
* 34,5,6: Scott Marcianus; Momm. Maecianus
* 37,1,37,1a: Bei Mommsen wurde offenbar ein Teil vom pr. zu § 1 und der vorige § 1 zu § 1a; der neue § 1 war dann 
  nicht mehr Teil des Zitats im pr. Bei Scott ist er es aber sehr wohl noch.
* 37,1,37,1a und 39,2,24,1a: Offenbar verwendet Mo. 1a usw., wenn ein früherer § 1 nun zu § 1a umbenannt wird, weil ein 
  früherer weiter geteilt wird
* Bei 4,3,9,4a anders: hier wurde § 4 zu § 4 und § 4a aufgesp.
* Nach 43,5,15 hat Scott offenbar den verbleibenden Teil des Titels in einen eigenen Titel 6 abgespaltet. Die folgenden 
  Titel waren eine Nummer höher nummeriert. Das war rückgängig zu machen.
* Bei den Fr. 49,13,1,2–49,13,2,0 im Scott-Original handelt es sich offenbar um Texte, die infolge eines Druckfehlers 
  an die Stelle 49,14,1,2–49,14,2,0 gehören. Sie wurden hier nun dorthin verschoben.

### Bleibende Unterschiede

* 5,1,49,1: Bei Scott fehlend.
* 9,2,17,1: Bei Mommsen nicht vorhanden, siehe Anm. bei Mo. im App.
* 19,5,27: Fehlt tatsächlich, 19,5,26 vermutl. unvollständig
* 22,3,30 und 31: Bei Scott vorhanden, bei Mommsen nicht. Zunächst im Dokument belassen.
* 26,4,11: Fehlt bei Scott.
* 28,8,7,1–3: Fehlt bei Scott.
* 30,0,41,16: Fehlt bei Scott.
* 34,5,4 bei Scott ist bei Mommsen nicht vorhanden; beibehalten als 34,5,3a
* 34,5,5 ist bei Mommsen 34,5,4; entsprechend angepasst
* 36,1,45 (und wohl 36,1,44 i.f.) bei Scott nicht vorhanden.
* 36,1,84 und 85: bei Scott nicht vorhanden.
* 36,4,16 und 17: bei Scott nicht vorhanden.
* 38,2,8,5: Fehlt offenbar bei Scott.
* 40,13,5: Fehlt offenbar bei Scott.
* 41,3,4,25 bei Scott ist bei Mom. offenbar gestrichen worden, deshalb hat das fr. bei Scott einen § zu viel. Der § 
  wurde bei Scott nun zu 24a umbenannt, damit er nicht mehr mit Mo. assoziiert wird.
* 44,2,8: Dieses Fr. kommt bei Scott nicht vor, in der Online-Fassung stand ("Lacuna: 8"), was entfernt wurde.
* 46,8,26: Bei Scott nicht vorhanden
* 47,2,38a: Das bei Scott als 38 nummerierte fr. ist bei Mo. nicht vorhanden. Es ist deshalb bei Scott jetzt als 37a 
  bezeichnet, die nachfolgenden fr. haben eine entsprechend niedrigere Nummer erhalten.
* 47,7,3,5a: Bei Scott waren §§ 5, 5a einfach § 5, offenbar hat Mommsen dazwischen noch Worte eingefügt, die bei Scott 
  fehlen. Am Text nichts verändert.
* 48,8,15,1: Bei Mommsen nicht vorhanden.
* 48,13,13,1: Bei Mommsen nicht vorhanden.
* 49,13,1,2–49,13,2: Bei Mommsen nicht vorhanden.
* Bei 49,14,17,0 ff. standen die Texte, die zu 49,14,18 gehören.
  Die richtige Inskr. zu 49,14,17 wurde entfernt, da ihr der Text fehlt:
  `49,14,17 Modestinus, On Punishments, Book II.`
  Die Inskr. zum (neuen) 49,14,18 wurde von einer anderen Stelle kopiert.
* 49,15,22,2a: Bei Scott nicht vorhanden.

