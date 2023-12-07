# README TEMA1 ISC
### CRYPTO ATTACK
Rezolvare:
1. `message.txt` contine un mesaj de tip json in base64 unde gasesti:
    * `n`
    * `e`
    * `flag` (encriptat)
2. la server se poate trimite un `mesaj codat in base64`, din
care se extrage flagul encriptat, iar serverul iti trimite
inapoi fie mesajul "the flag is valid", fie `mesajul decriptat`
3. pentru a obtine flagul decriptat, se foloseste `"chosen
RSA attack"`
4. ideea de baza consta in trimiterea `(flag ului criptat x nr criptat)`
pentru a primi inapoi mesajul decriptat sub forma `(flag x nr)`
5. cum se stie nr initial, se poate afla cu usurinta flagul impartind 
raspunsul primit de la server la nr initial ales
6. pentru usurinta, se modifica scriptul initial pentru a satisface toti pasii

Flagul este: `SpeishFlag{AOXf0JYBUWteUxxTWO9gh7eb47xBPF9R}`

### LINUX ACL
Rezolvare:
1. te conectezi cu cheia ssh la server si se inspecteaza folderul
din `/usr/local/bin`
2. se observa 3 scripturi:
    * `janitor-coffe.sh` -> se observa ca nu se poate rula
    robot-sudo 
    * `janitor-vacuum.sh` -> se observa ca se poate rula robot-sudo
    folosind calea absoluta /usr/local/bin/vacuum-control
    * `vacuum-control` -> se observa ca se face o filtrare a utilizatorilor
    dupa id
3. cu comanda ls -al observam ca robot-sudo are alt owner si grup
4. se inspecteaza cu `strings robot-sudo` si observam un configuration
file unde se afla 2 reguli:
    * `allow roombax /usr/bin/askundete/b0ss-call`
    * `allow janitor /usr/local/bin/vacuum-control`
5. se inspecteaza cu `strings b0ss-call` si dam de urmatoarele informatii:
    * `b72b3b726420bdc905b71005b1a67431` (pare un argument)
    * Access denied! (daca nu se da argumentul de mai sus)
    * I will contact you when I require your cleaning services, janitor!
    * Congratulations, here's your flag: (se da argumentul corect)
    * `cat /usr/lib/ziggy/damn/.my.flag` (se afla flagul)
6. trebuie sa incercam sa rulam `b0ss-call` cu argumentul lung de mai 
sus
7. `roombax` poate sa apeleze `b0ss-call`, iar janitor poate sa apeleze 
`vacuum-control`
8. facem un script care sa apeleze b0ss-call cu arg si sa faca match pe
numele `vacuum-control`, pentru ca suntem janitor

Flagul este: `SpeishFlag{yQI5ZR9F1pVIR7mzRtb3VQVTpRh4IUxU}`

### BINARY EXPLOIT
Rezolvare:
1. se inspecteaza executabilul cu ghidra unde se observa
ca vectorul ce contine numerele e plasat `relativ la stiva`
2. exista astfel situatia in care se poate face un atac
de tip overflow, adaugand `nr maxim de numere` (de tip uint) + `adresa lui win` 
(extrasa tot din ghidra) + `4 bytes` (old ebp) + `lucky number ul`
3. se ruleaza pe server si se obtine flag ul corespunzator

Flagul este: `SpeishFlag{JcaHUnSRHtdXP8UHnSfaX44QmcXvk1lb}`

