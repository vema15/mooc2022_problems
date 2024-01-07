# Write your solution here
import json

class PlayerSearch():
    def __init__(self):
        self.player_information_list = []

    def process_information(self, user_json):
        with open(user_json) as player_info_json:
            data = player_info_json.read()
        synthesized_info = json.loads(data)
        self.player_information_list = synthesized_info

    def search_for_player(self, player_name):
        print()
        player_info = [player for player in self.player_information_list if player['name'] == player_name]
        print(f'{player_info[0]["name"]+(" " * (21-len(player_info[0]["name"])))}{player_info[0]["team"]}{" " * (4-len(str(player_info[0]["goals"])))}{player_info[0]["goals"]} +{" " * (3-(len(str(player_info[0]["assists"]))))}{player_info[0]["assists"]} ={" " * (4-(len(str(player_info[0]["goals"] + player_info[0]["assists"]))))}{player_info[0]["goals"]+player_info[0]["assists"]}')

    def list_teams(self):
        unique_teams = []
        for player in self.player_information_list:
            if player["team"] not in unique_teams:
                unique_teams.append(player["team"])
        for team in sorted(unique_teams):
            print(team)

    def list_countries(self):
        unique_countries = []
        for player in self.player_information_list:
            if player["nationality"] not in unique_countries:
                unique_countries.append(player["nationality"])
        for country in sorted(unique_countries):
            print(country)

    def team_rankings(self, select_team):
        print()
        team_list = sorted(list(filter(lambda x:x['team'] == select_team, self.player_information_list)), key=lambda x:x['goals'] + x["assists"], reverse=True)
        for player in team_list:
            print(f'{player["name"]+(" " * (21-len(player["name"])))}{player["team"]}{" " * (4-len(str(player["goals"])))}{player["goals"]} +{" " * (3-(len(str(player["assists"]))))}{player["assists"]} ={" " * (4-(len(str(player["goals"] + player["assists"]))))}{player["goals"]+player["assists"]}')

    def country_rankings(self, select_country):
        print()
        country_list = sorted(list(filter(lambda x:x['nationality'] == select_country, self.player_information_list)), key=lambda x:x['goals'] + x["assists"], reverse=True)
        for player in country_list:
            print(f'{player["name"]+(" " * (21-len(player["name"])))}{player["team"]}{" " * (4-len(str(player["goals"])))}{player["goals"]} +{" " * (3-(len(str(player["assists"]))))}{player["assists"]} ={" " * (4-(len(str(player["goals"] + player["assists"]))))}{player["goals"]+player["assists"]}')

    def most_points(self, amount: int):
        ordered_list = sorted([player for player in self.player_information_list], key=lambda x: (x['goals']+x['assists'], x['goals']), reverse=True)
        i = 0
        while i <= amount-1:
            print(f'{ordered_list[i]["name"]+(" " * (21-len(ordered_list[i]["name"])))}{ordered_list[i]["team"]}{" " * (4-len(str(ordered_list[i]["goals"])))}{ordered_list[i]["goals"]} +{" " * (3-(len(str(ordered_list[i]["assists"]))))}{ordered_list[i]["assists"]} ={" " * (4-(len(str(ordered_list[i]["goals"] + ordered_list[i]["assists"]))))}{ordered_list[i]["goals"]+ordered_list[i]["assists"]}')
            i += 1

    def most_goals(self, amount: int):
        ordered_list = sorted([player for player in self.player_information_list], key=lambda x: (x['goals'], -x['games']), reverse=True)
        i = 0
        while i <= amount-1:
            print(f'{ordered_list[i]["name"]+(" " * (21-len(ordered_list[i]["name"])))}{ordered_list[i]["team"]}{" " * (4-len(str(ordered_list[i]["goals"])))}{ordered_list[i]["goals"]} +{" " * (3-(len(str(ordered_list[i]["assists"]))))}{ordered_list[i]["assists"]} ={" " * (4-(len(str(ordered_list[i]["goals"] + ordered_list[i]["assists"]))))}{ordered_list[i]["goals"]+ordered_list[i]["assists"]}')
            i += 1

class PlayerSearchApplication():
    def __init__(self):
        self.player_search = PlayerSearch()

    def compile_json(self):
        user_json = input("file name: ")
        self.player_search.process_information(user_json)
        print(f"read the data of {len(self.player_search.player_information_list)} players")
        print()
    
    def execute(self):
        self.compile_json()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
        while True:
            print()
            try:
                user_input = int(input("command: "))
            except:
                print("Please enter a valid command")
            if user_input == 0:
                break
            elif user_input == 1:
                player_input = input("name: ")
                self.player_search.search_for_player(player_input)
            elif user_input == 2:
                self.player_search.list_teams()
            elif user_input == 3:
                self.player_search.list_countries()
            elif user_input == 4:
                team_input = input("team: ")
                self.player_search.team_rankings(team_input)
            elif user_input == 5:
                country_input = input("country: ")
                self.player_search.country_rankings(country_input)
            elif user_input == 6:
                amount_input = int(input("how many: "))
                self.player_search.most_points(amount_input)
            elif user_input == 7:
                total_input = int(input("how many: "))
                self.player_search.most_goals(total_input)

application = PlayerSearchApplication()
application.execute()