import tkinter
from tkinter import messagebox


import algo  #fichier python qui contient toutes les fonctions qui vérifient les conditions du jeu + gère la création de la grille

fenetre = tkinter.Tk() #Def de la fenêtre
fenetre['bg'] = 'black' #La coleur du fond(background)
fenetre.title('Jeu de Sudoku')  #Le titre de la fênetre
fenetre.geometry('578x660+500+150') #on crée une fenêtre de taille 578х660 et on essayé de la cadre à peu près au milieu de l'écran lorsqu'elle s'ouvre

    


class Sudoku:
    """
    
    
    """
    def __init__(self): #constructeur
        

        self.grille = algo.CreerGrille()    #grille du jeu
        self.lines = algo.ViderGrille(tuple(list(tuple(L)) for L in self.grille))   #la grille avec des vides
        self.entrée_widget = [] 
        self.valeurs = []   
        self.b = 0  



        
        print(self.grille)
        
        x = 5   #x et y utilisées pour placer des widgets(coordonnées)
        y = 0
        n = 0   #cette variable est utilisée pour numéroter les entrées
        
        for i in range(9):
            for j in range(9):  #les boucles permettent de parcourir toutes les cases de la grille
                self.valeurs.append(tkinter.StringVar())
                self.entrée_widget.append(tkinter.Entry(width=2, font=("", 40, "bold"), textvariable=self.valeurs[-1],
                                             justify=tkinter.CENTER,)) #on crée un objet stringvar et un widget pour chaque case de la grille et ensuite on ajoute les deux dans les listes 
                
                if self.lines[i][j]:    
                    self.entrée_widget[n].config(bg='#add8e6', fg='black')
                    self.valeurs[n].set(self.lines[i][j])
                    self.configurer_commande_valeur_speciale(n, self.lines[i][j])
                else:
                    self.configurer_commande_valeur(n)
                    


                self.entrée_widget[-1].place(x=x, y=y)
                n += 1
                x += 62
                if j == 2 or j == 5:
                    x += 4

                    
            y += 66 #maj des variables x et y 
            x = 5
            if i == 2 or i == 5:    #si c'est la 3ème ou la 6ème case on rajoute un petit espace entre les carrés 3x3
                y += 4


        bouton_quitter = tkinter.Button(text='Quitter', bg='black', fg='red', width=10, font=('', 15, 'bold'), bd=3, command=fenetre.destroy)
        bouton_quitter.place(x=440, y=610)
        
        bouton_verifier = tkinter.Button(text='Vérifier', bg='black', fg='red', width=10, font=('', 15, 'bold'), bd=3, command=self.Vérifier)
        bouton_verifier.place(x=5, y=610)
        
        bouton_recommencer = tkinter.Button(text='Recommencer', bg='black', fg='red', width=10, font=('', 15, 'bold'), bd=3, command=self.Recommencer)
        bouton_recommencer.place(x=300, y=610)
        
        bouton_solution = tkinter.Button(text='Solution', bg='black', fg='red', width=12, font=('', 15, 'bold'), bd=3, command=self.Solutionn)
        bouton_solution.place(x=140, y=610)
        
        

    def configurer_commande_valeur(self, v):
        
        class CommandeValeur:
            
            def __init__(self, valeurs, v):
                self.v = v 
                self.valeurs = valeurs
                
            def mettre_a_jour(self,*argv):
                
                s = self.valeurs[self.v].get()
                if s:
                    if s.isnumeric() and "0" not in s:
                        self.valeurs[self.v].set(s[-1])

                    else:
                        self.valeurs[self.v].set('')
    
        C = CommandeValeur(self.valeurs, v)
        self.entrée_widget[-1].config(xscrollcommand=C.mettre_a_jour)



    def configurer_commande_valeur_speciale(self, v, x):
        
        class CommandeValeurSpeciale:
            """
            
            """
            def __init__(self, valeurs, v, x):
                self.v = v
                self.x = x
                self.valeurs = valeurs

            def mettre_a_jour(self, *argv):

                self.valeurs[self.v].set(self.x)

        C = CommandeValeurSpeciale(self.valeurs, v, x)
        self.entrée_widget[-1].config(xscrollcommand=C.mettre_a_jour)

    def Solutionn(self):
        """
        Cette fonction vérifie si l'utilisateur a gagné ou pas'
        Return :
            elle renvoie soit le message de la victoire soit renvoie un message qui propose de revérifier 
            ses réponses 
        """            
        x = 0
        for i in range(9):
            for j in range(9):
                self.valeurs[x].set(self.grille[i][j])
                x+=1
                                
    def Vérifier(self):
        """
        Cette fonction vérifie si l'utilisateur a gagné ou pas'
        Return :
            elle renvoie soit le message de la victoire soit renvoie un message qui propose de revérifier 
            ses réponses 
        """        
        L = []
        for i in range(81):
                L.append(self.valeurs[i].get())
                
        if not algo.VerifierSolution(L):
                messagebox.showinfo('Question','Vérifiez encore une fois les solutions proposées')
                
        else:
                self.Victoire()
                    
    def Recommencer(self):
        """
        Cette fonction affiche à l'utilisateur le message qui lui demande s'il souhaite continuer
        (refaire une deuxième)
        En fonction de son choix elle soit ne fait rien, soit fait appel à la classe Sudoku(recommence la partie)
    
        Return :
            elle ne renvoie rien
        """
        
        if messagebox.askyesno('Question','Voulez vous rejouer ?'):
                    Sudoku()
                    
    def Victoire(self):
        """
        Cette fonction affiche à l'utilisateur le message de la victoire lorsqu'il gagne la partie.
        Elle fait appel à une autre fonction qui lui demande si le joeur souhaite de recommencer la partie
        
        Return :
            elle ne renvoie rien
        """
        
        
        messagebox.showinfo("Affichage","Vous avez gagné! Bravo!")
        self.Recommencer()



Sudoku()

fenetre.mainloop()

#                
#                vérifient si la case courante doit être remplie avec une valeur pré-remplie (si self.lines[i][j] est différent de zéro), 
#                et configurent le widget Entry() en conséquence. Si la case n'a pas de valeur pré-remplie, la méthode configurer_commande_valeur(n) 
#                est appelée pour configurer les commandes de la case.
#                

#                
#                ces lignes placent le widget Entry() courant sur la grille graphique, et mettent à jour la 
#                position horizontale x et le compteur de case n. Si la case courante est la troisième ou la 
#                sixième dans la ligne, la position horizontale est ajustée pour ajouter un petit espace entre 
#                les groupes de trois cases.
#    
