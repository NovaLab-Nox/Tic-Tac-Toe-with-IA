import math

# Fonction pour jouer une partie
def jouer_tic_tac_toe():
    plateau = [" "] * 9
    joueur_humain = "X"
    joueur_ia = "O"
    joueur_actuel = joueur_humain

    while True:
        afficher_plateau(plateau)

        if joueur_actuel == joueur_humain:
            position = obtenir_position(joueur_humain, plateau)
        else:
            print("L'IA réfléchit...")
            position = meilleur_coup(plateau, joueur_ia)

        plateau[position] = joueur_actuel

        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            if joueur_actuel == joueur_humain:
                print("Félicitations, vous avez gagné ! 🎉")
            else:
                print("L'IA a gagné ! 😢")
            break

        if " " not in plateau:  # Match nul
            afficher_plateau(plateau)
            print("Match nul ! 🤝")
            break

        joueur_actuel = joueur_ia if joueur_actuel == joueur_humain else joueur_humain


# Fonction pour afficher le plateau
def afficher_plateau(plateau):
    print(f"""
     {plateau[0]} | {plateau[1]} | {plateau[2]} 
    ---+---+---
     {plateau[3]} | {plateau[4]} | {plateau[5]} 
    ---+---+---
     {plateau[6]} | {plateau[7]} | {plateau[8]} 
    """)


# Fonction pour obtenir la position du joueur humain
def obtenir_position(joueur, plateau):
    while True:
        try:
            position = int(input(f"Joueur {joueur}, entrez une position (1-9) : ")) - 1
            if 0 <= position <= 8 and plateau[position] == " ":
                return position
            else:
                print("Position invalide. Essayez à nouveau.")
        except ValueError:
            print("Veuillez entrer un nombre valide entre 1 et 9.")


# Fonction pour vérifier la victoire
def verifier_victoire(plateau, joueur):
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6],             # Diagonales
    ]
    return any(all(plateau[i] == joueur for i in combi) for combi in combinaisons)


# Fonction IA : Algorithme Minimax
def minimax(plateau, profondeur, is_maximizing, joueur_ia, joueur_humain):
    if verifier_victoire(plateau, joueur_ia):
        return 10 - profondeur
    if verifier_victoire(plateau, joueur_humain):
        return profondeur - 10
    if " " not in plateau:  # Match nul
        return 0

    if is_maximizing:
        meilleur_score = -math.inf
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = joueur_ia
                score = minimax(plateau, profondeur + 1, False, joueur_ia, joueur_humain)
                plateau[i] = " "
                meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = math.inf
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = joueur_humain
                score = minimax(plateau, profondeur + 1, True, joueur_ia, joueur_humain)
                plateau[i] = " "
                meilleur_score = min(meilleur_score, score)
        return meilleur_score


# Fonction pour déterminer le meilleur coup pour l'IA
def meilleur_coup(plateau, joueur_ia):
    meilleur_score = -math.inf
    coup = -1
    joueur_humain = "X"
    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = joueur_ia
            score = minimax(plateau, 0, False, joueur_ia, joueur_humain)
            plateau[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                coup = i
    return coup


# Boucle principale pour gérer plusieurs parties
while True:
    jouer_tic_tac_toe()
    replay = input("Voulez-vous rejouer ? (o/n) : ").strip().lower()
    if replay != 'o':
        print("Merci d'avoir joué ! À bientôt.")
        break
