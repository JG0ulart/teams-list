class Teams:
    def __init__(self, name):
        self.name = []

    def add_teams(self, name):
        if name not in self.name:
            self.name.append(name)
            print(f"Team {name} has been aditioned in our list of teams")
        else:
            print(f'Team {name} is duplicated!')
    
    def del_teams(self, name):
        if name in self.name:
            self.name.remove(name)
            print(f"The team {name} has been removed!")
        else:
            print(f'{name} not in our list of teams')

    def list_teams(self):
        print('Our team list:')
        if self.name == []:
            print("Empty list")
        for i in self.name:
            print(i)
