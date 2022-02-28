class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'Constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party county', self.x)

q = PartyAnimal('Kelven')
n = PartyAnimal('Dragonforce')

q.party()
n.party()
q.party()