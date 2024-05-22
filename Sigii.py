import bz2
import json

def sec(cas):
    h, m, s = cas.split(':')
    return (int(h) * 3600 + int(m) * 60 + int(s))


def upravgraf(g):
    for a in g:
            for i in g[a]:
                x = sec(i[2]) - sec(i[1])
                i.append((x))

    nemavrchol = []

    for vrchol in g:
        for soused,a,b,c,d in g[vrchol]:
             if soused not in g:
                 nemavrchol.append(soused)

    for vrchol in nemavrchol:
        g[vrchol] = []

    return (g)

                                                    #program se jmenuje podle Sigismunda Dijkstry, postavy ze Zaklínače s povědomým příjmením
def Sigi():                          
    g = json.load(bz2.open("graf.json.bz2"))        #stanice piště ve formátu - "jménostanice" - například:"Letňany"
    start = input('Zadej výchozí stanici:  ')       # ano i s uvozovkami
    cil = input('Zadej cílovou stanici:  ')
    cas = input('Zadej čas:  ')                     #čas piště ve formátu - hh:mm:ss - například: 12:00:00               

#Ukázka vstupu a výstupu
#Zadej výchozí stanici:  "Skalka"
#Zadej cílovou stanici:  "Letňany" 
#Zadej čas:  12:00:00
#Linkou 195 ze stanice "Skalka"
#   Odjezd: 12:01:00
#   Příjezd: 12:16:00
#Na stanici "K Žižkovu" přestupte na linku 183
#   Odjezd: 12:16:00
#   Příjezd: 12:24:00
#Na stanici "Prosek" přestupte na linku 195
#   Odjezd: 12:24:00
#V 12:28:00 jste v cílové stanici "Letňany"

#Testovaci graf:1
    #g = {'a': [['b', '2:54:50', '5:35:00', 111], ['c', '5:24:50', '5:35:00', 'A'],['s', '5:54:50', '8:35:00', 500]],
    #        'b': [['a', '1:54:50', '5:35:00', 500], ['d', '0:54:50', '5:35:00', 'A']],
    #        'c': [['a', '5:14:50', '5:35:00', "B"], ['d', '3:54:50', '5:35:00', 568], ['t', '0:00:50', '5:35:00', 'B']],
    #        'd': [['b', '5:14:50', '5:35:00', 544], ['c', '2:54:50', '5:35:00', 450],['t', '5:0:50', '5:35:00', "B"]],
    #        't': [['c', '5:14:50', '5:35:00', 450], ['d', '0:24:50', '5:35:00', 567]]}
    
    graf = upravgraf(g)
    shortest = {}
    kudykam = {}
    kudytam = []
    unseen = graf
    
    for vrchol in unseen:
        shortest[vrchol] = float("inf")
    shortest[start] = 0
    
    while unseen:
        nejbliz = None

        for vrchol in unseen:
            if nejbliz is None:
                nejbliz = vrchol
            elif shortest[vrchol] < shortest[nejbliz]:
                nejbliz = vrchol

        cesty = []

        for cesta in graf[nejbliz]:
            if sec(cas) < sec(cesta[1]):
                cesty.append(cesta)
                 
        for soused, kdy, kdytam, linka, delka in cesty:
            current_cas = sec(cas) + shortest[nejbliz]
            wait = sec(kdy) - current_cas
            if delka + shortest[nejbliz] + wait < shortest[soused] and sec(kdy) >= current_cas:
                shortest[soused] = delka + shortest[nejbliz] + wait
                kudykam[soused] = [nejbliz, kdy, kdytam, linka, delka]
        unseen.pop(nejbliz)

    current = cil
    kdy, kdytam, linka, delka = 0,0,0,0
    
    while current != start:
        kudytam.insert(0,[current,kdy, kdytam, linka, delka])
        current,kdy, kdytam, linka, delka = kudykam[current]

                
    kudytam.insert(0,[start,kdy, kdytam, linka, delka])

    vcili = kudytam[-2][2]
    
    print("Linkou "+ kudytam[0][3] + " ze stanice " + kudytam[0][0])
    print("   Odjezd: " + kudytam[0][1])
    
    linka = kudytam[0][3]
    
    while len(kudytam) != 0:
        for spoj in kudytam:
            kudytam = kudytam[1:]
            if len(kudytam) == 0:
                break
            if spoj[3] != linka:
                print ("   Příjezd: " + prijezd )
                linka = spoj[3]
                print("Na stanici " + spoj[0] +
                      " přestupte na linku " + spoj[3])
                print("   Odjezd: " + spoj[1])
                prijezd = spoj[2]
                break
            prijezd = spoj[2]
    print("V "+ vcili + " jste v cílové stanici " + cil)
    g = json.load(bz2.open("graf.json.bz2"))

Sigi()
        

