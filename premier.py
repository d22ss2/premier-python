#mon premier code pythonformation pytho
#print(type(nom))
#print(type(age))
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
#try equivalent si ou if.... essaye d'effectuer cette ligne. except.... s'il y'a erreur faire
        try:
            age_int = int(age_str) 
        except:
            print("ERREUR: veillez entrer un nombre pour l'age")
    return age_int

def afficher_resultat(nom_personne, age_personne):
    print()
    print("Je me nomme "+ nom_personne +", j'ai " + str(age_personne) +" ans")
    print("L'annee prochaine j'aurais "+ str(age_personne + 1) + " ans")

    age = 0
    if age == 1 or age == 2:
        print("je suis un bebe")
    elif age >= 12 and age < 18:
        print("je suis adolescent")
    elif age < 18:
        print("je suis mineur")
    elif age >= 18:
        print("je suis majeur")



""" #demander le nom
nom1 = demander_nom()
nom2 = demander_nom()
#demander l'age
    
age1 = demander_age(nom1)
age2 = demander_age(nom2)

#afficher les resultats

#str(age)->"18"
afficher_resultat(nom1, age1)
afficher_resultat(nom2, age2)

"""
for i in range(0,3):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_resultat(nom, age)