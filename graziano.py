import random
import csv

class Game:
    def __init__(self):
        self.points = 100
        self.collection = []

    def open_pack(self):
        pack = [random.choices(['Comune', 'Non Comune', 'Rara', 'Ultra Rara'], [0.7, 0.2, 0.09, 0.01])[0] for _ in range(5)]
        self.collection.extend(pack)
        self.points += sum([{'Comune': 1, 'Non Comune': 3, 'Rara': 5, 'Ultra Rara': 10}[card] for card in pack]) - 10
        print(f"Carte: {pack}")

    def show(self):
        print(f"Punti: {self.points}\nCollezione: {self.collection}")

    def save(self):
        with open('collezione.csv', 'w', newline='') as f:
            csv.writer(f).writerow(self.collection)

def menu():
    game = Game()
    while True:
        choice = input("1. Apri pacchetto\n2. Mostra collezione\n3. Mostra punti\n4. Salva\n5. Esci\nScegli: ")
        if choice == '1': game.open_pack()
        elif choice == '2': game.show()
        elif choice == '3': game.show()
        elif choice == '4': game.save()
        elif choice == '5': break

menu()
