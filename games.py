import random

class candies:
    

    def __init__(self, candies_count = 2021, max = 28, min = 1):
        self._candies_left = candies_count
        self._take_max = max
        self._take_min = min
        


    def _can_move(self, count):
        return self._candies_left - count >= 0 and count <= self._take_max and count >= self._take_min

    def _is_win(self):
        return self._candies_left == 0


    def _make_player_move(self, candies_count, player_name = 'Игрок'):
        if not self._can_move(candies_count):
            return False
        self._candies_left -= candies_count
        print(f'{player_name} забирает {candies_count} конфет. Осталось {self._candies_left}')
        return True
        
    def _make_bot_move(self):
        candies_count = 0
        if self._candies_left <= self._take_max:
            candies_count = self._candies_left
            self._candies_left = 0
        elif self._candies_left <= (self._take_max*2 + self._take_min):
            candies_count = self._candies_left - self._take_max - self._take_min
            self._candies_left -= candies_count            
        else:
            candies_count = random.randint(self._take_min, self._take_max)
            self._candies_left -= candies_count
        
        print(f'Бот забирает {candies_count} конфет. Осталось {self._candies_left}')
        return True


    def start_game_pvc(self):
        print(f'На столе лежит {self._candies_left} конфет.')
        print(f'Можно взять от {self._take_min} до {self._take_max}')
        while self._candies_left > 0:
            count = int(input('Сколько конфет взять? '))
            if not self._make_player_move(count):
                print('Столько конфет взять нельзя, попробуйте снова.')
                continue
            if(self._is_win()):
                print('Игрок выиграл')
                break
            self._make_bot_move()
            if(self._is_win()):
                print('Бот выиграл')
                break


    def start_game_pvp(self, player_count = 2):
        if player_count < 2:
            print('Миниальное количество игроков - 2')
            return
        print(f'На столе лежит {self._candies_left} конфет.')
        print(f'Можно взять от {self._take_min} до {self._take_max}')
        while self._candies_left > 0:
            player = 1
            while player <= player_count:
                name = 'Игрок ' + str(player)
                count = int(input(f'{name} ходит. Сколько конфет взять? '))
                if not self._make_player_move(count, name):
                    print('Столько конфет взять нельзя, попробуйте снова.')
                    continue
                if(self._is_win()):
                    print(f'{name} выиграл')
                    return
                player+=1
            
class tic_tac_toe:

    __map = [1,2,3,
    4,5,6,
    7,8,9]

    __win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


    def __print_map(self):
        print(f'{self.__map[0]} {self.__map[1]} {self.__map[2]}' )
        print(f'{self.__map[3]} {self.__map[4]} {self.__map[5]}' )
        print(f'{self.__map[6]} {self.__map[7]} {self.__map[8]}' )


    def __make_move(self, num, chr):
        idx = self.__map.index(num)
        self.__map[idx] = chr


    def __is_win(self):
        win = ''
        for w in self.__win:
            if self.__map[w[0]] == "X" and self.__map[w[1]] == "X" and self.__map[w[2]] == "X":
                win = "X"
            if self.__map[w[0]] == "O" and self.__map[w[1]] == "O" and self.__map[w[2]] == "O":
                win = "O"   
        return win

    def pvp(self):
        chr = 'X'
        while True:
            self.__print_map()
            num = int(input(f'Где поставить {chr}?'))
            self.__make_move(num, chr)

            if chr == 'X':
                chr = 'O'
            else:
                chr = 'X'
            
            win = self.__is_win()
            if(win != ''):
                print(f'{win} выиграли')
                break
            







            


        




