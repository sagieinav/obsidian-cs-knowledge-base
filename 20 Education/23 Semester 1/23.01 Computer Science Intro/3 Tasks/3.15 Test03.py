from typing import ForwardRef


def top_scorer(players):
	max_goals = 0
	top_player = ''
	for player in players:
		if player['goals'] > max_goals:
			top_player = player['name']
			max_goals = player['goals']
	
	return top_player

def players_by_position(players, position):
	pos_list = []
	for player in players:
		if player['position'] == position:
			pos_list.append(player['name'])
	
	return pos_list
	

def team_of_player_v1(teams, player_name):
	for team in teams:
		if player_name in teams[team]:
			return team


def team_of_player(teams, player_name):
	for team in teams.items():
		if player_name in team[-1]:
			return team[0]
		
def most_goal_scoring_team(players, teams):

	for player in players:
		for team in teams:
			if player['name'] in teams[team]:
				player['team'] = team
	
	new_teams = []
	for team in teams:
		new_teams.append({'name':team, 'players':teams[team], 'goals':0})
	
	for player in players:
		scored = player['goals']
		for team in new_teams:
			if player['name'] in team['players']:
				team['goals'] += scored
	
	most_goals = 0
	best_team = ''
	for team in new_teams:
		if team['goals'] > most_goals:
			most_goals = team['goals']
			best_team = team['name']
	
	return best_team
	

def add_goal(players, player_name):
	for player in players:
		if player['name'] == player_name:
			player['goals'] += 1
	
	
def longest_game(games):
	max_hours = 0
	longest = ''
	
	for game in games:
		if game['hours'] > max_hours:
			max_hours = game['hours']
			longest = game['title']
	
	return longest

def favourite_genre(games, gamers, gamer_name):
	target_gamer = [gamer['name'] for gamer in gamers if gamer['name'] == gamer_name][0]
	
	genres = set(game['genre'] for game in games)
	for gamer in gamers:
		for genre in genres:
			gamer[genre] = 0
	
	for gamer in gamers:
		if gamer['name'] == gamer_name:
			for game in games:
				if game['game_id'] in gamer['played']:
					gamer[game['genre']] += 1
	
	popular_genre = set()
	votes = 0
	for gamer in gamers:
		if gamer['name'] == gamer_name:
			for genre in genres:
				if gamer[genre] >= votes:
					votes = gamer[genre]
					popular_genre.add(genre)
		
	
	return popular_genre
	

def game_recommendation(games, gamers, gamer_name):
	fav_genre = favourite_genre(games, gamers, gamer_name)
	for gamer in gamers:
		if gamer['name'] == gamer_name:
			for game in games:
				if game['genre'] in fav_genre and game['game_id'] not in gamer['played']:
					return game['title']

def input_list(length = 6): # Create a user-input list
	print(f'Forming a list. Please enter {length} numbers: ')
	list = [int(input()) for item in range(length)]
	return list

import random
def random_list(length = 6, max = 100): # Create a random list
	list = [random.randint(0, max) for item in range(length)]
	return list


if __name__ == '__main__':
	# players = [
	# 	{"id": 101, "name": "Eran Zahavi", "position": "Forward", "goals": 15},
	# 	{"id": 102, "name": "Manor Solomon", "position": "Midfielder", "goals": 27},
	# 	{"id": 103, "name": "Dor Peretz", "position": "Defensive Midfielder", "goals": 3},
	# 	{"id": 104, "name": "Eli Dasa", "position": "Right Back", "goals": 21},
	# 	]
	#
	# teams = {
	# 	"Maccabi Tel Aviv": ["Eran Zahavi", "Dor Peretz"],
	# 	"Shakhtar Donetsk": ["Manor Solomon"],
	# 	"Dynamo Moscow": ["Eli Dasa"]
	# }
	#
	# print(top_scorer(players))
	#
	# position = 'Right Back'
	# print(players_by_position(players, position))
	#
	# player_name = 'Eran Zahavi'
	# print(team_of_player(teams, player_name))
	#
	# print(most_goal_scoring_team(players, teams))
	#
	# print(players)
	# add_goal(players, 'Eran Zahavi')
	# print(players)
	
	games = [
		{"game_id": 101, "title": "The Witcher 3", "genre": "RPG", "hours": 100},
		{"game_id": 102, "title": "FIFA 24", "genre": "Sports", "hours": 50},
		{"game_id": 103, "title": "Cyberpunk 2077", "genre": "RPG", "hours": 120}
	]
	
	gamers = [
	{"name": "Gamer1", "played": [101, 102]},
	{"name": "Gamer2", "played": [103]},
	{"name": "Gamer3", "played": [101, 103]}
	]
	
	# print(longest_game(games))
	
	gamer_name = 'Gamer1'
	# print(favourite_genre(games, gamers, gamer_name))
	# print(game_recommendation(games, gamers, gamer_name))
	
	# print(input_list())
	# print(random_list())
	
	arr = [[None] * 4 for row in range(5)]
	# print(arr)
	# print(view_as_matrix(arr))
	
	set1 = {10, 20, 30}
	print(set1)
	tup1 = tuple(set1)
	print(tup1)
	
	dict1 = dict([("book_id", 101), ("title", "AOT"), ("votes", 0)])
	print(dict1)
	values = dict1.values()
	print(values)
	values2 = tuple(item for item in dict1.values())
	print(values2)
	print('AOT' in values2)
	values3 = set(dict1.values())
	print(values3)
	
	print()
	pairs = dict1.items()
	# print(pairs)
	pairs1 = [pair for pair in dict1.items()]
	print(pairs1)
	pairs2 = set(dict1.items())
	# print(pairs2)
	
	for key, value in pairs1:
		print(key,value)
	