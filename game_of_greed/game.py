from game_of_greed.game_logic import GameLogic
#from game_logic import GameLogic
#from game_of_greed import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    # @staticmethod
    # def print_roll(roll):
    #     print(','.join([str(i) for i in roll]))

    def play(self):
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')


        elif res == 'y':
            round = 1
            remaining_dice = 6
            score = 0
            shelf_score=0
            new_round= True
            while True:
                if new_round ==True:
                    print(f'Starting round {round}')
                    print(f'Rolling {remaining_dice} dice...')
                    roll = self.roller(remaining_dice)
                    #roll=GameLogic.roll_dice(remaining_dice)
                    print(','.join([str(i) for i in roll]))
                    dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                try:
                    if type(int(dice_to_keep)) == int:
                        user_aside =()
                        user_aside = user_aside+(int(dice_to_keep),)
                        shelf_score=GameLogic.calculate_score(user_aside)
                        remaining_dice-=1
                        print(f"You have {shelf_score} unbanked points and {remaining_dice} dice remaining")
                        dice_to_keep= input('(r)oll again, (b)ank your points or (q)uit ')
                        if dice_to_keep == 'b' or dice_to_keep =='q':
                            new_round =False
                except ValueError:

                        if dice_to_keep == 'b':
                            score+=shelf_score
                            print(f'You banked {shelf_score} points in round {round}')
                            print(f'Total score is {score} points')
                            round+=1
                            new_round=True
                            remaining_dice=6

                        if dice_to_keep == 'q':
                            print(f'Total score is {score} points')
                            print(f'Thanks for playing. You earned {score} points')
                            break
                        # else:
                        #     break


if __name__ == '__main__':
    game = Game()
    game.play()