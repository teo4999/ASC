Nume: Hossu Teodor-Ioan
Grupă: 335CB

# Tema 1 ASC

Organizare
-

* Am folosit dicţionare şi lock-uri deoarece mi s-au părut mai uşor de utilizat
(self.producers = {}, self.carts = {}, self.lock_register = Lock(),
self.lock_carts = Lock()). Producătorii sunt definiţi de un dicţionar care
include toate produsele aferente fiecărui producător (fiecare producător este
identificat prin id-ul său). Analog şi în cazul coşului fiecărui consumător.
* Tema este utilă deoarece ne ajută să ne familiarizăm cu paralelismul în
Python.
* Implementarea o consider eficientă.
* Funcţia remove_from_cart din marketplace.py returnează True sau False (dacă
s-a executat cu succes sau nu), chiar dacă în enunţ nu este specificat să
returneze.


Implementare
-

* Întregul enunț al temei e implementat.
* Nu există funcționalități extra.
* Nu există dificultăți întâmpinate.
* Lucruri interesante descoperite pe parcurs: tema funcţionează şi fără
lock-uri datorită dicţionarelor care se sincronizează automat.


Resurse utilizate
-

* https://ocw.cs.pub.ro/courses/asc/laboratoare/02
* https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/

Git
-
* https://github.com/teo4999/ASC
