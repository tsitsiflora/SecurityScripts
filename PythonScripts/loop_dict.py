#this script loops through a dictionary and pluralize the words according to number

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

def game_stats(games_won=games_won):
    '''this function goes through the key value pairs in the dictionary 
    and checks how many games a person has won, then prints the results'''
    for name, num_games in games_won.items():
        games = 'game' if num_games == 1 else 'games'
        print(f'{name} won {num_games} {games}')

game_stats(games_won)