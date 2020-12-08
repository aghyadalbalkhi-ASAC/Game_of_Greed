from game_of_greed.game_logic import GameLogic,Banker
# from game_logic import GameLogic,Banker
#from game_of_greed import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    def new_round(self,remaining_dice,round):
        print(f'Starting round {round}')
        print(f'Rolling {remaining_dice} dice...')
        roll = self.roller(remaining_dice)
        #roll=GameLogic.roll_dice(remaining_dice)
        print(','.join([str(i) for i in roll]))
        return input('Enter dice to keep (no spaces), or (q)uit: ')

    @staticmethod
    def quit_game(score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')
        



    def play(self):
        nope_player = Banker()
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')


        elif res == 'y':                                   # we have to path [new round - current round]
            
            #initializing Variable
            round = 1
            remaining_dice = 6
            new_round= True

            #looping until reach break ('q')
            while True:

                # run this code if we are in a new round                                     
                if new_round ==True:                        
                    dice_to_keep=self.new_round(remaining_dice,round)

                # handeling the Integers -> If Not Integers handel execep where the inpu is string ['q' - 'b']
                try:            
                    if type(int(dice_to_keep)) == int:

                        # calc the score using the static methode in Game_Logic  - input -> tuple
                        user_aside =()
                        user_aside = user_aside+(int(dice_to_keep),)
                        nope_player.shelf(GameLogic.calculate_score(user_aside))

                        # decrese The Remainig Dice
                        remaining_dice-=1
                        print(f"You have {nope_player.shelved} unbanked points and {remaining_dice} dice remaining")
                        dice_to_keep= input('(r)oll again, (b)ank your points or (q)uit ')

                        # To Prevent handel the new_round msg when back to hande ['b' or 'q']
                        if dice_to_keep == 'b' or dice_to_keep =='q':
                            new_round =False
                except ValueError:

                        if dice_to_keep == 'b':
                            print(f'You banked {nope_player.shelved} points in round {round}')
                            nope_player.bank()
                            print(f'Total score is {nope_player.balance} points')
                            round+=1
                            new_round=True
                            remaining_dice=6

                        if dice_to_keep == 'q':
                            Game.quit_game(nope_player.balance)
                            break


if __name__ == '__main__':
    game = Game()
    game.play()