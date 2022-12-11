import random
import time

# use '*' for a missed hit
# use 'x' for a hit
# use '#' for a boat part
# use 'O' for empty grid

### functions ###
def possible_to_place_boat(length, field, coord, direction):
    if direction == 'y':
        for i in range(length):
            if field[int(coord[1])+i][int(coord[0])] == '#':
                return False
        return True
    elif direction == 'x':
        for i in range(length):
            if field[int(coord[1])][int(coord[0])+i] == '#':
                return False
        return True
    return False

def generate_boats(field):
    list_lengths = [6,4,4,3,3,3,2,2,2,2]
    for length in list_lengths:
        y_or_x = random.randint(0,1)
        
        # generate a boat in the Y-axis
        if y_or_x == 0:
            direction = 'y'
            while True: 
                possible_coord = [random.randint(0,len(field)-1),random.randint(0,len(field)-length-1)]
                if possible_to_place_boat(length, field, possible_coord, direction):
                    for index in range(length):
                        field[possible_coord[1]+index][possible_coord[0]] = '#'
                    break
                
        # generate a boat in the X-axis
        else:
            direction = 'x'
            while True: 
                possible_coord = [random.randint(0,len(field)-1-length),random.randint(0,len(field)-1)]
                if possible_to_place_boat(length, field, possible_coord, direction):
                    for index in range(length):
                        field[possible_coord[1]][possible_coord[0]+index] = '#'
                    break
    return field    
    
def generate_field():
    field = []
    for i in range(0, 10):
        field.append([])
        for j in range(1, 11):
            field[i].append(str("O"))
    return field

def is_already_hit(coord, field):
    x = int(coord[0])
    y = int(coord[1])
    if field[y-1][x-1] == '*' or field[y-1][x-1] == 'x':
        return True
    return False

def hit_or_miss(shot, field):
    if field[shot[1]-1][shot[0]-1] == 'O':
        return "Miss!"
    elif field[shot[1]-1][shot[0]-1] == '#':
        return "Hit!"

def ask_for_new_shot():
    coord = list(input("Choose a new coordinate where u want to shoot at (seperated by a space).\n").split())
    coord[0] = int(coord[0])
    coord[1] = int(coord[1])
    return coord

def print_field(field):
    list_field = field
    list1 = []
    for i in range(len(list_field)+1):
        list1.append(i)
    list_field = [list1] + list_field
    for i in range(1, len(list_field)):
        list_field[i] = [i] + list_field[i]
    for i in range(len(list_field)):
        print(*list_field[i],sep=' ')
    print('')
    
def user_builds_boats(field):
    list_all_boat_lengths = [6,4,4,3,3,3,2,2,2,2]
    print("This is your field:\n")
    print_field(field)
    for length in list_all_boat_lengths:
        
        direction = input(f"In which direction do you want to place a boat with a length of {length} blocks. (x or y)\n")
        
        if 'y' in direction.lower():
            while True: 
                coord = list(input(f"Where do you want to place that boat with a length of {length} blocks. (coordinate x y, seperated by a space)\n").split())
                coord[0] = (int(coord[0]) - 1)
                coord[1] = (int(coord[1]) - 1)
                if len(coord) == 2 and coord[1] <= (len(field)-length) and coord[1] > -1 and coord[0] > -1 and coord[0] < 10:
                    if possible_to_place_boat(length, field, coord, 'y'):
                        for index in range(length):
                            field[coord[1]+index][coord[0]] = '#'
                        break
                else:
                    print("invalid coordinate, try again\n")
                    
        elif 'x' in direction.lower():
            while True: 
                coord = list(input(f"Where do you want to place that boat with a length of {length} blocks. (coordinate x y, seperated by a space)\n").split())
                coord[0] = (int(coord[0]) - 1)
                coord[1] = (int(coord[1]) - 1)
                if len(coord) == 2 and coord[0] <= (len(field)-length) and coord[0] > -1 and coord[1] > -1 and coord[1] < 10:
                    if possible_to_place_boat(length, field, coord, 'x'):
                        for index in range(length):
                            field[coord[1]][coord[0] + index] = '#'
                        break
                else:
                    print("invalid coordinate, try again\n")
                    
        print("This is your new field:\n")
        print_field(field)
    print("That's it, you have made your army, time to attack the enemy!")
    return field

