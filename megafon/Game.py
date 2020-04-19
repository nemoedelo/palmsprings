from random import randint

from megafon.GameException import GameException


class Game:

    def __init__(self, card_generator, mode):
        self.card_generator = card_generator
        self.used_numbers = []
        self.rolled_count = 0
        self.mode = mode

    def start(self):
        user_card = self.card_generator.generate_card("User")
        pc_card = self.card_generator.generate_card("PC")
        while not user_card.is_winner() and not pc_card.is_winner():
            try:
                self.play_turn(user_card, pc_card)
            except(GameException):
                msg = "User has lost the Game -- wrong answer"
                print(msg)
                return msg

    def play_turn(self, user_card, pc_card):
        rand = self.roll()
        print(f"Новый бочонок {rand}, осталось {90 - len(self.used_numbers)}")
        if rand == 77:
            print("77 -- ГУСИ ЛЕБЕДИ!")

        print("----------- USER---------")
        print(user_card)
        print("----------- PC---------")
        print(pc_card)
        optional_number = user_card.handle_round(rand)
        if self.mode == "manual":
            number_present = optional_number is not None
            user_answer = input("Введенный номер есть в карте? (Y/N)")
            if (number_present and user_answer == "N"):
                raise GameException("The number was found, but user answered No")
            elif not number_present and user_answer == "Y":
                raise GameException("The number was not found, but user answered Yes")

        pc_card.handle_round(rand)

    def roll(self):
        rand = randint(1, 90)
        if rand in self.used_numbers:
            return self.roll()
        else:
            self.used_numbers.append(rand)
            return rand
