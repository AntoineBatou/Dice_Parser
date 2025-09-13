import argparse
import random
import pathlib
import math

home = pathlib.Path.cwd()

parser = argparse.ArgumentParser(description="Lancer de dés")

parser.add_argument("base",type=str, help="Nombre de dés et de face. // Ex : 3d6 --> 3 Dès à 6 faces !")
parser.add_argument(
    "-r",
    "--repeat",
    help="Nombre de fois où les dés sont lancés !",
    type=int,
    default=1
)
parser.add_argument(
    "-l",
    "--log",
    help="Adresse ou on veut enregistrer les logs",
    type=str,
    default=home / 'log'
)

args = parser.parse_args()


config = args.base
repeat = args.repeat
path = home / f"{args.log}.txt"

total = []

separation = config.split("d")
nb_des = int(separation[0])
nb_face = int(separation[1])

def launch(nb_des, faces):
    for _ in range(nb_des * repeat):
        resultat_des = random.randint(1, faces)
        total.append(resultat_des)

def print_resultat(total):
    total_str = [str(i) for i in total]
    print(f"Résultat des dès : {", ".join(total_str)}")
    print(f"Total : {sum(total)}")
    print(f"Moyenne : {round(sum(total)/len(total), 2)}")

def save(log):
    with open (log, "a") as f:
        f.write(f"{total}\n")

launch(nb_des, nb_face)
print_resultat(total)
save(path)

