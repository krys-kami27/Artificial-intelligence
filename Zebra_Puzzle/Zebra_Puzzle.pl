/*
Krystian Kamiński nr 304013

Zagadka Einsteina: 5 ludzi różnych narodowości zamieszkuje 5 domów
w 5 różnych kolorach.
Wszyscy palą 5 różnych wyrobów tytoniowych i piją 5 różnych napojów.
Hodują zwierzęta 5 różnych gatunków. Który z nich trzyma w domu rybki?
Który z nich pije wodę?

Kanadyjczyk zamieszkuje pierwszy dom
Hiszpan mieszka w czerwonym domu.
Zielony dom znajduje się bezpośrednio po lewej stronie domu białego.
Szkot pija herbatkę.
Palacz papierosów light mieszka obok hodowcy kotów.
Mieszkaniec żółtego domu pali cygara.
Niemiec pali fajkę.
Mieszkaniec środkowego domu pija mleko.
Palacz papierosów light ma sąsiada, który pija wodę.
Palacz papierosów bez filtra hoduje ptaki.
Francuz hoduje psy.
Kanadyjczyk mieszka obok niebieskiego domu.
Hodowca koni mieszka obok żółtego domu.
Palacz mentolowych pija piwo.
W zielonym domu pija się kawę.
*/

baza_wiedzy(Domy) :-
    % (narodowosc, kolor domu, wyrob tytoniowy, napoj, zwierze)
    % narodowosci: kanadyjczyk, hiszpan, szkot, francuz, niemiec
    % wyroby: light, cygaro, fajka, bez_filtra, mentolowy
    % napoje: herbata, mleko, woda, piwo, kawa
    % kolor domu: bialy, czerwony, zolty, niebieski, zielony
    % zwierzeta: kon, pies, kot, ptak, ryba
    Domy = [_,_,_,_,_],
    Domy = [(kanadyjczyk,_,_,_,_)|_],
    member((hiszpan,czerwony,_,_,_), Domy),
    lewo((_,zielony,_,_,_), (_,bialy,_,_,_), Domy),
    member((szkot,_,_,herbata,_), Domy),
    sasiad((_,_,light,_,_), (_,_,_,_,kot), Domy),
    member((_,zolty,cygaro,_,_), Domy),
    member((niemiec,_,fajka,_,_), Domy),
    Domy = [_,_,(_,_,_,milk,_),_,_],
    sasiad((_,_,light,_,_), (_,_,_,woda,_), Domy),
    member((_,_,bez_filtra,_,ptak), Domy),
    member((francuz,_,_,_,pies), Domy),
    sasiad((kanadyjczyk,_,_,_,_), (_,niebieski,_,_,_), Domy),
    sasiad((_,_,_,_,kon), (_,zolty,_,_,_), Domy),
    member((_,_,mentolowy,piwo,_), Domy),
    member((_,zielony,_,kawa,_), Domy),
    member((_,_,_,_,ryba), Domy).

sasiad(Lewy, Prawy, Domy) :-
    append(_, [Lewy,Prawy|_], Domy).

sasiad(Lewy, Prawy, Domy) :-
    append(_, [Prawy,Lewy|_], Domy).

lewo(Lewy, Prawy,Domy) :-
    append(_, [Lewy,Prawy|_], Domy).

kto_pije_wode(Kraj) :-
    baza_wiedzy(Domy),
    member((Kraj,_,_,woda,_), Domy).

kto_ma_rybki(Kraj) :-
    baza_wiedzy(Domy),
    member((Kraj,_,_,_,ryba), Domy).

/** <examples>
?- kto_ma_rybki(Kraj).
?- kto_pije_wode(Kraj).
*/
