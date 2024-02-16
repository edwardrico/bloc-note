import requests
import time

note = []


def cree_note(nouvelle_note):
    note.append(nouvelle_note)


def affacer_note(note_a_supprimer):
    if note_a_supprimer in note:
        note.remove(note_a_supprimer)


def rechercher_note(note_a_rechercher):
    if note_a_rechercher in note:
        print("Note trouvée : ", note_a_rechercher)
    else:
        print("Votre note n'existe pas !")


def afficher_notes():
    print("Liste de notes : ")
    for n in note:
        print(n)


def main():
    while True:
        print("Vous souhaitez faire quoi:\n")
        print(" 1 - Créer une note !")
        print(" 2 - Effacer une note !")
        print(" 3 - Recherche une note !")
        print(" 4 - Afficher toutes les notes !")
        print(" 5 - Terminer \n ")

        try:
            choix = int(input("Faites un choix de /1/2/3/4/5/ : "))
        except ValueError:
            print("Erreur, vous devez rentre un nombre pour votre choix. Réessayez.")
            continue

        if choix == 5:
            print("Au revoir")
            break

        elif choix == 1:
            note_texte = input("Entrez votre note : ")
            cree_note(note_texte)
            if len(note_texte) > 200:
                print("Désolé, votre note est trop longue. La limite de caractères est de 200.")
            else:
                print("Parfait, votre note a été enregistrée.")

        elif choix == 2:
            note_a_supprimer = input("Entrez la note à supprimer : ")
            affacer_note(note_a_supprimer)

        elif choix == 3:
            note_a_rechercher = input("Entrez la note à rechercher : ")
            rechercher_note(note_a_rechercher)

        elif choix == 4:
            afficher_notes()

        time.sleep(2)


if __name__ == "__main__":
    main()
