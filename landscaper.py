# tools array
tools = [
    {'name': "teeth", "generate": 1, "price": 0},
    {'name': "scissor", "generate": 5, "price": 5},
    {'name': "lawnmower", "generate": 50, "price": 25},
    {'name': "battery-powered lawnmower", "generate": 100, "price": 250},
    {'name': "students", "generate": 250, "price": 500}
]

# player
player = {
    "tool": 0, # index of the tools array, player starts with the first basic tool
    "money": 0, # initially the player has $0
    "winStatus": False # at the start of the game player has not won the game
}

# function to cut lawn
def cut_lawn():
    tool = tools[player['tool']]
    
    # moneyn earned by cutting lawn
    player['money'] +=  tool['generate']
    print(f"You earned {tool['generate']} by cutting the lawn with {tool['name']}.")


def upgrade_tool():
    if (player['tool'] + 1 < len(tools)): # checking if player has tools to upgrade to 
        nextTool = tools[player['tool'] + 1]

        # checking if player has enough money to upgrade
        if (player['money'] >= nextTool['price']):
            player['tool'] += 1 # upgraded
            player['money'] -= nextTool['price'] # deducting amount after purchase of new tool
        else:
            print("You don't have enough money to upgrade. Continue cutting lawn to earn money.")
    else: # case when player has no more tools to upgrade to
        print("You don't have tools to upgrade to.")

# win condition check
def winCondition():
  # winning condition: have a team of starving students and $1000
    if ((player['tool'] == len(tools)- 1) and (player['money'] >= 1000)):
        player['winStatus'] = True

        print("Congrats! You have won!")
    else:
        pass


print("Welcome to Landscape")

while (player['winStatus'] == False): 

    currentAmount = player['money']
    currentToolIndex = player['tool']
    response = input(f"You are currently using {tools[currentToolIndex]['name']} and have ${currentAmount}. Do you want to [c]ut the lawn or [u]pgrade your tool? Enter c/u:")

    if (response == 'c'):
        cut_lawn()

    if (response == 'u'):
        upgrade_tool()

    if (response != 'u' and response != 'c'):
        print("Invalid reponse, please enter 'c' or 'u'")

    winCondition() # check if player won

    if player['winStatus']: # if player won the game
        response = input(f"Do you want to [r]eplay the game or [q]uit? Enter r/q:")

        if (response == 'r'): 

            # resetting player credentials
            player['winStatus'] = False
            player['money'] = 0
            player['tool'] = 0

        if (response == 'q'):
            break

        if (response != 'r' and response != 'q'):
            print("Invalid reponse, please enter 'r' or 'q'")
