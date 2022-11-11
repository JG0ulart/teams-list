from colors import bcolors
from teams import Teams

teams = Teams("Europe")
f = open('trophy.txt','r')
def menu():
    global option
    print(f"""{bcolors.WARNING}{bcolors.BOLD}{f.read()}{bcolors.ENDC}""")
    option = input(f"{bcolors.OKGREEN}{bcolors.BOLD}Choose one of this options below:\n 1: Add team \n 2: Del team \n 3: List our teams\n 4: Quit \nYour option: {bcolors.ENDC}")


def checker():
    while True:  
        menu()         
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
            print("Option doesnt exists\nTry to use the correct options")
            