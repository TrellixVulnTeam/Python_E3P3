# inicjalizacja wartosci globalnej w skrypcie
globalId = 0
class Player:
    def __init__(self, name, lastname, repr, weight, height):
        self.name = name
        self.lastname = lastname
        self.repr = repr
        self.weight = weight
        self.height = height
        global globalId # modyfikacja wartosci globalnej w skrypcie
        globalId += 1 # - wslaznik globalny niezwiazany z klasa player
        self.id = globalId # self -> id dla konkretnego obiektu
    def calculateBMI(self):
        return self.weight/pow(self.height/100,2)
    def __str__(self):

        return ("| %3d | %10s | %10s | %10s | %10d | %10d | %10.2f |"
                % (self.id,
                   self.name,
                   self.lastname,
                   self.repr,
                   self.weight,
                   self. height,
                   self.calculateBMI()))


p1 = Player("Adam","Małysz", "POL", 50, 165)
p2 = Player("Kamil","Stoch", "POL", 60, 180)
p3 = Player("Jan","Matura", "CZE", 60, 180)
p4 = Player("Martin","Schmidt", "GER", 60, 180)


print()

players = [p1, p2, p3, p4]
for player in players:
    print(player)

def getPlayers():
    for player in players:
        print(player)


def findPlayerByID(findId):
    for player in players:
        if(player.id == findId):
            print(player)




getPlayers()
print()
findPlayerByID(2)
