from game_of_greed.game_logic import GameLogic,Banker
# from game_logic import GameLogic,Banker
#from game_of_greed import GameLogic

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    @staticmethod
    def new_round(remaining_dice,round):
        print(f'Starting round {round}')
        print(f'Rolling {remaining_dice} dice...')
    
    def rolling(self,remaining_dice):
        roll = self.roller(remaining_dice)
        #roll=GameLogic.roll_dice(remaining_dice)
        print(','.join([str(i) for i in roll]))
        return roll

    @staticmethod
    def user_input():
        return input('Enter dice to keep (no spaces), or (q)uit: ')
    
    @staticmethod
    def quit_game(score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')

    @staticmethod
    def convert_input_to_tuple(user_input):
        digits = [int(x) for x in str(user_input)]
        return tuple(digits)


    @staticmethod
    def cheatting(rolled,input):
        t1 = list(rolled)
        t2 = list(input)
        for n in t2:
            try:
                index = (t1.index(n))
                t1.pop(index)
            except ValueError:
                return True
        return False

    @staticmethod
    def zilch(round,roll,bank=0,remaining_dice=0):
        if GameLogic.calculate_score(roll)==0 or remaining_dice==0:
            print('Zilch!!! Round over')
            print(f'You banked 0 points in round {round}')
            print(f'Total score is {bank} points')
            return True
        return False

    @staticmethod
    def unbankmsg(shelved,remaining_dice):
        if shelved ==1500:
            remaining_dice=0
        print(f"You have {shelved} unbanked points and {str(remaining_dice)} dice remaining")

    @staticmethod
    def action():
        return input('(r)oll again, (b)ank your points or (q)uit ')


    def play(self):
        nope_player = Banker()
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')

        elif res == 'y':
            remaining_dice =6
            round =1
            user_input=' '
            action_status = True
            EndOfGame=True
            while EndOfGame:

                if action_status:
                    # Starting New Round
                    remaining_dice=6
                    Game.new_round(remaining_dice,round)
                    roll=self.rolling(remaining_dice)

                while Game.zilch(round,roll,nope_player.balance,remaining_dice):
                    round+=1
                    Game.new_round(remaining_dice,round)
                    roll=self.rolling(remaining_dice)
                    Game.zilch(round,roll,nope_player.balance,remaining_dice)

                user_choice=Game.user_input()
                if user_choice =='q':
                    Game.quit_game(nope_player.balance)
                    break


                if user_choice.isdigit():
                    user_aside =Game.convert_input_to_tuple(int(user_choice))

                    cheat = Game.cheatting(roll,user_aside)
                    while cheat:
                        print('Cheater!!! Or possibly made a typo...')
                        print(','.join([str(i) for i in roll]))
                        user_choice=Game.user_input()
                        if user_choice.isdigit():
                            user_aside =Game.convert_input_to_tuple(int(user_choice))
                        cheat = Game.cheatting(roll,user_aside)

                    nope_player.shelf(GameLogic.calculate_score(user_aside))

                    Game.unbankmsg(nope_player.shelved,remaining_dice-len(user_choice))
                    if nope_player.shelved == 1500:
                        remaining_dice=6
                        user_choice=''
                    action= Game.action()
                while True :
                    if action == 'b':
                            print(f'You banked {nope_player.shelved} points in round {round}')
                            nope_player.bank()
                            print(f'Total score is {nope_player.balance} points')
                            round +=1
                            action_status = True
                            break

                    elif action == 'r':
                        action_status = False
                        print(f'Rolling {remaining_dice-len(user_choice)} dice...')
                        roll=self.rolling(remaining_dice-len(user_choice))

                        while Game.zilch(round,roll,nope_player.balance,remaining_dice):
                            round+=1
                            remaining_dice=6
                            Game.new_round(remaining_dice,round)
                            roll=self.rolling(remaining_dice)
                            Game.zilch(round,roll,nope_player.balance,remaining_dice)
                        remaining_dice = remaining_dice-len(user_choice)
                        break
                    
                    if action == 'q':
                        Game.quit_game(nope_player.balance)
                        action_status=False
                        EndOfGame=False
                        break

        else:
            print('Enter Yes (yn) or No (n)')

if __name__ == '__main__':
    game = Game()
    game.play()