def draw_shots_on_field(shot, field, field_to_draw):
    if hit_or_miss(shot, field) == 'Hit!':
        field_to_draw[shot[1]-1][shot[0]-1] = 'x'
    else:
        field_to_draw[shot[1]-1][shot[0]-1] = '*'
    return field_to_draw

def generate_shot(field_opponent, list_shots):
    while True:    
        randomx = random.randint(1,10)
        randomy = random.randint(1,10)
        if field_opponent[randomy-1][randomx-1] != 'x' and field_opponent[randomy-1][randomx-1] != '*':
            if [randomx, randomy] not in list_shots:
                return [randomx,randomy]
            
def draw_shots_on_player_field(shot, field):
    if hit_or_miss(shot, field) == 'Hit!':
        field[shot[1]-1][shot[0]-1] = 'x'
    else:
        field[shot[1]-1][shot[0]-1] = '*'
    return field

def player_has_won(field):
    counter = 0
    for index1 in range(len(field)):
        for index2 in range(len(field[index1])):
            if field[index1][index2] == 'x':
                counter += 1
    if counter == 31:
        return True
    return False


### main ###
def main():
    # get a list of all shots performed by the computer
    list_comp_shots_computer= []
#     list_all_shots_player1 = [] # DISABLE IN RELEASE
    
    # generate empty fields
    field_player1 = generate_field()
    field_computer = generate_field()
    field_shots = generate_field()
    
    # generate boats of computer
    field_computer = generate_boats(field_computer)
#    field_player1 = generate_boats(field_player1)
    
    # print the user his field and start asking to place boats
    user_builds_boats(field_player1) # ENABLE IN RELEASE
    
    # start the shooting!
    while True:
        while True:
            shot_against_computer = ask_for_new_shot()
            # check if the coordinate already has been hit
            if is_already_hit(shot_against_computer, field_shots):
                print("You've already hit that coordinate!")
            else:
                break
            
#       shot_against_computer = generate_shot(field_shots, list_all_shots_player1)
#       list_all_shots_player1.append(shot_against_computer)

        print(hit_or_miss(shot_against_computer, field_computer))
        
        # add shot to map of hits against computer
        field_shots = draw_shots_on_field(shot_against_computer, field_computer, field_shots)
        
        # give the user some delay, to register if he has hit or missed the shot
        time.sleep(1.3)
        
        # check if the game is over and player1 has won
        if player_has_won(field_shots):
            print("\nYou have won the game!")
            print("\nField of all your shots:")
            print_field(field_shots)
            break
        
        # print it so the user knows where he can shoot if it was a hit
        print("\n--- Field Opponent ---")
        print_field(field_shots)
        
        # make the computer shoot
        shot_computer = generate_shot(field_player1, list_comp_shots_computer)
        list_comp_shots_computer.append(shot_computer)
        print(f"You have been shot at ({shot_computer[0]},{shot_computer[1]}). It was a {hit_or_miss(shot_computer, field_player1)}")
        
        # give the user some delay, to register if he has been hit or not
        time.sleep(1.3)
        
        # check if the game if over and the computer has won
        if player_has_won(field_player1):
            print("\nThe computer has won the game!")
            print("\nField of all the computer's shots:")
            print_field(field_player1)
            break
        
        # show the hit on the player's field
        field_player1 = draw_shots_on_player_field(shot_computer, field_player1)
        print("\n---- Your Field ----")  
        print_field(field_player1)
        
        
    
    
    
    


if __name__ == '__main__':
    main()