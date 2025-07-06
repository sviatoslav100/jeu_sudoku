from random import randint

def CreerLigne():       #Crée une matrice à une seule dimention en choissisant les nombres de 1 à 9
    L,numéros = [[]],list('123456789')
    while len(L[-1]) != 9:
        L[-1] += numéros.pop(randint(0,len(numéros)-1))

    return L


def GetLongueur(l):
    L = []
    for i in range(len(l)-1):
        L.append(l[i][len(l[-1])])
    return L


def RecupererZone(l): 
    """
    
    Cette fonction retourne une liste contenant les valeurs de la zone de la grille où se trouve la case donnée. 
    Les zones sont les carrés de 3x3 qui composent la grille.
    
    """
    x ,y,L = len(l), len(l[-1]) ,[]
    if x <= 3:
        x = 0
    elif 4<= x <=6:
        x = 3
    else:
        x = 6
    
    if y < 3:
        y = [0,3]
    elif 3<= y <6:
        y = [3,6]
    else :
        y = [6,9]
    
    for _ in range(x,len(l)):
        L.extend(l[_][y[0]:y[1]])
    return L

def VerifierValeur(l,n): #Vérifie si la variable n peut être placée dans la ligne
    if n not in l[-1] and n not in GetLongueur(l) and n not in RecupererZone(l):
        return True
    return False

def CreerGrille():
    l, y = CreerLigne(), 0
    while len(l) != 9:
        ns, l, x = list('123456789'), l + [[]], 0
        while len(l[-1]) != 9:
            x, n = x + 1, ns.pop(randint(0, len(ns) - 1))
            if x == 40:
                y += 1
                del l[-1]
                break
            if y == 10:
                del l[-1], l[-1]
                y = 0
                break
            if VerifierValeur(l, n):
                l[-1] += n
            else:
                ns.append(n)
    return l


def ViderGrille(grille):  #De façon aléatoire on enlève les chiffres dans la grille
    for i in range(9):
        n = randint(2,7)
        for j in range(n):
            n = randint(0,8)
            grille[i][n] = ''
    return grille

def VerifierSolution(grille): #La fonction vérifie que la grille est valide càd que la somme de chaque ligne/colonne/cube = 9
    lignes = []
    while grille != []:
        lignes.append(grille[:9])
        del grille[:9]
    n = set('123456789')
    for ligne in lignes:
        if n != set(ligne):
            return False
    for x in lignes[:3],lignes[3:6],lignes[6:]:
        box1 = []
        box2 = []
        box3 = []
        [box1.extend(ligne[:3]) for ligne in x]
        [box2.extend(ligne[3:6]) for ligne in x]
        [box3.extend(ligne[6:9]) for ligne in x]
        if n != set(box1) or n != set(box2) or n != set(box3):
            return False
    for x in range(9):
        ligne = []
        for y in range(9):
            ligne.append(lignes[y][x])
        if set(ligne) != n:
            return False
        return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
"""
# Test de la fonction CreerLigne
assert len(CreerLigne()) == 1
assert len(CreerLigne()[0]) == 9

# Test de la fonction GetLongueur
L = [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
assert GetLongueur(L) == ['4', '5', '6', '7', '8', '9', '1', '2', '3']

# Test de la fonction RecupererZone
L = [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']]
assert RecupererZone(L) == ['1', '2', '3', '2', '3', '4', '3', '4', '5']

# Test de la fonction VerifierValeur
L = [['1', '2', '3', '4', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', '']]
assert VerifierValeur(L, '5') == True
assert VerifierValeur(L, '2') == False

# Test de la fonction ViderGrille
grille_test = [    ['2', '7', '8', '1', '5', '4', '6', '9', '3'],
    ['5', '1', '6', '7', '3', '9', '4', '8', '2'],
    ['4', '3', '9', '6', '2', '8', '1', '5', '7'],
    ['7', '2', '4', '5', '1', '3', '8', '6', '9'],
    ['9', '5', '1', '8', '7', '6', '3', '2', '4'],
    ['6', '8', '3', '9', '4', '2', '7', '1', '5'],
    ['3', '9', '2', '4', '8', '1', '5', '7', '6'],
    ['8', '4', '5', '2', '6', '7', '9', '3', '1'],
    ['1', '6', '7', '3', '9', '5', '2', '4', '8']
]
grille_vide = ViderGrille(grille_test)
print(grille_vide)

# Test de la fonction VerifierSolution
grille_correcte = [    ['2', '7', '8', '1', '5', '4', '6', '9', '3'],
    ['5', '1', '6', '7', '3', '9', '4', '8', '2'],
    ['4', '3', '9', '6', '2', '8', '1', '5', '7'],
    ['7', '2', '4', '5', '1', '3', '8', '6', '9'],
    ['9', '5', '1', '8', '7', '6', '3', '2', '4'],
    ['6', '8', '3', '9', '4', '2', '7', '1', '5'],
    ['3', '9', '2', '4', '8', '1', '5', '7', '6'],
    ['8', '4', '5', '2', '6', '7', '9', '3', '1'],
    ['1', '6', '7', '3', '9', '5', '2', '4', '8']
]
grille_incorrecte = [    ['2', '7', '8', '1', '5', '4', '6', '9', '3'],
    ['5', '1', '6', '7', '3', '9', '4', '8', '2'],
    ['4', '3', '9', '6', '2', '8', '1', '5', '7'],
    ['7', '2', '4', '5', '1', '3', '8', '6', '9'],
    ['9', '5', '1', '8', '7', '6', '3', '2', '4'],
    ['6', '8', '3', '9', '4', '2', '7', '1', '5'],
    ['3', '9', '2', '4', '8', '1', '5', '9', '9'],
    ['3', '9', '2', '4', '8', '1', '5', '9', '9'],
    ['3', '9', '2', '4', '8', '1', '5', '9', '9'],
    
    
    ]

"""

