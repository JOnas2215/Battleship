import Battleship_functions as z
import time

def main():
    
    print("---------------------------------- OPEN BETA ----------------------------------\nPlease be aware that the game might run into errors when entering unusual responses.\n\n")
    
    print("Welcome To Battleship. In this game your objective is to destroy all the boats of your opponent.\nBut if your opponent can shoot all your boats before you, they win...\n")
    
    # get a list of all shots performed by the computer
    list_comp_shots_computer= []
    
    # generate empty fields
    field_player1 = z.generate_field()
    field_computer = z.generate_field()
    field_shots = z.generate_field()
    
    # generate boats of computer
    field_computer = z.generate_boats(field_computer)
    
    # tell the user we will start building their boats and how the game exactly works
    print("Before you can start playing, here are the important details of the game: 'x' means hit and '*' means miss.")
    print('Coordinates in this game have the following format: x y (it is important that there is a space between the x and y coordinates before you press enter).')
    print("The process of placing your boats will firstly ask how the boat should be positioned and then ask at what coordinate you want to place it.")
    print("Now you're ready to start building your sea army. Every part of a boat will be marked as '#' on your field. Good luck!\n")
    
    # wait for user to start the game
    start = input("Press enter to start the game.\n")
    if start == 'secret':
        print('\nYou have found the secret, congratulations! You can now celebrate this enormous achievement.\n')
    
    # wait 
    # print the user his field and start asking to place boats
    print("Boat placing progress started!")
    z.user_builds_boats(field_player1)
    
    # start the shooting!
    while True:
        while True:
            shot_against_computer = z.ask_for_new_shot()
            # check if the coordinate already has been hit
            if z.is_already_hit(shot_against_computer, field_shots):
                print("You've already hit that coordinate!")
            else:
                break

        print(z.hit_or_miss(shot_against_computer, field_computer))
        
        # add shot to map of hits against computer
        field_shots = z.draw_shots_on_field(shot_against_computer, field_computer, field_shots)
        
        # give the user some delay, to register if he has hit or missed the shot
        time.sleep(1.3)
        
        # check if the game is over and player1 has won
        if z.player_has_won(field_shots):
            print("\nYou have won the game!")
            print("\nField of all your shots:")
            z.print_field(field_shots)
            break
        
        # print it so the user knows where he can shoot if it was a hit
        print("\n--- Field Opponent ---")
        z.print_field(field_shots)
        
        # make the computer shoot
        shot_computer = z.generate_shot(field_player1, list_comp_shots_computer)
        list_comp_shots_computer.append(shot_computer)
        print(f"You have been shot at {shot_computer}. It was a {z.hit_or_miss(shot_computer, field_player1)}")
        
        # give the user some delay, to register if he has been hit or not
        time.sleep(1.3)
        
        # check if the game if over and the computer has won
        if z.player_has_won(field_player1):
            print("\nThe computer has won the game!")
            print("\nField of all the computer's shots:")
            z.print_field(field_player1)
            break
        
        # show the hit on the player's field
        field_player1 = z.draw_shots_on_player_field(shot_computer, field_player1)
        print("\n---- Your Field ----")  
        z.print_field(field_player1)
        


if __name__ == '__main__':
    main()
