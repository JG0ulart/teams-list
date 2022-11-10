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
        for i in self.name:
            print(i)

teams = Teams('Europa')
list_teams = ['Vallencia', 'PSG', 'Borussia', 'Real Madrid', 'Barcelona', 'Bayer']

for i in list_teams:
    teams.add_teams(i)

while True:
    option = input("Choose one of this options below:\n 1: Add team \n 2: Del team \n 3: List our teams\n 4: Quit \nYour option: ")

    if option == "1":
        team = input("Write your team name for include in our\n Team name: ")
        teams.add_teams(team)
        print("Now our team list is:\n")
        teams.list_teams()
        
    elif option == "2":
        team = input("Write the team name that you want delete\n Team name: ")
        teams.del_teams(team)
        print("Now our team list is:\n")
        teams.list_teams()

    elif option == "3":
        teams.list_teams()
    
    elif option == "4":
        print("Ending...\nBye bye!")
        break

    else:
        print("Option doesnt exists\nSee you later!")
        break