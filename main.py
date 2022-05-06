import random

class Carte :
    def __init__(self,nom,mana,description):
        self.__name = nom
        self.__mana = mana
        self.__description = description
    def getName(self):
        return self.__name
    def getMana(self):
        return self.__mana
    def getDescription(self):
        return self.__description

class Creature(Carte):
    def __init__(self,nom,mana,description,attaque,pv):
        self.__name = nom
        self.__mana = mana
        self.__description = description
        self.__attaque = attaque
        self.__pv = pv
    def getName(self):
        return self.__name
    def getMana(self):
        return self.__mana
    def getDescription(self):
        return self.__description
    def getAttaque(self):
        return self.__attaque
    def getPV(self):
        return self.__pv

class Cristal(Carte):
    def __init__(self,nom,mana,description,value):
        self.__name = nom
        self.__mana = mana
        self.__description = description
        self.__value = value
    def getName(self):
        return self.__name
    def getMana(self):
        return self.__mana
    def getDescription(self):
        return self.__description
    def getScrore(self):
        return self.__value
    

class Mage :
    def __init__(self,nom):
        self.__name = nom
        self.__pv = 50
        self.__mana = 5
        self.__sauvegardeMana = 5
        self.__mainNom = [0,0,0,0,0]
        self.__mainMana = [0,0,0,0,0]
        self.__defausse = [0]
        self.__zone = [0,0,0,0,0]
    def getName(self):
        return self.__name
    def getPV(self):
        print("Vous avez",self.__pv,"PV")
        return self.__pv
    def getMana(self):
        print("Vous avez",self.__mana,"mana")
        return self.__mana
    def getMain(self):
        for i in range (5):
            alea=random.randint(0,7)
            self.__mainNom[i] = deck[alea].getName()
            self.__mainMana[i] = deck[alea].getMana()
            print(self.__mainNom[i])
        return self.__mainNom
    def getDefausse(self):
        return self.__defausse
    def getZone(self):
        print(self.__zone)
        return self.__zone
        #actions
    def jouerCarte(self):
        jouer=int(input("Quelle carte voulez-vous jouer ? "))
        endroit=int(input("Dans quel emplacement de la zone de jeu ? "))
        self.__zone[endroit] = self.__mainNom[jouer]
        print(self.__zone)
        self.__mana -= self.__mainMana[jouer]
        print("Il vous reste",self.__mana,"mana.")
        self.__mainNom[jouer]=0
        return self.__zone,self.__mainNom,self.__mana
    def recupMana(self):
        self.__mana = self.__sauvegardeMana 
        return self.__mana
    def attaquer(self,attaqueCreature):
        self.__zone[attaqueCreature].getName()
        return self.__zone


dragon = Creature("Dragon",5,"éloigner vos forets",4,20)
gobelin = Creature("Gobelin",2,"Gnéhéhéhé",4,20)
chevalier = Creature ("Chevalier",3,"le paladin noir",4,20)
loup = Creature("Loup",3,"Gros loup",4,20)
sanglier = Creature("Sanglier",2,"Gruiiik",4,20)
cristal = Cristal("Cristale ",1,"rajoute 1 à votre mana",1)
deck=[dragon,gobelin,chevalier,loup,sanglier,cristal]
joueur1 = Mage("le mage noir")
joueur2 = Mage("le mage blanc")
attaqueCreature=0
game=True
tour=0
while (game!=False):
    tour+=1
    print("Tour",tour)

    print("C'est à",joueur1.getName(),"de jouer")
    joueur1.getPV()
    joueur1.getMana()

    print("Voici votre main :")
    joueur1.getMain()
    joueur1.jouerCarte()
    truc = int(input("Souhaitez-vous jouer une autre carte(1) ou passer à la phase d'attaque(2) ?"))
    if (truc == 1):
        joueur1.jouerCarte()
    print("A vous de jouer !")
    joueur1.getZone()
    attaqueCreature = int(input("Quelle créature souhaite-vous activer ?"))
    joueur1.attaquer(attaqueCreature)
    print("C'est à",joueur2.getName(),"de jouer")
    joueur2.getPV()
    joueur2.getMana()
 

    print("Vos cartes")
    joueur2.getMain()
    joueur2.jouerCarte()



