# Meeting scheduler

Name: Meeting scheduler ID:4 Difficulty:A Propose: CGI

--------------
Construiti o aplicatie grafica care va putea gestiona meeting-urile (sedintele) cu ajutorul unei
baze de date PostgreSQL . Aceasta va permite interactiunea cu utilizatorul printr-un meniu cu
urmatoarele comenzi:
- Adugarea unei persoane in baza de date
- Stabilirea unui viitor meeting ( data de inceput, data de sfarsit, lista persoanelor care
vor participa )
- Afisarea sedintelor dintr-un anumit interval de timp
- Export/Import intr-un format de calendar standard (fie ical, fie ics, etc). Se va face
export-ul/importul doar catre un singur format.
Aplicatia va face validarea input-ului dat de utilizator si va face error handling in sensul ca va
afisa un mesaj sugestiv in cazul aparitiei unei exceptii.

-----------------------
INPUT: Interfata cu meniu interactiv
Ex. adauga persoana Ion Popescu
adauga sedinta care va incepe la 2020-11-20 14:00, se va termina la 2020-11-20 14:30
si la care vor participa Ion Popescu, Ana Maria
afiseaza sedintele din intervalul 2020-11-20 08:00, 2020-11-20 23:59

----------------------
OUTPUT:
Orice metoda de afisare este OK
